---
id: cmd-kubectl-proxy-001
data: kubectl proxy &
tags:
  - proxy
  - debug
type: command
output: 'Starting to serve on 127.0.0.1:8001'
executor: bash
platforms:
  - Kubernetes
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.683Z'
verified: false
validated: true
submitted: true
---
# start-kubectl-proxy

## Command

```bash
kubectl proxy &
```

## Description

Starts kubectl proxy server in background on localhost:8001 for API access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `&` | Background execution | Yes |

## Examples

### Basic Usage

```bash
kubectl proxy &
```

### Advanced Usage

```bash
kubectl proxy --port=8001 --address=0.0.0.0 &
```

## Expected Output

Proxy serve message.

## Related

- [[commands/set-klog-verbosity]]
- [[procedures/Enable-Kubectl-Proxy-and-Debug-Flags]]
