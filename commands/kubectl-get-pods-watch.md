---
id: cmd-kubectl-get-pods-watch
data: watch -n 1 'kubectl get pods --all-namespaces'
tags:
  - kubernetes
  - monitoring
type: command
output: Updated pod list every second
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.514Z'
verified: false
validated: true
submitted: true
---
# watch -n 1 'kubectl get pods --all-namespaces'

## Command

```bash
watch -n 1 'kubectl get pods --all-namespaces'
```

## Description

Watches pod status across namespaces, refreshing every 1s to detect unresponsiveness.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n 1 | Refresh interval | Yes |
| kubectl get pods --all-namespaces | Inner command | Yes |

## Examples

### Basic Usage

```bash
watch -n 1 'kubectl get pods'
```

### Advanced Usage

```bash
watch -n 5 'kubectl get pods -o wide'
```

## Expected Output

Table updates; delays/timeouts during DoS.

## Related

- [[commands/kubectl-top-nodes]]
- [[procedures/observe-kubernetes-resource-exhaustion]]
