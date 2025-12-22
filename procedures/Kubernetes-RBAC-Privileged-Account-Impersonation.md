---
id: 1bf13c14-d37d-4908-a03f-f936597c5f0a
name: Kubernetes-RBAC-Privileged-Account-Impersonation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.339458+00:00'
updated_at: '2023-04-10T20:34:06.521270+00:00'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[T1078.004]]'
sub_techniques: []
tags:
  - '[[tags/Impersonating a Privileged Account]]'
  - '[[tags/Kubernetes]]'
  - '[[tags/RBAC Configuration]]'
  - impersonation
  - privilege-escalation
commands:
  - '[[commands/curl-kubernetes-impersonate-masters-group]]'
platforms:
  - Kubernetes
tools: []
validated: true
---

# Kubernetes-RBAC-Privileged-Account-Impersonation

## Summary

This procedure demonstrates how to impersonate a privileged account in a Kubernetes cluster using Role-Based Access Control (RBAC) by leveraging a valid JSON Web Token (JWT) from an impersonator account and specific impersonation headers. It allows an attacker to bypass RBAC restrictions and access sensitive resources, such as secrets in the kube-system namespace, leading to privilege escalation and potential lateral movement within the cluster.

## Description

In Kubernetes, RBAC controls access to cluster resources based on user identities and group memberships. This procedure exploits misconfigurations or overly permissive impersonation policies by crafting an HTTP request to the Kubernetes API server. Using the 'Impersonate-Group' header set to 'system:masters' (a built-in privileged group) and an impersonator's JWT, the request impersonates a master-level user to retrieve restricted data. This technique is particularly effective in environments where service accounts or users have partial impersonation rights but can be chained to access cluster-wide secrets. The target environment is a Kubernetes cluster API server, typically exposed on port 6443, and success enables data exfiltration or further exploitation like pod escapes.

## Requirements

1. A valid JWT token from an account with impersonation capabilities (e.g., a service account or user with 'impersonate' verbs in RBAC bindings).
2. Network access to the Kubernetes API server (e.g., via kubectl proxy or direct connectivity).
3. Knowledge of the cluster's API endpoint, including the master's IP address and port (default 6443).
4. The 'curl' utility installed on the attacker's machine.

## Defense

- Strictly define and audit RBAC policies to limit impersonation rights; avoid broad 'system:masters' group assignments.
- Enable Kubernetes API server auditing to log impersonation attempts and anomalous requests.
- Implement network segmentation, such as restricting API server access to trusted IPs and using mTLS.
- Monitor for unusual API calls to sensitive endpoints like /api/v1/namespaces/kube-system/secrets using tools like Falco or Prometheus.

## Objectives

1. Impersonate a privileged 'system:masters' group to bypass RBAC restrictions.
2. Retrieve sensitive secrets from protected namespaces like kube-system.
3. Escalate privileges for lateral movement or data exfiltration in the Kubernetes cluster.

## Instructions

### Step 1: Prepare Impersonation Request

**Context**: Obtain or craft the JWT token from an impersonator account (e.g., via a compromised service account). Identify the Kubernetes API server endpoint. This step ensures the request headers are correctly set to impersonate the privileged group without altering the user's identity.

**Command** ([[commands/curl-kubernetes-impersonate-masters-group]]):

```bash
curl -k -v -XGET -H "Authorization: Bearer $_JWT_TOKEN" -H "Impersonate-Group: system:masters" -H "Impersonate-User: null" -H "Accept: application/json" https://$_MASTER_IP:$_PORT/api/v1/namespaces/kube-system/secrets/
```

> This command sends a GET request to list secrets in the kube-system namespace. The '-k' flag skips SSL verification for self-signed certificates common in clusters. Verbose output ('-v') helps debug connection issues. The 'Authorization' header uses the impersonator's JWT. 'Impersonate-Group: system:masters' elevates to privileged access, while 'Impersonate-User: null' retains the original username. If successful, it returns a JSON list of secrets; failures may show 403 Forbidden if RBAC blocks the impersonation.

### Step 2: Verify Access and Extract Data

**Context**: Review the response for accessible secrets. If the request succeeds, parse the JSON to identify high-value items like service account tokens or config maps. This validates the impersonation and prepares for further actions like secret decoding.

Use standard JSON parsing tools (e.g., jq) to process the output:

```bash
# Assuming the curl output is saved to response.json
jq '.items[] | .metadata.name' response.json
```

> Expected to list secret names such as 'default-token-xyz' or etcd credentials. If no secrets are returned or an error occurs, check JWT validity or RBAC policies.
