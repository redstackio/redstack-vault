---
data: ngrok http 5000
tags:
  - tunneling
  - exposure
type: command
executor: bash
platforms:
  - Linux
id: 721a7847-0b94-49ea-ba78-35ef890c018b
created_at: '2025-12-11T03:48:06.032Z'
updated_at: '2025-12-11T03:48:06.032Z'
verified: false
validated: true
submitted: true
---
# ngrok-expose-local-server

## Command

```bash
ngrok http 5000
```

## Description

Uses ngrok to create a public tunnel to a local HTTP server on port 5000, providing a URL for remote access in exploits like fake API servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http` | Protocol to tunnel | Yes |
| `5000` | Local port to expose | Yes |

## Examples

### Basic Usage

```bash
ngrok http 5000
```

### Advanced Usage

```bash
ngrok http --region=us 5000
```

## Expected Output

Ngrok session with forwarding URL like https://xxxx.ngrok.io -> http://localhost:5000.

## Related

- [[procedures/Setup-Fake-GitHub-API-Server-with-Ngrok]]
- #ngrok
