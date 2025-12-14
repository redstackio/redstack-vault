---
id: cmd-18
data: k auth can-i '*' '*' -A
tags:
  - rbac
  - check
type: command
output: 'yes'
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.503Z'
verified: false
validated: true
submitted: true
---
# kubectl-auth-can-i

## Command

```bash
k auth can-i '*' '*' -A
```

## Description

Checks if the current user can perform actions on resources across all namespaces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'*' '*'` | Verbs and resources | Yes |
| `-A` | All namespaces | Yes |

## Examples

### Basic Usage

```bash
k auth can-i '*' '*' -A
```

### Advanced Usage

```bash
k auth can-i get pods --namespace=default
```

## Expected Output

'yes' or 'no' based on RBAC.

## Related

- [[commands/kubectl-config-use-context]]
