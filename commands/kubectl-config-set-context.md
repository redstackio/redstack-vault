---
id: cmd-16
data: k config set-context pwn@kops --cluster=kops --user=pwn
tags:
  - config
  - context
type: command
output: Context updated
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.511Z'
verified: false
validated: true
submitted: true
---
# kubectl-config-set-context

## Command

```bash
k config set-context pwn@kops --cluster=kops --user=pwn
```

## Description

Sets a context linking cluster and user in kubeconfig.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pwn@kops` | Context name | Yes |
| `--cluster` | Cluster ref | Yes |
| `--user` | User ref | Yes |

## Examples

### Basic Usage

```bash
k config set-context dev@prod --cluster=prod --user=dev
```

### Advanced Usage

```bash
k config set-context ... --namespace=default
```

## Expected Output

'Context "pwn@kops" set'.

## Related

- [[commands/kubectl-config-use-context]]
