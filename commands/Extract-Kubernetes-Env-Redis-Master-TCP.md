---
id: 0ea0a176-92e0-4086-b378-8c18ef6d381c
name: Extract-Kubernetes-Env-Redis-Master-TCP
type: command
executor: bash
data: kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_PORT_6379_TCP
output: 'REDIS_MASTER_PORT_6379_TCP=tcp://10.0.0.11:6379'
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
tags:
  - extraction
  - kubernetes
  - redis
verified: true
validated: true
---

# Extract-Kubernetes-Env-Redis-Master-TCP

## Command

```bash
kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_PORT_6379_TCP
```

## Description

Extracts TCP-specific details for the Redis master port (e.g., protocol, addr, port) from the pod env, useful for reconstructing service connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_POD_NAME | Name of the target pod | Yes |
| grep REDIS_MASTER_PORT_6379_TCP | Filter for TCP var | Built-in |

## Examples

### Basic Usage

```bash
kubectl exec redis-master -- env | grep REDIS_MASTER_PORT_6379_TCP
```

## Expected Output

```
REDIS_MASTER_PORT_6379_TCP=tcp://10.0.0.11:6379
```

## Related

- [[procedures/Enumerate-Kubernetes-Container-Environment-Variables]]
- [[commands/Extract-Kubernetes-Env-Redis-Master-Service-Host]]
