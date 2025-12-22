---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
name: start-simple-http-server
type: command
executor: bash
data: python -m SimpleHTTPServer 80
output: Serving HTTP on 0.0.0.0 port 80 ...
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.655Z'
platforms:
  - Linux
  - macOS
tags:
  - hosting
  - web
verified: false
validated: true
submitted: true
---

# start-simple-http-server

## Command

```bash
python -m SimpleHTTPServer 80
```

## Description

Starts Python's built-in SimpleHTTPServer module to host static files, such as malicious HTML for RFI/XSS attacks, on the specified port (default 80 for HTTP).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `80` | Port to bind the server (HTTP standard) | No (defaults to 8000 if omitted) |

## Examples

### Basic Usage

```bash
python -m SimpleHTTPServer 80
```

### Advanced Usage

```bash
python -m SimpleHTTPServer 8080
```

## Expected Output

"Serving HTTP on 0.0.0.0 port 80 ..." followed by request logs like "127.0.0.1 - - [date] "GET /t.html HTTP/1.1" 200 -"

## Related

- [[Related Procedure|procedures/Host-Malicious-HTML-for-RFI-Exploitation]]
