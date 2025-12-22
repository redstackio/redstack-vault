---
type: command
executor: bash
data: 'export DOCKER_HOST=tcp://$_TARGET_IP:2376'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - docker
  - configuration
verified: true
validated: true
---

# set-docker-host-tcp

## Command

```bash
export DOCKER_HOST=tcp://$_TARGET_IP:2376
```

## Description

Sets the DOCKER_HOST environment variable to point to a remote unauthenticated Docker daemon over TCP, enabling subsequent Docker CLI commands to target the remote host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the Docker host | Yes |
| tcp://... | Protocol and port (2376 for unencrypted) | Built-in |

## Examples

### Basic Usage

```bash
export DOCKER_HOST=tcp://10.10.10.10:2376
```

### Advanced Usage

```bash
export DOCKER_HOST=tcp://10.10.10.10:2375  # For TLS
```

## Expected Output

No output; verifies with `echo $DOCKER_HOST` showing the set value.

## Related

- [[procedures/Exploit-Open-Docker-API-for-Container-Management]]
- [[tools/Docker]]
