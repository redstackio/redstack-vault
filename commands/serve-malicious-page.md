---
id: cmd-serve-malicious-page
data: python3 -m http.server 8000
tags:
  - web
  - hosting
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.726Z'
verified: false
validated: true
submitted: true
---
# serve-malicious-page

## Command

```bash
python3 -m http.server 8000
```

## Description

This command starts a simple HTTP server using Python's built-in module to serve static files, such as a malicious HTML page for clickjacking attacks, from the current directory on port 8000.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `python3` | Python 3 interpreter | Yes |
| `-m` | Run library module as script | Yes |
| `http.server` | The HTTP server module | Yes |
| `8000` | Port to listen on | No (default 8000) |

## Examples

### Basic Usage

```bash
python3 -m http.server 8000
```

Serves files from the current directory at http://localhost:8000.

### Advanced Usage

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

Binds to all interfaces on port 8080 for external access.

## Expected Output

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 - - [Date] "GET /clickjack.html HTTP/1.1" 200 -

Indicates the server is running and serving requested files successfully.

## Related

- [[Related Procedure|procedures/Exploit-Clickjacking-with-Transparent-Iframe]]
