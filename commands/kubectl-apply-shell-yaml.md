---
id: cmd-1
data: k apply -f shell.yaml
tags:
  - deploy
  - pod
type: command
output: pod/shell created
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.558Z'
verified: false
validated: true
submitted: true
---
# kubectl-apply-shell-yaml

## Command

```bash
k apply -f shell.yaml
```

## Description

Deploys a Kubernetes pod from a YAML manifest file, typically for creating a shell-accessible container like Alpine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Path to YAML manifest | Yes |
| `shell.yaml` | File defining the pod spec | Yes |

## Examples

### Basic Usage

```bash
k apply -f shell.yaml
```

### Advanced Usage

```bash
k apply -f shell.yaml --namespace=default
```

## Expected Output

'pod/shell created' or similar confirmation; check with 'k get pods'.

## Related

- [[commands/kubectl-exec-ash]]
