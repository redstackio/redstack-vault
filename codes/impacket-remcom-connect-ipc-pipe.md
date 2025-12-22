---
type: code
language: python
verified: true
platforms:
  - Windows
tags:
  - impacket
  - smb
  - internal
validated: true
---

# impacket-remcom-connect-ipc-pipe

## Code

```python
tid = s.connectTree('IPC$')
fid_main = self.openPipe(s,tid,r'\RemCom_communicaton',0x12019f)
```

## Description

This Python snippet from Impacket's psexec implementation establishes an SMB connection to the IPC$ tree on a remote Windows host and opens the RemCom communication named pipe. It is used internally to set up the channel for sending commands and receiving output during remote execution, mimicking PSExec's service communication.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| s | SMB connection socket object from Impacket | impacket.smbconnection.SMBConnection(...) |
| tid | Tree ID returned from connectTree | Integer tree identifier |
| r'\RemCom_communicaton' | Named pipe path for RemCom service | Fixed string |
| 0x12019f | Access flags (read/write, etc.) | Fixed integer |

## Usage

Embed this in custom Impacket scripts for low-level SMB pipe manipulation, such as building a custom remote executor. Typically used after authenticating and before sending command packets. Not for direct execution; requires full Impacket context.

## Detection

- Monitor for SMB pipe opens to unusual names like RemCom_communicaton.
- Log SMB Tree Connect to IPC$ from non-admin tools.
- Network IDS signatures for Impacket SMB patterns (e.g., specific transact requests).

## Related

- [[procedures/windows-impacket-psexec-remote-execution-with-credentials]]
- [[tools/Impacket]]
