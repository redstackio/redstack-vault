---
data: ./ngrok http 8080
tags:
  - tunneling
type: command
output: Public ngrok URL for tunneling
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.905Z'
id: 25b4aa4a-0b27-4265-b87d-810c020c5313
verified: false
validated: true
submitted: true
---
# ngrok-tunnel-http

## Command

```bash
./ngrok http 8080
```

## Description

Create secure tunnel to local port for exfiltration server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| http | Protocol | Yes |
| 8080 | Local port | Yes |

## Examples

### Basic Usage

```bash
./ngrok http 8080
```

## Expected Output

ngrok.io URL.

## Related

- [[procedures/Exfiltrate-2FA-Code-Using-CSS-Selectors]]
