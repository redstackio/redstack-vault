---
data: >-
  kubectl apply -f
  https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
tags:
  - kubernetes
  - ingress
type: command
output: Deployment status messages
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.890Z'
id: 037e6184-0547-4076-b826-6dadb586b280
verified: false
validated: true
submitted: true
---
# kubectl-apply-ingress-deployment

## Command

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

## Description

Applies the official NGINX Ingress Controller deployment YAML for Kind clusters, creating necessary resources like namespace, RBAC, and pods.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | URL or path to the YAML manifest | Yes |

## Examples

### Basic Usage

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

### Advanced Usage

```bash
kubectl apply -f local-deploy.yaml --namespace=ingress-nginx
```

## Expected Output

Messages like "namespace/ingress-nginx unchanged", "deployment.apps/ingress-nginx-controller created".

## Related

- [[procedures/Deploy-NGINX-Ingress-Controller]]
