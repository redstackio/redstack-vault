---
id: e4701e2f-f540-4eec-8e90-990857055327
name: start-privileged-ubuntu-container
type: command
executor: bash
data: >-
  docker run --rm -it --cap-add=SYS_ADMIN --security-opt apparmor=unconfined
  ubuntu bash
output: null
created_at: '2023-04-06T03:56:17.110150+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - docker
  - container
verified: true
validated: true
---

# start-privileged-ubuntu-container

## Command

```bash
docker run --rm -it --cap-add=SYS_ADMIN --security-opt apparmor=unconfined ubuntu bash
```

## Description

Starts an interactive Ubuntu container with elevated SYS_ADMIN Linux capability and disabled AppArmor confinement, providing a shell for cgroup manipulation in privilege escalation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --rm | Remove container on exit | No |
| -it | Interactive mode with TTY | Yes |
| --cap-add=SYS_ADMIN | Add SYS_ADMIN capability for filesystem mounts | Yes |
| --security-opt apparmor=unconfined | Disable AppArmor profiles | Yes |
| ubuntu | Base image to use | Yes |
| bash | Entry command for shell | Yes |

## Examples

### Basic Usage

```bash
docker run --rm -it --cap-add=SYS_ADMIN --security-opt apparmor=unconfined ubuntu bash
```

### With Custom Image

```bash
docker run --rm -it --cap-add=SYS_ADMIN --security-opt apparmor=unconfined myimage bash
```

## Expected Output

root@container-id:/# (Interactive bash prompt inside the container, confirming successful spawn with privileges.)

## Related

- [[procedures/Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation]]
