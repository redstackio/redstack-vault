---
data: kubectl get pods --all-namespaces
tags:
  - kubernetes
  - discovery
type: command
executor: bash
platforms:
  - Kubernetes
  - Linux
id: 0a9c8e8f-b43b-44f5-bbc6-560ce8080e19
created_at: '2025-12-10T05:44:16.318Z'
updated_at: '2025-12-10T05:44:16.318Z'
verified: false
validated: true
submitted: true
---
# kubectl-get-pods

## Command

```bash
kubectl get pods --all-namespaces
```

## Description

This command lists all pods in a Kubernetes cluster across all namespaces, useful for discovering running resources during initial access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--all-namespaces` | Include all namespaces | No |
| `--server` | Specify API server | No |

## Examples

### Basic Usage

```bash
kubectl get pods --all-namespaces
```

### Advanced Usage

```bash
kubectl --server=https://target:6443 get pods --all-namespaces --insecure-skip-tls-verify
```

## Expected Output

A table listing pod names, namespaces, status, and other details if access is granted.

## Related

- #kubectl-run-job
- [[procedures/Scan-for-Exposed-Kubernetes-APIs]]
