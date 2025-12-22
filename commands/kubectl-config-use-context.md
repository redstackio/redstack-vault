---
id: cmd-17
data: k config use-context pwn@kops
tags:
  - config
  - switch
type: command
output: Context switched
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.508Z'
verified: false
validated: true
submitted: true
---
# kubectl-config-use-context

## Command

```bash
k config use-context pwn@kops
```

## Description

Switches kubectl to use the specified context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pwn@kops` | Context name | Yes |

## Examples

### Basic Usage

```bash
k config use-context prod@cluster
```

### Advanced Usage

```bash
k config use-context --kubeconfig=custom.kubeconfig context
```

## Expected Output

'Now using context pwn@kops'.

## Related

- [[commands/kubectl-auth-can-i]]
