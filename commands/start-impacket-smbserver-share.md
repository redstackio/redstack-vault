---
type: command
executor: bash
data: python3 smbserver.py share /tmp/smb/ -smb2support
output: null
platforms:
  - Linux
tags:
  - smb
  - hosting
  - printnightmare
verified: true
validated: true
---

# start-impacket-smbserver-share

## Command

```bash
python3 smbserver.py share /tmp/smb/ -smb2support
```

## Description

This command starts an SMB server using Impacket's smbserver.py to host files from a specified directory, commonly used for serving malicious payloads in exploits like PrintNightmare. It creates a share named 'share' and supports SMBv2 for Windows compatibility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `share` | Name of the SMB share to create | Yes |
| `/tmp/smb/` | Local directory to share (place payloads here) | Yes |
| `-smb2support` | Enable SMBv2 protocol support | No (recommended for modern targets) |

## Examples

### Basic Usage

```bash
python3 smbserver.py share /tmp/smb/
```

Starts the server without SMBv2; use for older systems.

### Advanced Usage

```bash
python3 smbserver.py share /tmp/payloads/ -smb2support -username attacker -password pass123
```

Adds authentication to the share for controlled access.

## Expected Output

```
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

Selected interface 'eth0'
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-012B20ED8D75 V:1.0
[*] Types added: {\'MsRPC:12345778-1234-ABCD-EF00-0123456789AB': <class \'impacket.dcerpc.v5.rpcrt.RuntimeExtendedError\'>}
[*] Types added: {\'NDR:12345678-1234-ABCD-EF00-01234567CFFB': <class \'impacket.dcerpc.v5.dtypes.RPC_SID\'>}
Impacket-SMBServer ['\\ATTACKER_IP']
Server started on port 445
```

The server listens for connections; during exploitation, expect auth logs like '[*] Authenticating against ATTACKER_IP as DOMAIN\\user'.

## Related

- [[procedures/PrintNightmare-SMB-Server-Payload-Hosting]]
- [[tools/Impacket-SmbServer]]
