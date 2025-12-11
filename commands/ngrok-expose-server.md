---
id: 7ccd8d1b-7b6a-4116-b7a2-7111ad2a9cdf
type: command
executor: bash
data: ngrok http 5000
output: null
created_at: '2025-12-11T03:48:05.889Z'
updated_at: '2025-12-11T03:48:05.889Z'
platforms:
  - Linux
tags:
  - tunnel
  - ngrok
verified: false
validated: true
submitted: true
---

# ngrok-expose-server

## Command

```bash
ngrok http 5000
```

## Description

Expose the local Flask server externally by tunneling HTTP traffic on port 5000, making the proxy accessible for GitLab import.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http 5000` | Tunnel HTTP traffic on port 5000 | Yes |

## Examples

### Basic Usage

```bash
ngrok http 5000
```

## Expected Output

Ngrok interface showing the forwarding URL (e.g., https://random.ngrok.io -> http://localhost:5000).

## Related

- [[procedures/Setup-Proxy-Server-with-Flask-and-Ngrok]]
- [[commands/flask-run-proxy]]
