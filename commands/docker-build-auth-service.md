---
id: cmd-uuid-3
data: 'cd auth-service; docker build -t auth-service:0.0.4 .'
tags:
  - docker
  - build
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.469Z'
verified: false
validated: true
submitted: true
---
# docker-build-auth-service

## Command

```bash
cd auth-service; docker build -t auth-service:0.0.4 .
```

## Description

Builds the Docker image for the authentication service from its Dockerfile.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t` | Image tag | Yes |
| `.` | Build context | Yes |

## Examples

### Basic Usage

```bash
docker build -t auth-service:0.0.4 .
```

## Expected Output

Successfully tagged auth-service:0.0.4

## Related

- [[commands/minikube-load-auth-image]]
