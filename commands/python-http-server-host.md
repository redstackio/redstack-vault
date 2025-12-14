---
id: cmd-python-http-server
data: python -m http.server
tags:
  - hosting
  - http
type: command
output: 'Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...'
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.934Z'
verified: false
validated: true
submitted: true
---
# python-http-server-host

## Command

```bash
python -m http.server
```

## Description

Starts a basic HTTP server using Python's http.server module to serve files from the current directory, commonly used for quick local hosting of static content like exploit HTML files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Runs the specified module (http.server) | Yes |
| `http.server` | The module to execute, defaults to port 8000 | Yes |

## Examples

### Basic Usage

```bash
python -m http.server
```

### Advanced Usage

```bash
python -m http.server 8080
```

> Binds to port 8080 instead of default 8000.

## Expected Output

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ... -- press Ctrl+C to shut down.

## Related

- [[Related Procedure|procedures/Host-Burp-Exploit-Page]]
