---
data: kubectl apply -f webshell_ingress.yaml
tags:
  - kubernetes
  - webshell
type: command
output: Ingress update confirmation
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.874Z'
id: 094eff00-370d-4e47-97d8-f2b761cb6c59
verified: false
validated: true
submitted: true
---
# kubectl-apply-webshell-ingress-yaml

## Command

```bash
kubectl apply -f webshell_ingress.yaml
```

## Description

Deploys or updates an Ingress YAML to include a Lua webshell file in NGINX config.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Path to the webshell Ingress YAML | Yes |

## Examples

### Basic Usage

```bash
kubectl apply -f webshell_ingress.yaml
```

## Expected Output

"ingress.networking.k8s.io/webshell configured".

## Related

- [[procedures/Create-Webshell-Ingress-for-RCE]]
