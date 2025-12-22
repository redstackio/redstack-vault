---
id: c337c7f5-c0f0-4d14-b81c-d9d5d36c3f88
name: powershell-check-laps-admpwd-dll-integrity
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:04.492573+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - laps
  - integrity-check
  - active-directory
validated: true
---

# powershell-check-laps-admpwd-dll-integrity

## Code

```powershell
Get-ChildItem 'c:\program files\LAPS\CSE\Admpwd.dll'
Get-FileHash 'c:\program files\LAPS\CSE\Admpwd.dll'
Get-AuthenticodeSignature 'c:\program files\LAPS\CSE\Admpwd.dll'
```

## Description

This PowerShell script performs a comprehensive integrity check on the LAPS Admpwd.dll file by confirming its existence, computing its hash, and validating its digital signature. It is used as a preliminary step to verify LAPS installation before attempting password retrieval from Active Directory.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The script uses a hardcoded path; modify 'c:\\program files\\LAPS\\CSE\\Admpwd.dll' for custom locations | N/A |

## Usage

Execute this script on a domain-joined Windows machine to quickly assess LAPS CSE deployment. Run in PowerShell: .\script.ps1 or paste directly. If all checks pass, proceed to AD queries for password retrieval. Ideal for initial reconnaissance in AD environments.

## Detection

- PowerShell execution logs (Module Logging, Script Block Logging) showing Get-ChildItem, Get-FileHash, or Get-AuthenticodeSignature on LAPS paths.
- File access audits on Admpwd.dll (Event ID 4663).
- Anomaly detection in EDR for unusual DLL queries in Program Files\LAPS.

## Related

- [[procedures/Check-LAPS-Installation-and-Retrieve-Password]]
- [[powershell-get-adcomputer-laps-password]]
