---
type: command
executor: bash
data: docker -H $_DOCKER_HOST ps
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - docker
  - enumeration
verified: true
validated: true
---

# docker-list-remote-containers

## Command

```bash
docker -H $_DOCKER_HOST ps
```

## Description

Lists running containers on a remote Docker host, showing IDs, images, commands, status, and ports for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H $_DOCKER_HOST | Remote host specification (e.g., tcp://ip:2376) | Yes |
| ps | List processes (containers) | Built-in |

## Examples

### Basic Usage

```bash
docker -H tcp://10.10.10.10:2376 ps
```

### Advanced Usage

```bash
docker -H tcp://10.10.10.10:2376 ps -a  # All containers
```

## Expected Output

```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
abc123def456   nginx     "nginx"   5 min     Up 5 min  80/tcp    web
```

## Related

- [[procedures/Exploit-Open-Docker-API-for-Container-Management]]
- [[tools/Docker]]
