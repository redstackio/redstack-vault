---
id: uuid-python3-ssl-server
data: sudo python3 ssl_server.py
tags:
  - server
  - https
type: command
output: Serving HTTPS on 0.0.0.0 port 443 (type Ctrl+C to shut down)
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.048Z'
verified: false
validated: true
submitted: true
---
# python3-ssl-server

## Command

```bash
sudo python3 ssl_server.py
```

## Description

Starts a local HTTPS web server using the custom ssl_server.py script, binding to port 443 to host exploit files like exploit_preview.html under a spoofed domain for postMessage-based XSS attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sudo` | Elevates privileges for port 443 binding | Yes (Linux/macOS) |
| `python3` | Python interpreter | Yes |
| `ssl_server.py` | Script file in current directory | Yes |

## Examples

### Basic Usage

```bash
sudo python3 ssl_server.py
```

### Advanced Usage

Run in background: ```bash
sudo nohup python3 ssl_server.py &
```

## Expected Output

Server startup message indicating HTTPS on port 443, followed by request logs when accessing hosted files.

## Related

- [[procedures/Start-Local-SSL-Server]]
