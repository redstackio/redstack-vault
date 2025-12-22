---
id: 6920dc2b-4cee-4b26-80aa-515d758560cc
name: Windows-PowerShell-Search-for-Credential-Files
type: code
language: Powershell
verified: true
created_at: '2023-04-06T03:56:28.986322+00:00'
updated_at: '2023-04-10T20:37:53.846607+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - discovery
  - looting
validated: true
---

# Windows-PowerShell-Search-for-Credential-Files

## Code

```powershell
dir /S /B *pass*.txt == *pass*.xml == *pass*.ini == *cred* == *vnc* == *.config*
where /R C:\ user.txt
where /R C:\ *.ini
```

## Description

This PowerShell code snippet performs a comprehensive filesystem search on Windows for potential credential files. It combines pattern-based searches using dir for keyword-laden files and where for specific names/extensions, aiding in the discovery of plain-text passwords during privilege escalation. The code is lightweight, using native commands to minimize footprint.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; hardcoded paths and patterns | N/A |

## Usage

Execute this snippet in a PowerShell session on a compromised Windows host, ideally after gaining initial shell access. Pipe output to a file for offline review (e.g., | Out-File results.txt). Follow up by inspecting listed files with Get-Content or notepad to extract credentials. Commonly used in red team operations for EoP looting before attempting token manipulation or lateral movement.

## Detection

- Monitor PowerShell execution logs (Module Logging, Script Block Logging) for dir/where commands with wildcard patterns.
- Sysmon Event ID 1 (Process Creation) for powershell.exe spawning with suspicious arguments.
- File access audits showing recursive reads in C:\ or user directories.
- EDR alerts on high-volume file enumerations targeting .ini or password patterns.

## Related

- [[procedures/Windows-EoP-Looting-for-Passwords]]
- [[commands/windows-dir-search-password-files]]
