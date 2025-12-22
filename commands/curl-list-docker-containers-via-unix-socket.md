---
id: bd2b82a4-c341-4bb2-b02a-91a67cdb1457
name: curl-list-docker-containers-via-unix-socket
type: command
executor: bash
data: 'curl --unix-socket /var/run/docker.sock http://foo/containers/json'
output: null
created_at: '2023-04-06T03:56:38.757122+00:00'
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

# curl-list-docker-containers-via-unix-socket

## Command

```bash
curl --unix-socket /var/run/docker.sock http://foo/containers/json
```

## Description

This command uses curl to query the Docker API via the Unix socket to list all containers (running and stopped). The 'http://foo' is a placeholder to satisfy curl's URL requirement when using Unix sockets. In SSRF contexts, this endpoint path is used as the payload URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--unix-socket /var/run/docker.sock` | Connect to the Docker daemon via Unix socket instead of TCP | Yes |
| `http://foo/containers/json` | API endpoint path for listing containers (foo is dummy host) | Yes |
| `-s` (optional) | Silent mode to suppress progress meter | No |

## Examples

### Basic Usage

```bash
curl --unix-socket /var/run/docker.sock http://foo/containers/json
```

Retrieves the full list of containers.

### Advanced Usage

```bash
curl --unix-socket /var/run/docker.sock -s http://foo/containers/json?all=true
```

Adds ?all=true to include stopped containers explicitly.

## Expected Output

```json
[
  {
    "Id": "sha256:abc123...",
    "Names": ["/container1"],
    "Image": "ubuntu",
    "State": "running",
    "Status": "Up 5 minutes"
  }
]
```

A JSON array of container objects. Success is a non-empty array; empty means no containers or access denied.

## Related

- [[procedures/SSRF-to-Enumerate-Docker-Containers-and-Images]]
