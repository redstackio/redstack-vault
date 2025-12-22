---
id: 270a4901-6a9f-4477-9534-18b2a484ef00
name: check-docker-overlay-mount
type: command
executor: bash
data: mount | head -n 1
output: null
created_at: '2023-04-06T03:56:17.157140+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - docker
  - recon
  - filesystem
verified: true
validated: true
---

# check-docker-overlay-mount

## Command

```bash
mount | head -n 1
```

## Description

This command checks the root filesystem mount in a Docker container to identify if it's using the overlay2 driver and reveals the writable upperdir path, which is crucial for directing core dumps in privilege escalation attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `mount` | Displays mounted filesystems | Built-in |
| `head -n 1` | Limits output to the first line (root mount) | Built-in |

## Examples

### Basic Usage

```bash
mount | head -n 1
```

### In a Script

```bash
MOUNT_INFO=$(mount | head -n 1)
echo $MOUNT_INFO | grep upperdir
```

## Expected Output

```
overlay on / type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/<layer1>:/var/lib/docker/overlay2/l/<layer2>,upperdir=/var/lib/docker/overlay2/<container-hash>/diff,workdir=/var/lib/docker/overlay2/<container-hash>/work)
```

Parse the 'upperdir=' value to get the writable path for core dump redirection.

## Related

- [[procedures/Abuse-Core-Dumps-and-Core-Pattern-for-Privilege-Escalation-in-Docker]]
- [[commands/set-core-pattern-pipe]]
