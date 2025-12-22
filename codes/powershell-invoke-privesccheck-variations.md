---
id: 687ee0a7-7358-42bf-9a53-58da76f37759
type: code
name: powershell-invoke-privesccheck-variations
language: powershell
verified: true
created_at: '2023-04-06T03:56:28.514528+00:00'
updated_at: '2023-04-10T20:37:50.960310+00:00'
platforms:
  - Windows
tags:
  - privesc
  - enumeration
validated: true
---

# powershell-invoke-privesccheck-variations

## Code

```powershell
C:\Temp\>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
C:\Temp\>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended"
C:\Temp\>powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck -Report PrivescCheck_%COMPUTERNAME% -Format TXT,CSV,HTML"
```

## Description

Variations of invoking PrivescCheck.ps1 for basic, extended, and reporting modes from a temp directory.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| %COMPUTERNAME% | Auto-inserts hostname in report | WORKSTATION |
| -Format TXT,CSV,HTML | Output formats for report | TXT only |

## Usage

Run from a writable dir like C:\Temp; use reporting for exfil or analysis in privesc workflows.

## Detection

- Multiple PowerShell -c invocations (pattern in logs).
- File creation of reports with privesc keywords.
- Script loading from temp dirs (behavioral alerts).

## Related

- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
- [[tools/PrivescCheck]]
