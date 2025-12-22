---
id: uuid-kubectl-auth-can-i-1
name: kubectl-auth-can-i-exec
type: command
executor: bash
data: kubectl auth can-i exec pod -n $_NAMESPACE
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
tags:
  - RBAC
  - authorization
verified: true
validated: true
---

# kubectl-auth-can-i-exec

## Command

```bash
kubectl auth can-i exec pod -n $_NAMESPACE
```

## Description

This command checks if the current Kubernetes user or service account has permission to perform 'exec' operations on pods in the specified namespace. It is used to verify RBAC access before attempting pod execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `exec` | The verb to check (exec for shell access) | Yes |
| `pod` | The resource type (pod) | Yes |
| `-n $_NAMESPACE` | Namespace flag with target namespace (e.g., default) | Yes |

## Examples

### Basic Usage

```bash
kubectl auth can-i exec pod -n default
```

### Advanced Usage

```bash
kubectl auth can-i exec pod --namespace=production
```

## Expected Output

A simple 'yes' or 'no' response.

yes

If access is denied:

no

## Related

- [[procedures/Kubernetes-RBAC-Pod-Exec-Privilege-Escalation]]
- [[commands/kubectl-get-pods]]
