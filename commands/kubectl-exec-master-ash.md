---
id: cmd-20
data: k exec -it shell-78d66f6f7c-ft7ch -- ash
tags:
  - exec
  - master
type: command
output: Shell on master
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.498Z'
verified: false
validated: true
submitted: true
---
# kubectl-exec-master-ash

## Command

```bash
k exec -it shell-78d66f6f7c-ft7ch -- ash
```

## Description

Execs interactive ash shell into a pod running on the master node.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-it` | Interactive | Yes |
| `pod-name` | Master pod | Yes |
| `-- ash` | Shell | Yes |

## Examples

### Basic Usage

```bash
k exec -it master-pod -- ash
```

## Expected Output

Ash prompt on master.

## Related

- [[commands/wget-metadata-admin-token]]
