---
type: command
executor: bash
data: python3 -m http.server 8000
output: 'Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - http
  - hosting
verified: true
validated: true
---

# Python-HTTP-Server-for-File-Hosting

## Command

```bash
python3 -m http.server 8000
```

## Description

Starts a simple HTTP server to host files for download by targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m http.server | Module to run | Yes |
| 8000 | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
python3 -m http.server 80
```

Port 80.

### Advanced Usage

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Bind to localhost.

## Expected Output

Server ready message; access via browser.

## Related

- [[procedures/Map-Active-Directory-with-SharpHound]]
