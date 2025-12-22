---
type: command
executor: bash
data: ./ngrok http 4433
tags:
  - tunnel
  - http
platforms:
  - Linux
verified: true
validated: true
---

# deploy-ngrok-http-forwarding

## Command

```bash
./ngrok http 4433
```

## Description

Starts an HTTP tunnel forwarding public requests to local port 4433, exposing the service via a temporary public URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 4433 | Local port to forward to | Yes |
| --region (optional) | Ngrok region (e.g., us) | No |

## Examples

### Basic Usage

```bash
./ngrok http 4433
```

### Advanced Usage

```bash
./ngrok http 4433 --subdomain=mytunnel
```

## Expected Output

ngrok by @inconshreveable

Session Status                online
Account                       youraccount (Plan: Free)
Version                       2.3.40
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://abc123.ngrok.io -> http://localhost:4433

## Related

- [[procedures/Setup-Ngrok-Port-Forwarding-Tunnel]]
