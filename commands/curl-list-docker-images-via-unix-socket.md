---
id: 37c841a4-e61f-4ea8-99c5-c92674c694cc
name: curl-list-docker-images-via-unix-socket
type: command
executor: bash
data: 'curl --unix-socket /var/run/docker.sock http://foo/images/json'
output: null
created_at: '2023-04-06T03:56:38.757151+00:00'
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

# curl-list-docker-images-via-unix-socket

## Command

```bash
curl --unix-socket /var/run/docker.sock http://foo/images/json
```

## Description

Queries the Docker API via Unix socket to list all local images. The dummy host 'foo' is required for curl's URL parsing. This endpoint is key for SSRF payloads to discover image inventories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--unix-socket /var/run/docker.sock` | Use Unix socket for Docker API connection | Yes |
| `http://foo/images/json` | Endpoint path for images list | Yes |
| `?all=false` (optional) | Show only top-level images (default); true for intermediates | No |

## Examples

### Basic Usage

```bash
curl --unix-socket /var/run/docker.sock http://foo/images/json
```

Lists all images.

### Advanced Usage

```bash
curl --unix-socket /var/run/docker.sock -s http://foo/images/json?all=true
```

Includes intermediate layers.

## Expected Output

```json
[
  {
    "Id": "sha256:ghi789...",
    "RepoTags": ["ubuntu:latest", "ubuntu:20.04"],
    "Size": 123456789,
    "VirtualSize": 123456789
  }
]
```

JSON array of image objects. Success: Populated array; indicates accessible API.

## Related

- [[procedures/SSRF-to-Enumerate-Docker-Containers-and-Images]]
