---
id: cmd-kubectl-apply
data: kubectl apply -f large-nginx-deployment.yaml
tags:
  - kubernetes
  - deployment
type: command
output: deployment.apps/nginx created
executor: bash
platforms:
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.552Z'
verified: false
validated: true
submitted: true
---
# kubectl apply -f large-nginx-deployment.yaml

## Command

```bash
kubectl apply -f large-nginx-deployment.yaml
```

## Description

Applies a Kubernetes deployment YAML file to the cluster, creating or updating the 'nginx' deployment with large env vars.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f | Path to YAML file | Yes |
| large-nginx-deployment.yaml | File containing oversized deployment spec | Yes |

## Examples

### Basic Usage

```bash
kubectl apply -f deployment.yaml
```

### Advanced Usage

```bash
kubectl apply -f large-nginx-deployment.yaml --namespace=default
```

## Expected Output

"deployment.apps/nginx created" or updated status; initial processing may take seconds due to size.

## Related

- [[commands/kubectl-proxy-start]]
- [[procedures/create-large-kubernetes-deployment-with-env-vars]]
