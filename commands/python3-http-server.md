---
data: python3 -m http.server 8000
tags:
  - hosting
  - web-server
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:04.873Z'
id: bbe754f2-72aa-47de-ae95-72bb7b24e90a
verified: false
validated: true
submitted: true
---
# python3-http-server

## Command

```bash
python3 -m http.server 8000
```

## Description

This command starts a simple HTTP server using Python 3's built-in module to host static files like HTML PoCs locally, useful for testing web-based attacks such as ClickJacking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Specifies the module to run | Yes |
| `http.server` | The HTTP server module | Yes |
| `8000` | Port to listen on (default 8000) | No |

## Examples

### Basic Usage

```bash
python3 -m http.server 8000
```

### Advanced Usage

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

## Expected Output

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 - - [date] "GET /poc.html HTTP/1.1" 200 -

## Related

- [[Related Procedure]]
