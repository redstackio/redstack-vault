---
id: 4ea2d2a1-29ae-4096-8b56-bcbb19752578
type: code
name: powershell-execute-sherlock-for-privesc
language: powershell
verified: true
created_at: '2023-04-06T03:56:28.513726+00:00'
updated_at: '2023-04-10T20:37:50.960310+00:00'
platforms:
  - Windows
tags:
  - privesc
  - patch-check
validated: true
---

# powershell-execute-sherlock-for-privesc

## Code

```powershell
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File Sherlock.ps1
```

## Description

Executes the Sherlock script in a minimal PowerShell environment to check for missing patches and known privesc vulnerabilities across 200+ CVEs.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | Assumes Sherlock.ps1 is local; no params | N/A |

## Usage

Stage Sherlock.ps1 on target via initial access, then run to get quick vuln list. Use for targeted enumeration before deeper tools like Metasploit modules.

## Detection

- PowerShell spawning with -File flag (Event ID 4688).
- Script execution bypassing policy (Transcription logs).
- Checks against known KB numbers (behavioral EDR rules).

## Related

- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
- [[tools/Sherlock]]
