---
id: 4ed87fe4-7511-408c-a95e-d41f3176af53
name: kubectl-auth-can-i-list-namespace-kube-system
type: command
executor: bash
data: kubectl auth can-i --list --namespace=kube-system
output: null
created_at: '2023-04-06T03:56:01.145417+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
tags:
  - authorization
  - discovery
  - kube-system
verified: true
validated: true
---

# kubectl-auth-can-i-list-namespace-kube-system

## Command

```bash
kubectl auth can-i --list --namespace=kube-system
```

## Description

This command lists the permissions of the current service account specifically in the kube-system namespace, helping identify access to critical system resources like control plane components.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--list` | Output a detailed list of permissions | Yes |
| `--namespace=kube-system` | Scope the check to the kube-system namespace | Yes |

## Examples

### Basic Usage

```bash
kubectl auth can-i --list --namespace=kube-system
```

## Expected Output

```
Resources   Non-Resource URLs   Resource Names   Verbs
---------   -----------------   --------------   -----
[]          []                  []               [get list]  # If access granted

# Or empty if no permissions.
```

Look for verbs like 'list' or 'get' on pods or secrets, indicating potential lateral movement opportunities.

## Related

- [[procedures/Kubernetes-Service-Account-Permissions-Enumeration]]
