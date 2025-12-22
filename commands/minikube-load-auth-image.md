---
id: cmd-uuid-6
data: 'minikube image load auth-service:0.0.4'
tags:
  - minikube
  - docker
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.457Z'
verified: false
validated: true
submitted: true
---
# minikube-load-auth-image

## Command

```bash
minikube image load auth-service:0.0.4
```

## Description

Loads the built auth-service image into Minikube's Docker daemon.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `image` | Image name and tag | Yes |

## Examples

### Basic Usage

```bash
minikube image load auth-service:0.0.4
```

## Expected Output

Image loaded successfully to Minikube.
