---
data: kubectl exec -it rate-c848c5c8b-5b8vm sh
tags:
  - pod-exec
type: command
output: Interactive shell access with possible deprecation warning
executor: bash
platforms:
  - Kubernetes
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.618Z'
id: d5b45ab9-daba-4bdd-9d12-7f91709f40eb
verified: false
validated: true
submitted: true
---
# kubectl-exec-pod

## Command

```bash
kubectl exec -it rate-c848c5c8b-5b8vm sh
```

## Description

Executes a shell command inside a running pod, providing interactive access for further operations like file manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| exec | Subcommand to run in container | Yes |
| -it | Interactive terminal flags | Yes |
| rate-c848c5c8b-5b8vm | Pod name | Yes |
| sh | Shell to invoke | Yes |

## Examples

### Basic Usage

```bash
kubectl exec -it <pod-name> sh
```

### Advanced Usage

```bash
kubectl exec -it <pod-name> -- dd if=/dev/zero of=/etc/hosts
```

## Expected Output

Drops into shell; may warn about deprecated exec syntax.

## Related

- [[commands/dd-fill-etc-hosts]]
- [[procedures/Exec-Into-Pod-and-Baseline-Disk]]
