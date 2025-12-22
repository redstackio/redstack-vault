---
id: 90af7541-ea05-41b8-b635-f3403fc531a6
name: Load-PowerView-Bypass-Execution-Policy
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:23.962588+00:00'
updated_at: '2023-04-10T20:37:00.768331+00:00'
platforms:
  - Windows
tags:
  - powershell
  - powerview
  - execution-policy
validated: true
---

# Load-PowerView-Bypass-Execution-Policy

## Code

```ps1
powershell -EncodedCommand $encodedCommand
powershell -ep bypass ./PowerView.ps1

# Change execution policy
Set-Executionpolicy -Scope CurrentUser -ExecutionPolicy UnRestricted
Set-ExecutionPolicy Bypass -Scope Process
```

## Description

This PowerShell snippet provides multiple methods to load the PowerView reconnaissance module by bypassing execution policy restrictions. It includes encoded command execution, direct bypass invocation, and policy changes for user or process scope, enabling AD enumeration in restricted Windows environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `$encodedCommand` | Base64-encoded string for initial module import | `[Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes('Import-Module PowerView.ps1'))` |
| `./PowerView.ps1` | Local path to the PowerView script | `C:\temp\PowerView.ps1` |

## Usage

Save as a .ps1 file or execute inline during a compromised session. Use the encoded command first for stealth, fallback to bypass flag if needed, then adjust policy for persistent loads. Typically deployed after initial access to enable further discovery with PowerView cmdlets like Get-DomainUser.

## Detection

- PowerShell event logs showing Set-ExecutionPolicy calls or -ep bypass usage.
- EncodedCommand invocations in process creation events (Sysmon ID 1).
- Module loads for unsigned scripts via ScriptBlock logging.
- Network or file access to PowerView.ps1 downloads.

## Related

- [[procedures/Bypass-PowerShell-Execution-Policy-for-PowerView]]
- [[tools/PowerView]] (if documented)
