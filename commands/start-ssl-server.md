---
data: sudo python3 ssl_server.py
tags:
  - ssl
  - server
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 6ead610a-a937-47a5-bfbf-76c966028c67
created_at: '2025-12-14T17:29:36.435Z'
updated_at: '2025-12-14T17:29:36.435Z'
verified: false
validated: true
submitted: true
---
# start-ssl-server

## Command

```bash
sudo python3 ssl_server.py
```

## Description

Starts a local SSL web server using a Python script, binding to port 443 for HTTPS serving of exploit files with a self-signed certificate.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sudo` | Elevate privileges for port 443 | Yes |
| `python3` | Python interpreter | Yes |
| `ssl_server.py` | Script to execute | Yes |

## Examples

### Basic Usage

```bash
sudo python3 ssl_server.py
```

### Advanced Usage

Run in background: `sudo nohup python3 ssl_server.py &`

## Expected Output

Server startup message like "Serving HTTP on 0.0.0.0 port 443 (https)..." indicating it's listening.

## Related

- [[Related Procedure]]
