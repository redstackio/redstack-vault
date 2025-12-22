---
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:28.589446+00:00'
updated_at: '2023-04-10T20:37:36.294286+00:00'
platforms:
  - Windows
tags:
  - discovery
  - drives
  - filesystem
validated: true
---

# mixed-shell-enumerate-windows-drives

## Code

```cmd
wmic logicaldisk get caption || fsutil fsinfo drives
wmic logicaldisk get caption,description,providername
Get-PSDrive | where {$_.Provider -like "Microsoft.PowerShell.Core\FileSystem"}| ft Name,Root
```

## Description

This multi-line snippet enumerates Windows drives using a combination of CMD and PowerShell commands. It lists drive letters (with fsutil fallback), detailed descriptions via WMIC, and filesystem roots via PowerShell. Ideal for mapping storage in escalation scenarios to find data or drop points.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables to substitute | N/A |

Note: Run lines 1-2 in CMD; line 3 in PowerShell.

## Usage

Use during post-compromise enumeration to identify all volumes, including network or removable drives. Check for writable locations (e.g., USB) or sensitive paths like C:\Windows\Temp for privilege escalation staging.

## Detection

- WMIC logicaldisk queries in WMI logs or process monitoring.
- fsutil executions, which are less common and may trigger alerts.
- PowerShell Get-PSDrive calls in script block logging (Module 4104).

## Related

- [[procedures/windows-os-information-gathering-for-privilege-escalation]]
