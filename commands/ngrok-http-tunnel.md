---
id: cmd-ngrok-http-tunnel
data: ngrok http 5000
tags:
  - tunnel
  - ngrok
type: command
output: 'Forwarding URL like https://abc.ngrok.io'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.578Z'
verified: false
validated: true
submitted: true
---
# ngrok-http-tunnel

## Command

```bash
ngrok http 5000
```

## Description

Creates an HTTP tunnel exposing local port 5000 to a public ngrok URL, allowing external access to the mock API server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ngrok | Tunnel tool | Yes |
| http | Protocol | Yes |
| 5000 | Local port | Yes |

## Examples

### Basic Usage

```bash
ngrok http 5000
```

### Advanced Usage

With subdomain: `ngrok http 5000 --subdomain=mock`.

## Expected Output

ngrok session with forwarding https://random.ngrok.io -> http://localhost:5000.

## Related

- [[tools/ngrok]]
