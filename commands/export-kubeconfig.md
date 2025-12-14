---
id: cmd-13
data: export KUBECONFIG=./pwn.kconfig
tags:
  - config
  - env
type: command
output: Env set
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.519Z'
verified: false
validated: true
submitted: true
---
# export-kubeconfig

## Command

```bash
export KUBECONFIG=./pwn.kconfig
```

## Description

Sets the kubeconfig file path for kubectl operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `KUBECONFIG` | Path to config | Yes |
| `./pwn.kconfig` | Custom file | Yes |

## Examples

### Basic Usage

```bash
export KUBECONFIG=./custom.kubeconfig
```

### Advanced Usage

```bash
export KUBECONFIG=~/.kube/config
```

## Expected Output

No output; verify with 'echo $KUBECONFIG'.

## Related

- [[commands/kubectl-config-set-credentials]]
