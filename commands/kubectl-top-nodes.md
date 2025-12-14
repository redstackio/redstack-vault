---
id: cmd-kubectl-top-nodes
data: kubectl top nodes
tags:
  - kubernetes
  - monitoring
type: command
output: Node CPU/Memory usage table
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.528Z'
verified: false
validated: true
submitted: true
---
# kubectl top nodes

## Command

```bash
kubectl top nodes
```

## Description

Displays CPU and memory usage for cluster nodes, requiring metrics-server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| none | All nodes | No |

## Examples

### Basic Usage

```bash
kubectl top nodes
```

### Advanced Usage

```bash
kubectl top nodes --sort-by=cpu
```

## Expected Output

Table with NAME, CPU(cores), CPU%, MEMORY(bytes), MEMORY%; high % on masters.

## Related

- [[commands/kubectl-get-pods-watch]]
- [[procedures/observe-kubernetes-resource-exhaustion]]
