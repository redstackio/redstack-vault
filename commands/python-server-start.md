---
id: cmd-python-server-start
data: python server.py
tags:
  - server
  - poc
type: command
output: 'Serving HTTP on 0.0.0.0 port 5000 (http://0.0.0.0:5000/) ...'
executor: bash
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.172Z'
verified: false
validated: true
submitted: true
---
# python-server-start

## Command

```bash
python server.py
```

## Description

Starts a rudimentary HTTP server using Python 3 to host proof-of-concept files like universal_xss.html on localhost:5000, essential for serving malicious content in XSS exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| server.py | The Python script implementing the HTTP server | Yes |

## Examples

### Basic Usage

```bash
python server.py
```

### Advanced Usage

```bash
# If port needs change, modify server.py; default is 5000
python server.py
```

## Expected Output

Server logs: 'Serving HTTP on 0.0.0.0 port 5000 (http://0.0.0.0:5000/) ...' and readiness to handle requests for /universal_xss.html.

## Related

- [[Related Procedure|procedures/Host-Malicious-POC-Server-with-Python]]
