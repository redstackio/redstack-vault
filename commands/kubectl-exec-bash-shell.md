---
data: kubectl exec -ti ubuntu-node -- /bin/bash
tags:
  - shell
type: command
output: null
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.888Z'
id: 05c33a38-e7d4-4b63-9de6-f2f4740795fa
verified: false
validated: true
submitted: true
---
# kubectl-exec-bash-shell

## Command

```bash
kubectl exec -ti ubuntu-node -- /bin/bash
```

## Description

Executes a command in a container, opening an interactive shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ti | Interactive terminal | Yes |
| pod | Pod name | Yes |
| command | Shell to run | Yes |

## Examples

### Basic Usage

```bash
kubectl exec -it pod -- sh
```

## Expected Output

Interactive bash shell

## Related

- [[procedures/Transfer-Exploit-Script-and-Access-Pod-Shell]]
