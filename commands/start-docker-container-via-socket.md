---
type: command
executor: bash
data: >-
  curl -XPOST --unix-socket /var/run/docker.sock
  http://localhost/containers/$_CONTAINER_ID/start
output: null
created_at: '2023-04-06T03:56:16.917105+00:00'
updated_at: '2023-04-10T20:33:49.704451+00:00'
platforms:
  - Linux
tags:
  - docker
  - exploitation
verified: true
validated: true
---

# start-docker-container-via-socket

## Command

```bash
curl -XPOST --unix-socket /var/run/docker.sock http://localhost/containers/$_CONTAINER_ID/start
```

## Description

Starts a stopped Docker container via the API, confirming the ability to execute and manage host resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --unix-socket /var/run/docker.sock | Unix socket path | Yes |
| $_CONTAINER_ID | ID of the container to start | Yes |
| http://localhost/containers/$_CONTAINER_ID/start | API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -XPOST --unix-socket /var/run/docker.sock http://localhost/containers/def456/start
```

## Expected Output

204 No Content or empty body on success. Errors: 404 {"message":"No such container"} if ID invalid.

## Related

- [[procedures/Escape-Container-Using-Mounted-Docker-Socket]]
