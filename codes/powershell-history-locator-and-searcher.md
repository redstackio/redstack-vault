---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - credential-access
  - looting
  - powershell
validated: true
---

# powershell-history-locator-and-searcher

## Code

```powershell
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
type C:\Users\swissky\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
type $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
cat (Get-PSReadlineOption).HistorySavePath
cat (Get-PSReadlineOption).HistorySavePath | sls passw
```

## Description

This PowerShell snippet locates the command history file maintained by the PSReadLine module, displays its contents using multiple path resolution methods for compatibility, retrieves the official history path, and searches for lines containing potential password indicators (e.g., 'passw'). It is designed for quick credential looting from user history logs during privilege escalation attempts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The code uses fixed paths and built-in cmdlets; no user-defined variables | N/A |

## Usage

Execute this snippet directly in a PowerShell session with low-privilege access to dump and analyze history for exposed credentials. It is particularly useful after initial access to a user account that may have run administrative commands with plaintext passwords. Follow up by manually reviewing output for usable credentials to attempt escalation (e.g., via RunAs or psexec).

## Detection

- PowerShell execution logs showing Get-PSReadlineOption or Select-String on AppData paths.
- File access monitoring on %APPDATA%\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt.
- Anomalous searches for strings like 'passw' in logs via ETW or Sysmon.

## Related

- [[procedures/Windows-Privilege-Escalation-via-Powershell-History-Looting]]
