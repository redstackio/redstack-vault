---
type: command
executor: bash
data: 'curl --unix-socket /var/run/docker.sock http://127.0.0.1/containers/json'
output: null
created_at: '2023-04-06T03:56:16.917000+00:00'
updated_at: '2023-04-10T20:33:49.704451+00:00'
platforms:
  - Linux
tags:
  - docker
  - recon
verified: true
validated: true
---

# list-docker-containers-via-socket

## Command

```bash
curl --unix-socket /var/run/docker.sock http://127.0.0.1/containers/json
```

## Description

Queries the Docker daemon via the Unix socket to list all containers, testing socket access and providing reconnaissance on the host's container inventory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --unix-socket /var/run/docker.sock | Use Unix socket for communication | Yes |
| http://127.0.0.1/containers/json | API endpoint for container list | Yes |

## Examples

### Basic Usage

```bash
curl --unix-socket /var/run/docker.sock http://127.0.0.1/containers/json
```

### Pretty Print JSON

```bash
curl --unix-socket /var/run/docker.sock http://127.0.0.1/containers/json | jq .
```

## Expected Output

[{"Id":"abc123...","Names":["/container1"],"Image":"ubuntu","State":"running"},...]

Empty array [] if no containers; error like {"message":"Got permission denied while trying to connect to the Docker daemon socket"} if access denied.

## Related

- [[procedures/Escape-Container-Using-Mounted-Docker-Socket]]
