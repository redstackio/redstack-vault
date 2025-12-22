---
type: command
executor: bash
data: >-
  curl -XPOST --unix-socket /var/run/docker.sock -d '{"Image":"$_IMAGE"}' -H
  'Content-Type: application/json' http://localhost/containers/create
output: null
created_at: '2023-04-06T03:56:16.917057+00:00'
updated_at: '2023-04-10T20:33:49.704451+00:00'
platforms:
  - Linux
tags:
  - docker
  - exploitation
verified: true
validated: true
---

# create-nginx-container-via-socket

## Command

```bash
curl -XPOST --unix-socket /var/run/docker.sock -d '{"Image":"$_IMAGE"}' -H 'Content-Type: application/json' http://localhost/containers/create
```

## Description

Creates a new Docker container using the API via the socket, demonstrating control to instantiate malicious or test containers on the host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --unix-socket /var/run/docker.sock | Unix socket for daemon connection | Yes |
| -d '{"Image":"$_IMAGE"}' | JSON payload with image name | Yes |
| -H 'Content-Type: application/json' | Set request header | Yes |
| $_IMAGE | Docker image to use (default: nginx) | Yes |

## Examples

### Basic Usage

```bash
curl -XPOST --unix-socket /var/run/docker.sock -d '{"Image":"nginx"}' -H 'Content-Type: application/json' http://localhost/containers/create
```

### Custom Image

```bash
curl -XPOST --unix-socket /var/run/docker.sock -d '{"Image":"ubuntu"}' -H 'Content-Type: application/json' http://localhost/containers/create
```

## Expected Output

{"Id":"def456...","Warnings":null}

Id is the new container's identifier; use in subsequent starts.

## Related

- [[procedures/Escape-Container-Using-Mounted-Docker-Socket]]
