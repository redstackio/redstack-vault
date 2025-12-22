---
type: command
executor: bash
data: python3 -m http.server $_PORT
tags:
  - hosting
  - http
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# python-start-http-server

## Command

```bash
python3 -m http.server $_PORT
```

## Description

This command starts Python's built-in HTTP server to host static files (e.g., malicious HTML) or log incoming requests for exfiltration in web attacks like CSWSH.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `python3` | Python 3 executable | Yes |
| `-m http.server` | Run the http.server module | Yes |
| `$_PORT` | Port to listen on (e.g., 8000 for hosting, 9000 for exfil) | Yes |

## Examples

### Basic Usage

```bash
python3 -m http.server 8000
```

### Advanced Usage

Bind to all interfaces for remote access:

```bash
python3 -m http.server 8000 --bind 0.0.0.0
```

## Expected Output

```
Serving HTTP at 0.0.0.0:8000
127.0.0.1 - - [06/Apr/2023 03:56:41] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Apr/2023 03:56:41] "GET /?data=exfil HTTP/1.1" 200 -
```

Success: Logs show serving files or incoming requests with query params for exfil.

## Related

- [[procedures/Perform-Cross-Site-WebSocket-Hijacking]]
