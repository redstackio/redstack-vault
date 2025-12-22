---
id: 55980d43-b648-46b5-a692-aa180881f24e
name: docker-run-bash-with-docker-socket-mount
type: command
executor: bash
data: 'docker run -ti -v /var/run/docker.sock:/var/run/docker.sock bash'
output: null
created_at: '2023-04-06T03:56:38.757020+00:00'
updated_at: '2023-04-10T20:24:05.013008+00:00'
platforms:
  - Linux
tags:
  - docker
  - container
  - ssrf
verified: true
validated: true
---

# docker-run-bash-with-docker-socket-mount

## Command

```bash
docker run -ti -v /var/run/docker.sock:/var/run/docker.sock bash
```

## Description

This command launches a temporary Bash container that mounts the host's Docker socket, allowing the container to interact with the host's Docker daemon as if it were local. Use this to test Docker API access in a controlled environment before crafting SSRF payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ti` | Allocate a pseudo-TTY and keep STDIN open for interactive shell | Yes |
| `-v /var/run/docker.sock:/var/run/docker.sock` | Mount the host Docker socket into the container for API access | Yes |
| `bash` | The image to run (uses a minimal bash image; assumes docker pull bash if needed) | Yes |

## Examples

### Basic Usage

```bash
docker run -ti -v /var/run/docker.sock:/var/run/docker.sock bash
```

Drops into an interactive Bash shell inside the container with Docker control.

### Advanced Usage

```bash
docker run -ti --rm -v /var/run/docker.sock:/var/run/docker.sock alpine sh
```

Uses Alpine for a lighter image and auto-removes the container (--rm).

## Expected Output

```
root@container-id:/# 
```

An interactive shell prompt inside the container. From here, you can run curl commands against the Docker API via the mounted socket. Success is indicated by the shell opening without errors; failure shows permission denied or socket not found.

## Related

- [[procedures/SSRF-to-Enumerate-Docker-Containers-and-Images]]
