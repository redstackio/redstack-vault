---
type: command
executor: bash
data: python3 -m http.server $_PORT --directory $_HOST_DIR
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - hosting
  - web-server
verified: true
validated: true
---

# Host CSRF Page with Python

## Command

```bash
python3 -m http.server $_PORT --directory $_HOST_DIR
```

## Description

This command starts a simple HTTP server using Python's built-in module to host the malicious CSRF HTML page. It is useful for quickly serving static files during web-based attacks like CSRF, allowing the attacker to deliver the payload via a controlled domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | Port to listen on (e.g., 80, 8080) | Yes |
| $_HOST_DIR | Directory containing the HTML file (e.g., /path/to/csrf) | Yes |

## Examples

### Basic Usage

```bash
python3 -m http.server 8080 --directory ./public
```

### Advanced Usage

```bash
python3 -m http.server 80 --directory /var/www/csrf --bind 0.0.0.0
```

## Expected Output

Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
127.0.0.1 - - [01/Oct/2023 12:00:00] "GET /csrf.html HTTP/1.1" 200 -

The server runs indefinitely until stopped (Ctrl+C), logging requests to the console.

## Related

- [[procedures/perform-csrf-attack-with-semicolon-referer-bypass]]
