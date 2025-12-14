---
id: cmd-1
data: python server.py
tags:
  - http-server
  - dos
type: command
output: |
  Server running on 127.0.0.1:9000
executor: bash
platforms:
  - Linux
  - Unix-like
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.115Z'
verified: false
validated: true
submitted: true
---
# python-server-excessive-cookies

## Command

```bash
python server.py
```

## Description

Starts a Python HTTP server that responds with 256 Set-Cookie headers for domain hax.invalid, used to simulate malicious cookie injection in curl DoS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `server.py` | Script file with custom handler | Yes |

## Examples

### Basic Usage

```bash
python server.py
```

### Advanced Usage

Run in background: ```bash
python server.py &
```

## Expected Output

"Server running on 127.0.0.1:9000". Server handles GET requests by sending HTML and excessive cookies; logs incoming connections.

## Related

- [[Related Procedure|procedures/Set-Up-Malicious-HTTP-Server-for-Excessive-Cookies]]
