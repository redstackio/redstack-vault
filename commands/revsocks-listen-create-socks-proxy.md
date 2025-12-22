---
id: 0d4f933d-4a43-4489-9208-6d4dd94ccc21
name: revsocks-listen-create-socks-proxy
type: command
executor: bash
data: './revsocks -listen :8443 -socks 127.0.0.1:1080 -pass Password1234'
output: null
created_at: '2023-04-06T03:56:22.907095Z'
updated_at: '2023-04-10T20:25:18.397562Z'
platforms:
  - Linux
  - Windows
tags:
  - proxy
  - pivoting
verified: true
validated: true
---

# revsocks-listen-create-socks-proxy

## Command

```bash
./revsocks -listen :8443 -socks 127.0.0.1:1080 -pass Password1234
```

## Description

Starts the revsocks server to listen for reverse connections and bind a local SOCKS5 proxy on port 1080.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -listen :8443 | Listening address/port | Yes |
| -socks 127.0.0.1:1080 | Local SOCKS proxy | Yes |
| -pass Password1234 | Authentication password | Yes |

## Examples

### Basic Usage

```bash
./revsocks -listen :8443 -socks 127.0.0.1:1080 -pass Password1234
```

## Expected Output

Listening on :8443
SOCKS5 proxy started on 127.0.0.1:1080
Waiting for connection...

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
