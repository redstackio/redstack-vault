---
id: 06c13e7b-0c45-4a73-8093-4e1a550007c1
name: curl-list-docker-containers-via-tcp-socket
type: command
executor: bash
data: 'curl http://127.0.0.1:2375/v1.24/containers/json'
output: null
created_at: '2023-04-06T03:56:38.756960+00:00'
updated_at: '2023-04-10T20:24:05.013008+00:00'
platforms:
  - Linux
tags:
  - docker
  - curl
  - ssrf
  - enumeration
verified: true
validated: true
---

# curl-list-docker-containers-via-tcp-socket

## Command

```bash
curl http://127.0.0.1:2375/v1.24/containers/json
```

## Description

This command queries the Docker API over TCP on localhost port 2375 to enumerate all containers. It's used to verify API accessibility and serves as the basis for SSRF payloads targeting internal TCP-exposed Docker daemons.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://127.0.0.1:2375` | Target the local Docker API TCP endpoint | Yes |
| `/v1.24/containers/json` | API path to list containers (v1.24 is a common version) | Yes |
| `?all=true` (optional) | Include stopped containers | No |

## Examples

### Basic Usage

```bash
curl http://127.0.0.1:2375/v1.24/containers/json
```

Lists running containers by default.

### Advanced Usage

```bash
curl -s http://127.0.0.1:2375/v1.24/containers/json?all=true&size=true
```

Includes all containers with size information.

## Expected Output

```json
[
  {
    "Id": "sha256:def456...",
    "Names": ["/app-container"],
    "Image": "nginx",
    "State": "exited",
    "Status": "Exited (0) 10 minutes ago"
  }
]
```

JSON array detailing containers. Success: Valid JSON response; failure: Connection refused or empty array.

## Related

- [[procedures/SSRF-to-Enumerate-Docker-Containers-and-Images]]
