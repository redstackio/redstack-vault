---
id: cmd-start-python-simplehttpserver
data: python -m SimpleHTTPServer 80
tags:
  - hosting
  - http-server
type: command
output: Serving HTTP on 0.0.0.0 port 80 ...
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.129Z'
verified: false
validated: true
submitted: true
---
# start-python-simplehttpserver

## Command

```bash
python -m SimpleHTTPServer 80
```

## Description

This command starts Python's built-in SimpleHTTPServer module to host static files from the current directory on port 80, commonly used in security testing to serve malicious HTML/JS for RFI or XSS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Runs the specified module | Yes |
| `SimpleHTTPServer` | The module to run for HTTP serving | Yes |
| `80` | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
python -m SimpleHTTPServer 80
```

### Advanced Usage

```bash
python -m SimpleHTTPServer 8080
```

> Changes port to 8080 if 80 is unavailable.

## Expected Output

"Serving HTTP on 0.0.0.0 port 80 ..." followed by logs of incoming GET requests, such as "GET /t.html HTTP/1.1" 200 -

## Related

- [[Related Procedure: Host-Malicious-HTML-for-RFI-Exploitation]]
