---
id: cmd-kubectl-proxy
data: kubectl proxy
tags:
  - kubernetes
  - proxy
type: command
output: 'Starting to serve on 127.0.0.1:8001'
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.549Z'
verified: false
validated: true
submitted: true
---
# kubectl proxy

## Command

```bash
kubectl proxy
```

## Description

Starts a local proxy to the Kubernetes API server on localhost:8001, using current kubeconfig for auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| none | Default port 8001 | No |

## Examples

### Basic Usage

```bash
kubectl proxy
```

### Advanced Usage

```bash
kubectl proxy --port=8080
```

## Expected Output

Logs: "Starting to serve on 127.0.0.1:8001"; runs until Ctrl+C.

## Related

- [[commands/curl-scale-up-deployment]]
- [[procedures/start-kubectl-proxy]]
