---
id: cmd-uuid-7
data: 'minikube image load protected-service:0.0.1'
tags:
  - minikube
  - docker
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.444Z'
verified: false
validated: true
submitted: true
---
# minikube-load-protected-image

## Command

```bash
minikube image load protected-service:0.0.1
```

## Description

Loads the protected-service image into Minikube.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `image` | Image name | Yes |

## Examples

### Basic Usage

```bash
minikube image load protected-service:0.0.1
```

## Expected Output

Image loaded.
