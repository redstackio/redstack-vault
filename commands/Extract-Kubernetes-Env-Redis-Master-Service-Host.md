---
id: 9acb031c-4502-45e2-88d5-c952e3617256
name: Extract-Kubernetes-Env-Redis-Master-Service-Host
type: command
executor: bash
data: kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_SERVICE_HOST
output: REDIS_MASTER_SERVICE_HOST=10.0.0.11
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

# Extract-Kubernetes-Env-Redis-Master-Service-Host

## Command

```bash
kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_SERVICE_HOST
```

## Description

Extracts the REDIS_MASTER_SERVICE_HOST environment variable from a Kubernetes pod, revealing the internal IP of the Redis master service for potential lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_POD_NAME | Name of the target pod | Yes |
| grep REDIS_MASTER_SERVICE_HOST | Filter for the specific env var | Built-in |

## Examples

### Basic Usage

```bash
kubectl exec redis-master -- env | grep REDIS_MASTER_SERVICE_HOST
```

## Expected Output

```
REDIS_MASTER_SERVICE_HOST=10.0.0.11
```

## Related

- [[procedures/Enumerate-Kubernetes-Container-Environment-Variables]]
- [[commands/Extract-Kubernetes-Env-Redis-Master-Service-Port]]
