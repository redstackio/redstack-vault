---
data: ngrok http 5000
tags:
  - ngrok
  - tunneling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 407d1c0b-ccca-41a5-a6af-6a3f8c6e12eb
created_at: '2025-12-11T03:47:59.482Z'
updated_at: '2025-12-11T03:47:59.482Z'
verified: false
validated: true
submitted: true
---
# ngrok-expose-local-port

## Command

```bash
ngrok http 5000
```

## Description

Exposes a local HTTP server on the specified port to a public URL via ngrok.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http` | Protocol | Yes |
| `5000` | Local port | Yes |

## Examples

### Basic Usage

```bash
ngrok http 5000
```

### Advanced Usage

ngrok http --region eu 5000 for specific region.

## Expected Output

Tunnel information with forwarding URL like https://abc123.ngrok.io -> http://localhost:5000.

## Related

- [[procedures/Expose-Local-Fake-Server-with-Ngrok]]
- [[commands/flask-run-fake-server]]
