---
data: >-
  docker pull TARGET_IP/NAMESPACE/REPO:3.0.1 && docker run --rm -it
  TARGET_IP/NAMESPACE/REPO:3.0.1
tags:
  - docker
  - pull
  - run
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.907Z'
id: b3522028-8d67-4886-b1a3-b1db6d86a589
verified: false
validated: true
submitted: true
---
# docker-pull-run

## Command

```bash
docker pull TARGET_IP/NAMESPACE/REPO:3.0.1 && docker run --rm -it TARGET_IP/NAMESPACE/REPO:3.0.1
```

## Description

Pulls a Docker image from an unauthenticated registry and runs it interactively.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| TARGET_IP/NAMESPACE/REPO:3.0.1 | Image reference | Yes |
| --rm -it | Remove after exit, interactive | No |

## Examples

### Basic Usage

```bash
docker pull example.com/repo:latest
```

### Advanced Usage

```bash
docker run --rm -it example.com/repo:tag /bin/sh
```

## Expected Output

Image pulled, container starts with shell access.

## Related

- [[Related Procedure: Pull-Full-Docker-Image-with-CLI]]
