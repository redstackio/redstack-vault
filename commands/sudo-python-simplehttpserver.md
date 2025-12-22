---
data: sudo python -m SimpleHTTPServer 80
tags:
  - server
  - capture
  - python
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 6bb36e6c-6abb-4061-8bca-d6d002222bfa
created_at: '2025-12-14T04:39:09.647Z'
updated_at: '2025-12-14T04:39:09.647Z'
verified: false
validated: true
submitted: true
---
# sudo-python-simplehttpserver

## Command

```bash
sudo python -m SimpleHTTPServer 80
```

## Description

Starts a basic HTTP server on port 80 using Python's SimpleHTTPServer module to serve files and log incoming requests, requiring sudo for privileged port.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Runs the specified module (SimpleHTTPServer) | Yes |
| `80` | Port to bind the server to | Yes |

## Examples

### Basic Usage

```bash
sudo python -m SimpleHTTPServer 80
```

### Advanced Usage

```bash
sudo python -m SimpleHTTPServer 8080
```

## Expected Output

"Serving HTTP on 0.0.0.0 port 80 ..." and request logs upon hits.

## Related

- [[procedures/Start-Local-HTTP-Server-to-Capture-SSRF]]
- [[tools/Python-SimpleHTTPServer]]
