---
id: cmd-uuid-1
data: |-
  # Platform-specific; example for Windows via Chocolatey
  choco install minikube
  minikube start --kubernetes-version=v1.22.2
tags:
  - setup
  - kubernetes
type: command
output: null
executor: bash
platforms:
  - Windows
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.476Z'
verified: false
validated: true
submitted: true
---
# install-minikube

## Command

```bash
# Platform-specific; example for Windows via Chocolatey
choco install minikube
minikube start --kubernetes-version=v1.22.2
```

## Description

Installs and starts Minikube v1.23.2 with Kubernetes v1.22.2 for local cluster simulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--kubernetes-version` | Specifies K8s version | No |

## Examples

### Basic Usage

```bash
minikube start
```

### Advanced Usage

```bash
minikube start --driver=docker --kubernetes-version=v1.22.2
```

## Expected Output

Minikube cluster is starting... Done! kubectl is now configured...

## Related

- [[commands/enable-minikube-addons]]
