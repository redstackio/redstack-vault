---
type: command
executor: bash
data: docker -H $_DOCKER_HOST exec -it $_CONTAINER_NAME /bin/bash
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - docker
  - execution
verified: true
validated: true
---

# docker-exec-interactive-bash

## Command

```bash
docker -H $_DOCKER_HOST exec -it $_CONTAINER_NAME /bin/bash
```

## Description

Executes an interactive bash shell inside a running container on a remote Docker host, allowing command execution within the container's context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H $_DOCKER_HOST | Remote host (e.g., tcp://ip:2376) | Yes |
| exec | Execute command in container | Built-in |
| -it | Interactive with TTY | Yes |
| $_CONTAINER_NAME | Name or ID of target container | Yes |
| /bin/bash | Shell to spawn | Yes |

## Examples

### Basic Usage

```bash
docker -H tcp://10.10.10.10:2376 exec -it mysql /bin/bash
```

### Advanced Usage

```bash
docker exec -it web sh  # If local or env set
```

## Expected Output

Interactive shell: `root@mysql:/#`

## Related

- [[procedures/Exploit-Open-Docker-API-for-Container-Management]]
- [[tools/Docker]]
