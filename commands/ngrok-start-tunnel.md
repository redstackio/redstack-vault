---
id: cmd-uuid-1
data: ngrok http 80
tags:
  - tunnel
  - ssrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.262Z'
verified: false
validated: true
submitted: true
---
# ngrok-start-tunnel

## Command

```bash
ngrok http 80
```

## Description

Starts an ngrok tunnel exposing a local HTTP server on port 80 to a public URL, used in SSRF attacks to capture server-initiated requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http` | Protocol to tunnel (HTTP) | Yes |
| `80` | Local port to forward | Yes |

## Examples

### Basic Usage

```bash
ngrok http 80
```

### Advanced Usage

```bash
ngrok http 8080 --subdomain custom-ssrf
```

## Expected Output

ngrok by @inconshreveable

Session Status                online
Account                       your-account (Plan: Free)
Version                       3.x.x
Region                        United States (us)
Latency                       50ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://abc123.ngrok.io -> http://localhost:80

## Related

- [[Related Procedure: Set-Up-Ngrok-Listener-for-Request-Capture]]
