---
id: cmd-uuid-4
data: 'cd protected-service; docker build -t protected-service:0.0.1 .'
tags:
  - docker
  - build
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.465Z'
verified: false
validated: true
submitted: true
---
# docker-build-protected-service

## Command

```bash
cd protected-service; docker build -t protected-service:0.0.1 .
```

## Description

Builds the Docker image for the protected service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t` | Image tag | Yes |

## Examples

### Basic Usage

```bash
docker build -t protected-service:0.0.1 .
```

## Expected Output

Successfully tagged protected-service:0.0.1
