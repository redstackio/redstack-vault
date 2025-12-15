---
data: python3 -m http.server 8000 --bind 0.0.0.0
tags:
  - hosting
  - web-server
  - payload-delivery
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
id: 2e11233c-f3d1-42c3-9364-e7d253f1b7d2
created_at: '2025-12-14T17:24:44.887Z'
updated_at: '2025-12-14T17:24:44.887Z'
verified: false
validated: true
submitted: true
---
# python-http-server-host-payload

## Command

```bash
python3 -m http.server 8000 --bind 0.0.0.0
```

## Description

This command starts a simple HTTP server using Python 3 to host files, ideal for serving malicious payloads like disguised HTML files in penetration testing. It binds to all interfaces and uses port 8000 by default, serving files with appropriate MIME types (octet-stream for unknown extensions).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `python3` | Python 3 interpreter | Yes |
| `-m http.server` | Module to run the HTTP server | Yes |
| `8000` | Port to listen on | No (default 8000) |
| `--bind 0.0.0.0` | Bind to all network interfaces | No (default localhost) |

## Examples

### Basic Usage

```bash
python3 -m http.server 8000
```

Starts server on localhost:8000 for local testing.

### Advanced Usage

```bash
python3 -m http.server 8080 --bind 0.0.0.0 --directory /path/to/payloads
```

Serves from a specific directory on port 8080, accessible externally.

## Expected Output

Server logs incoming requests, e.g.:
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 - - [01/Oct/2023 12:00:00] "GET /payload.bin HTTP/1.1" 200 -
```
Successful run shows the server ready and logs file accesses without errors.

## Related

- [[Related Procedure|procedures/Exploit-LINE-iOS-WebView-XSS-via-Octet-Stream]]
