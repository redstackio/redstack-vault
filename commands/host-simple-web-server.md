---
type: command
executor: bash
data: python3 -m http.server $_PORT
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - linux
  - macos
tags:
  - web-hosting
  - server
verified: true
validated: true
---

# host-simple-web-server

## Command

```bash
python3 -m http.server $_PORT
```

## Description

Starts a basic HTTP server using Python's built-in module to host static files like the malicious HTML page for the CSRF attack. Ideal for quick testing or serving from an attacker-controlled machine. Default port is 8000 if not specified.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | The port to listen on (e.g., 8000, 8080) | No (defaults to 8000) |

## Examples

### Basic Usage

```bash
python3 -m http.server 8000
```

Serves files from the current directory on port 8000.

### Advanced Usage

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

Binds to all interfaces for external access.

## Expected Output

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 - - [01/Oct/2023 12:00:00] "GET / HTTP/1.1" 200 -

Indicates the server is running and serving requests successfully.

## Related

- [[procedures/CSRF-Attack-Bypassing-Referer-Validation]]
