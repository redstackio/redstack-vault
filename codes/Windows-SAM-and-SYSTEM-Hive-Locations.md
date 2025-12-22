---
id: defcbe57-2d99-47a3-81fc-08c0929ef788
name: Windows-SAM-and-SYSTEM-Hive-Locations
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:28.805392+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - registry
  - hives
validated: true
---

# Windows-SAM-and-SYSTEM-Hive-Locations

## Code

```powershell
# Usually %SYSTEMROOT% = C:\Windows
%SYSTEMROOT%\repair\SAM
%SYSTEMROOT%\System32\config\RegBack\SAM
%SYSTEMROOT%\System32\config\SAM
%SYSTEMROOT%\repair\system
%SYSTEMROOT%\System32\config\SYSTEM
%SYSTEMROOT%\System32\config\RegBack\system
```

## Description

This PowerShell snippet lists the common file paths for SAM and SYSTEM registry hives on Windows systems, including backups. It aids in locating files for copying during offline hash extraction.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `%SYSTEMROOT%` | Windows system root directory | `C:\Windows` |

## Usage

Execute in PowerShell on the target to display paths, then use `Get-ChildItem` or `copy` to extract files to a safe location for offline processing in procedures like SAM hash dumping.

## Detection

- Monitor PowerShell execution for path enumeration in config directories.
- File access logs to System32\config via Sysmon or EDR.
- Unusual copies of SAM/SYSTEM files to temp directories.

## Related

- [[procedures/Windows-SAM-and-SYSTEM-Hash-Extraction]]
