---
id: fe43f711-05a0-4264-a1b4-8a8abd559661
name: PowerShell-Constrained-Mode-Check-and-Bypass-Script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:23.987038+00:00'
updated_at: '2023-10-10T20:37:00.448153+00:00'
platforms:
  - Windows
tags:
  - powershell
  - evasion
  - discovery
validated: true
---

# PowerShell-Constrained-Mode-Check-and-Bypass-Script

## Code

```powershell
# Check if we are in a constrained mode
# Values could be: FullLanguage or ConstrainedLanguage
$ExecutionContext.SessionState.LanguageMode

## Bypass
powershell -version 2
```

## Description

This PowerShell script snippet first checks the current language mode to identify if Constrained Language Mode is active, then provides a bypass command to launch PowerShell v2 for unrestricted execution. It serves as a quick diagnostic and evasion tool in Windows environments where PowerShell restrictions are enforced.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; uses built-in session state and fixed version flag. | N/A |

## Usage

Execute the check line in an active PowerShell session to assess restrictions. If constrained, run the bypass line to spawn a v2 shell. This is typically used early in post-exploitation to enable script execution, such as loading offensive tools or running unsigned code. Save as a .ps1 file and invoke via `powershell -File script.ps1` if needed.

## Detection

- PowerShell event logs (ID 4103/4104) showing language mode queries or v2 launches.
- Process monitoring for `powershell.exe` with `-version 2` argument.
- Behavioral analytics detecting mode checks followed by version downgrades.

## Related

- [[procedures/Check-and-Bypass-PowerShell-Constrained-Language-Mode]]
