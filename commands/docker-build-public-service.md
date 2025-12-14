---
id: cmd-uuid-5
data: 'cd public-service; docker build -t public-service:0.0.1 .'
tags:
  - docker
  - build
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.462Z'
verified: false
validated: true
submitted: true
---
# docker-build-public-service

## Command

```bash
cd public-service; docker build -t public-service:0.0.1 .
```

## Description

Builds the Docker image for the public service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t` | Image tag | Yes |

## Examples

### Basic Usage

```bash
docker build -t public-service:0.0.1 .
```

## Expected Output

Successfully tagged public-service:0.0.1
