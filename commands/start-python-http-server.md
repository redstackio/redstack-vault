---
id: cmd-python-http-server-001
data: python3 -m http.server 4444
tags:
  - listener
  - http-server
type: command
output: |-
  Serving HTTP on 0.0.0.0 port 4444 (http://0.0.0.0:4444/) ...
  127.0.0.1 - - [timestamp] "GET / HTTP/1.1" 200 -
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.101Z'
verified: false
validated: true
submitted: true
---
# start-python-http-server

## Command

```bash
python3 -m http.server 4444
```

## Description

Starts a basic HTTP server using Python's http.server module on the specified port (4444), useful for SSRF POCs to log incoming requests from vulnerable applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m http.server` | Module to run the HTTP server | Yes |
| `4444` | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
python3 -m http.server 4444
```

### Advanced Usage

```bash
python3 -m http.server 4444 --bind 0.0.0.0
```

## Expected Output

Server startup message followed by request logs, e.g., IP, timestamp, method, path, status code. For SSRF, expect external IP hits on /info/refs paths.

## Related

- [[Related Procedure|procedures/Setup-HTTP-Listener-for-SSRF-POC]]
