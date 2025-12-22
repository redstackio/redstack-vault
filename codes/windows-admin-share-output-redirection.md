---
id: 0645e1ae-d4bd-4fc4-a52c-e4a1f422d0b5
name: windows-admin-share-output-redirection
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:30.959394+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - output-redirection
  - smb-share
  - wmi
validated: true
---

# Windows Admin Share Output Redirection

## Code

```cmd
cmd.exe /Q /c cd 1> \\127.0.0.1\ADMIN$\__RANDOM 2>&1
```

## Description

This Windows command snippet redirects the output of a simple diagnostic command (like 'cd' to get current directory) to a file in the hidden ADMIN$ SMB share. It uses quiet mode (/Q) to suppress banners and redirects both stdout and stderr. The __RANDOM placeholder should be replaced with a unique directory name (e.g., a UUID) to avoid conflicts during parallel executions. This is commonly used in remote execution tools like WMIExec to stage output for retrieval without interactive access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| __RANDOM | Unique directory name in ADMIN$ share | temp-uuid-1234 |
| \\127.0.0.1\ADMIN$ | Path to local ADMIN$ share (use target IP for remote) | \\192.168.1.100\ADMIN$ |

## Usage

Embed this as the remote command in tools like Impacket's wmiexec.py for non-interactive executions. After running, connect to the share via SMB (e.g., using smbclient) to download the output file. Ideal for lateral movement where direct output capture is unavailable. Example integration: `wmiexec.py user:pass@target "cmd.exe /Q /c whoami 1> \\127.0.0.1\ADMIN$\temp-out 2>&1"`.

## Detection

- File creation in ADMIN$ or other admin shares (monitor via Sysmon Event ID 11 for unexpected files).
- Anomalous cmd.exe spawns with redirection to localhost or shares (Event ID 4688 in Windows logs).
- SMB access patterns from unexpected sources.

## Related

- [[procedures/remote-command-execution-via-wmi-using-impacket]]
- [[tools/Impacket]]
