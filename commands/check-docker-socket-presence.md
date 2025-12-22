---
type: command
executor: bash
data: ls -la /var/run/docker.sock
output: null
created_at: '2023-04-06T03:56:16.916881+00:00'
updated_at: '2023-04-10T20:33:49.704451+00:00'
platforms:
  - Linux
tags:
  - docker
  - recon
verified: true
validated: true
---

# check-docker-socket-presence

## Command

```bash
ls -la /var/run/docker.sock
```

## Description

This command checks if the Docker Unix socket is present and mounted in the container's filesystem, verifying the initial condition for exploitation. Use it early to confirm the misconfiguration without API interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /var/run/docker.sock | Path to the Docker socket file | Yes |

## Examples

### Basic Usage

```bash
ls -la /var/run/docker.sock
```

### With Custom Path

```bash
ls -la $_SOCKET_PATH
```

## Expected Output

srw-rw---- 1 root docker 0 Oct 10 12:00 /var/run/docker.sock

If the file does not exist, output will be ls: cannot access '/var/run/docker.sock': No such file or directory.

## Related

- [[procedures/Escape-Container-Using-Mounted-Docker-Socket]]
