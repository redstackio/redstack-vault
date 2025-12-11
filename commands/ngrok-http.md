---
data: ngrok http 5000
tags:
  - exposure
type: command
executor: bash
platforms:
  - Linux
id: 189c93cf-8b8c-4de0-9879-43c8d801fd6d
created_at: '2025-12-11T03:48:05.997Z'
updated_at: '2025-12-11T03:48:05.997Z'
verified: false
validated: true
submitted: true
---
# ngrok-http

## Command

```bash
ngrok http 5000
```

## Description

Exposes a local port via ngrok tunnel.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http 5000` | Protocol and port | Yes |

## Examples

### Basic Usage

```bash
ngrok http 8080
```

## Expected Output

Ngrok tunnel URL

## Related

- #ngrok
