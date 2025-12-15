---
id: cmd-2
data: k exec -it shell-5d64dd647c-8l8s6 -- ash
tags:
  - exec
  - shell
type: command
output: Interactive shell prompt
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.554Z'
verified: false
validated: true
submitted: true
---
# kubectl-exec-ash

## Command

```bash
k exec -it shell-5d64dd647c-8l8s6 -- ash
```

## Description

Executes an interactive shell (ash) inside a running Kubernetes pod for command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-it` | Interactive terminal flags | Yes |
| `shell-5d64dd647c-8l8s6` | Pod name | Yes |
| `-- ash` | Shell to run | Yes |

## Examples

### Basic Usage

```bash
k exec -it pod-name -- ash
```

### Advanced Usage

```bash
k exec -it pod-name -c container -- ash
```

## Expected Output

Drops into ash shell; exit with 'exit'.

## Related

- [[commands/kubectl-apply-shell-yaml]]
