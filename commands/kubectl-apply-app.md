---
id: cmd-uuid-9
data: kubectl apply -f app.yaml
tags:
  - kubectl
  - deployment
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.437Z'
verified: false
validated: true
submitted: true
---
# kubectl-apply-app

## Command

```bash
kubectl apply -f app.yaml
```

## Description

Applies the Kubernetes manifest to deploy services, deployments, and ingress.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Manifest file | Yes |

## Examples

### Basic Usage

```bash
kubectl apply -f app.yaml
```

## Expected Output

deployment.apps/auth-service created

## Related

- [[commands/docker-build-auth-service]]
