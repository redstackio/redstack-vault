---
id: cmd-uuid-listener
data: python3 -m http.server 80
tags:
  - listener
  - ssrf
  - oob
type: command
output: 'Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.080Z'
verified: false
validated: true
submitted: true
---
# setup-listener

## Command

```bash
python3 -m http.server 80
```

## Description

Starts a simple HTTP server to listen for incoming SSRF-forged requests, useful for blind exploitation confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `python3` | Python interpreter | Yes |
| `-m http.server` | Module to run HTTP server | Yes |
| `80` | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
python3 -m http.server 80
```

### Advanced Usage

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

## Expected Output

Server startup message and logs of incoming GET requests, e.g., '127.0.0.1 - - [01/Oct/2024 12:00:00] "GET /payload HTTP/1.1" 200 -'.

## Related

- [[Related Procedure: Exploit Blind SSRF via URL Parameter]]
