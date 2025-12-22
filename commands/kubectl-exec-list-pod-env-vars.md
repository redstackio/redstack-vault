---
id: new-uuid-1
name: kubectl-exec-list-pod-env-vars
type: command
executor: bash
data: kubectl exec $_POD_NAME -- env
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Kubernetes
tags:
  - enumeration
  - kubernetes
verified: true
validated: true
---

# kubectl-exec-list-pod-env-vars

## Command

```bash
kubectl exec $_POD_NAME -- env
```

## Description

Executes the `env` command inside a Kubernetes pod to list all environment variables visible to the container. Useful for discovering configuration details, service endpoints, or leaked secrets during reconnaissance in a cluster.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_POD_NAME | Name of the target pod | Yes |
| --env | Built-in flag to run the env command | Built-in |

## Examples

### Basic Usage

```bash
kubectl exec redis-master -- env
```

### With Container Specification

```bash
kubectl exec redis-master -c redis-container -- env
```

## Expected Output

A list of environment variables in KEY=VALUE format:
```
HOME=/root
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
REDIS_MASTER_SERVICE_HOST=10.0.0.11
REDIS_MASTER_SERVICE_PORT=6379
```

## Related

- [[procedures/Enumerate-Kubernetes-Container-Environment-Variables]]
- [[commands/Extract-Kubernetes-Env-Redis-Master-Service-Host]]
