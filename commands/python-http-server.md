---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567890
data: python -m http.server 8000
tags:
  - hosting
  - web-server
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:42.568Z'
verified: false
validated: true
submitted: true
---
# python-http-server

## Command

```bash
python -m http.server 8000
```

## Description

Starts a simple HTTP server using Python's built-in module to host static files, such as malicious HTML for CSRF attacks. Useful for quickly serving content during web-based exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Runs the module | Yes |
| `http.server` | The module name | Yes |
| `8000` | Port to listen on | No (default 8000) |

## Examples

### Basic Usage

```bash
python -m http.server 8000
```

### Advanced Usage

```bash
python -m http.server 8080 --bind 127.0.0.1
```

## Expected Output

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 - - [01/Oct/2023 12:00:00] "GET /csrf.html HTTP/1.1" 200 -

## Related

- [[Related Procedure]]
