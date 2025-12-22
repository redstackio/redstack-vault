---
id: d8803945-e706-4f3d-9f70-7fee1657902b
name: Extract-Kubernetes-Env-Redis-Master-Service-Port
type: command
executor: bash
data: kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_SERVICE_PORT
output: REDIS_MASTER_SERVICE_PORT=6379
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

# Extract-Kubernetes-Env-Redis-Master-Service-Port

## Command

```bash
kubectl exec $_POD_NAME -- env | grep REDIS_MASTER_SERVICE_PORT
```

## Description

Pulls the port number for the Redis master service from the pod's environment variables, aiding in targeting internal Redis instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_POD_NAME | Name of the target pod | Yes |
| grep REDIS_MASTER_SERVICE_PORT | Filter for the port var | Built-in |

## Examples

### Basic Usage

```bash
kubectl exec redis-master -- env | grep REDIS_MASTER_SERVICE_PORT
```

## Expected Output

```
REDIS_MASTER_SERVICE_PORT=6379
```

## Related

- [[procedures/Enumerate-Kubernetes-Container-Environment-Variables]]
- [[commands/Extract-Kubernetes-Env-Redis-Master-Port]]
