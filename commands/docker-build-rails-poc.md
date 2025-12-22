---
id: cmd-docker-build
data: 'docker build -t local/railspoc:latest .'
tags:
  - build
  - docker
type: command
output: Build output indicating success
executor: bash
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.739Z'
verified: false
validated: true
submitted: true
---
# docker-build-rails-poc

## Command

```bash
docker build -t local/railspoc:latest .
```

## Description

Builds a Docker image for the vulnerable Rails PoC app from the current directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t | Tag for image: local/railspoc:latest | Yes |
| . | Build context (current dir) | Yes |

## Examples

### Basic Usage

```bash
docker build -t local/railspoc:latest .
```

### Advanced Usage

Add --no-cache for fresh build.

## Expected Output

Successfully tagged local/railspoc:latest

## Related

- [[commands/docker-run-rails-poc]]
- [[procedures/Build-Sample-Vulnerable-Rails-Application-with-Docker]]
