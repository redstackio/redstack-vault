---
id: cmd-uuid-2
data: |-
  minikube addons enable ingress
  minikube addons enable ingress-dns
tags:
  - setup
  - ingress
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.473Z'
verified: false
validated: true
submitted: true
---
# enable-minikube-addons

## Command

```bash
minikube addons enable ingress
minikube addons enable ingress-dns
```

## Description

Enables NGINX Ingress controller and DNS addons in Minikube for local routing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `enable` | Activates the addon | Yes |

## Examples

### Basic Usage

```bash
minikube addons enable ingress
```

## Expected Output

Addon 'ingress' enabled.

## Related

- [[commands/install-minikube]]
