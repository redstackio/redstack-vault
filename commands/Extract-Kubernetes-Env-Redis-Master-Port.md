---
id: 9aba0dcb-ed50-49df-ae05-8fbf28a6eb76
name: Extract-Kubernetes-Env-Redis-Master-Port
type: command
executor: bash
data: kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_PORT
output: 'REDIS_MASTER_PORT=tcp://10.0.0.11:6379'
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

# Extract-Kubernetes-Env-Redis-Master-Port

## Command

```bash
kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_PORT
```

## Description

Retrieves the full URI for the Redis master port from the container's env vars, providing a complete endpoint for connection attempts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_POD_NAME | Name of the target pod | Yes |
| grep REDIS_MASTER_PORT | Filter for the port URI var | Built-in |

## Examples

### Basic Usage

```bash
kubectl exec redis-master -- env | grep REDIS_MASTER_PORT
```

## Expected Output

```
REDIS_MASTER_PORT=tcp://10.0.0.11:6379
```

## Related

- [[procedures/Enumerate-Kubernetes-Container-Environment-Variables]]
- [[commands/Extract-Kubernetes-Env-Redis-Master-TCP]]
