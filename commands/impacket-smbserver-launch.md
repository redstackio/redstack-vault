---
type: command
executor: python
data: smbserver.py $_SHARE_NAME $_SHARE_PATH -smb2support
platforms:
  - Linux
  - Windows
tags:
  - smb
  - server
verified: true
validated: true
---

# impacket-smbserver-launch

## Command

```python
smbserver.py $_SHARE_NAME $_SHARE_PATH -smb2support
```

## Description

This command launches an SMB server using Impacket's smbserver.py script, serving files from a local directory over the SMB protocol. It is typically used to host payloads or tools for download by remote compromised systems during penetration testing or red team operations. The -smb2support flag ensures compatibility with modern Windows clients that do not support SMBv1 by default.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SHARE_NAME | The name of the SMB share to create (e.g., 'SHARE') | Yes |
| $_SHARE_PATH | The local filesystem path to serve as the share (e.g., '/tmp') | Yes |
| -smb2support | Enables SMBv2 protocol support for broader client compatibility | No (but recommended) |
| -ip $_IP | Binds the server to a specific IP address | No (defaults to all interfaces) |
| -user $_USERNAME | Sets the username for share authentication | No |
| -password $_PASSWORD | Sets the password for share authentication | No (if -user is used) |

## Examples

### Basic Usage

Launch a basic SMB server without authentication, serving /tmp as 'share'.

```python
smbserver.py share /tmp
```

### Advanced Usage

Launch with SMBv2 support and authentication, bound to a specific IP.

```python
smbserver.py share /tmp -smb2support -ip 192.168.1.100 -user attacker -password secret
```

## Expected Output

Upon successful launch, the command outputs Impacket version information, configuration parsing details, and protocol callback registrations. The server then listens for connections.

```
smbserver.py share /tmp
Impacket v0.9.20-dev - Copyright 2019 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
[*] Incoming connection (192.168.1.50,49159)
[*] AUTHENTICATE_MESSAGE (\SHARE,administrator@domain.com)
[*] ===== Incoming SMB1 SessionSetup ===== user: domain\administrator || password: || nt_password:  || aes_key:  || hmac_key:  ||
[*] AUTHENTICATE_MESSAGE (ADMIN$,administrator@domain.com)
[*] ===== Incoming SMB1 TreeConnect ===== \ADMIN$
```

Success is indicated by the server starting without errors and logging incoming connections when clients attempt to access the share.

## Related

- [[Related Procedure: Serve-Payloads-via-SMB]]
- [[tools/Impacket-SMB-Server]]
