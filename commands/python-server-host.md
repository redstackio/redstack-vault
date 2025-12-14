---
data: python -m http.server 8000
tags:
  - web
  - hosting
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.822Z'
id: bcd253cf-052b-4bed-83e6-caf27f000e2c
verified: false
validated: true
submitted: true
---
# python-server-host

## Command

```bash
python -m http.server 8000
```

## Description

This command starts a simple HTTP server using Python's built-in module to host static files, such as a CSRF PoC HTML page, on port 8000. It is useful for quickly serving malicious or test pages during web vulnerability exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Specifies the module to run | Yes |
| `http.server` | The module name for the HTTP server | Yes |
| `8000` | The port to bind to | No (default 8000) |

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
127.0.0.1 - - [01/Oct/2023 12:00:00] "GET /poc.html HTTP/1.1" 200 -

## Related

- [[Related Procedure]]
