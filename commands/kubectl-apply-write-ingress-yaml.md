---
data: kubectl apply -f write_ingress.yaml
tags:
  - kubernetes
  - injection
type: command
output: Ingress creation confirmation
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.885Z'
id: b8803931-b7d3-49aa-84cc-688d240fa58a
verified: false
validated: true
submitted: true
---
# kubectl-apply-write-ingress-yaml

## Command

```bash
kubectl apply -f write_ingress.yaml
```

## Description

Deploys a malicious Ingress YAML file to inject NGINX config for file writing via access_log.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Path to the Ingress YAML file | Yes |

## Examples

### Basic Usage

```bash
kubectl apply -f write_ingress.yaml
```

### Advanced Usage

```bash
kubectl apply -f write_ingress.yaml --dry-run=client -o yaml
```

## Expected Output

"ingress.networking.k8s.io/malicious-write created".

## Related

- [[procedures/Create-Malicious-Ingress-for-File-Write]]
