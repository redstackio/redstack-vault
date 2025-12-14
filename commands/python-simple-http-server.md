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
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:36.240Z'
id: 7eb2f7f0-5896-44d7-aa24-24bee2b62f08
verified: false
validated: true
submitted: true
---
# python-simple-http-server

## Command

```bash
python3 -m http.server 8000
```

## Description

This command starts Python's built-in HTTP server to host static files, such as malicious HTML for CSRF attacks, from the current directory on port 8000. Ideal for quick, low-profile hosting during web-based exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `python3` | Python 3 interpreter | Yes |
| `-m http.server` | Run the http.server module | Yes |
| `8000` | Port to bind (default 8000) | No |

## Examples

### Basic Usage

```bash
python3 -m http.server 8000
```

Serves files at http://localhost:8000.

### Advanced Usage

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

Binds to all interfaces on port 8080 for remote access.

## Expected Output

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 - - [Date] "GET /csrf_poc.html HTTP/1.1" 200 -

Indicates server running and files served successfully.

## Related

- [[Related Procedure: Host-Malicious-CSRF-Page]]
