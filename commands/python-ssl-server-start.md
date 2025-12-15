---
data: python ssl_server.py
tags:
  - https-server
  - python
type: command
output: 'Serving HTTPS on localhost port 5000 (https://localhost:5000/)'
executor: bash
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.608Z'
id: 197ef547-21bf-4e75-b890-e03146fb9100
verified: false
validated: true
submitted: true
---
# python-ssl-server-start

## Command

```bash
python ssl_server.py
```

## Description

Starts a rudimentary HTTPS server using Python 3 to host local files, including the malicious disable_features3.html, on https://localhost:5000 with an invalid self-signed certificate. Used in testing browser extension vulnerabilities requiring HTTPS to trigger security features like Kaspersky's URL Advisor.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ssl_server.py` | The Python script file implementing the HTTPS server | Yes |

## Examples

### Basic Usage

```bash
python ssl_server.py
```

### Advanced Usage

Run in a directory containing the exploit HTML; no additional flags needed for basic operation.

```bash
cd /path/to/exploit/files && python ssl_server.py
```

## Expected Output

Console displays: "Serving HTTPS on localhost port 5000 (https://localhost:5000/)". The server listens for requests and serves files like disable_features3.html over HTTPS, prompting certificate warnings in browsers.

## Related

- [[Related Procedure|procedures/Host-Malicious-Exploit-Page]]
