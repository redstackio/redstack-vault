---
type: command
executor: cmd
data: >-
  REG QUERY "HKLM\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine" /v
  PowerShellVersion
output: null
platforms:
  - Windows
tags:
  - enumeration
  - powershell
verified: true
validated: true
---

# check-powershell-version

## Command

```cmd
REG QUERY "HKLM\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine" /v PowerShellVersion
```

## Description

Queries the Windows registry to retrieve the installed PowerShell version, useful for compatibility checks during enumeration or scripting in privilege escalation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKLM\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine | Registry path for PowerShell engine info | Built-in |
| /v PowerShellVersion | Specifies the value name to query | Yes |

## Examples

### Basic Usage

```cmd
REG QUERY "HKLM\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine" /v PowerShellVersion
```

### Advanced Usage

Run in a batch script to parse version:

```cmd
for /f "tokens=3" %%a in ('REG QUERY "HKLM\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine" /v PowerShellVersion ^| find "PowerShellVersion"') do echo Version: %%a
```

## Expected Output

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine    PowerShellVersion    REG_SZ    5.1.19041.1237
```

A successful query shows the version string; errors indicate no PowerShell installed or access denied.

## Related

- [[procedures/windows-processes-and-tasks-enumeration-for-privilege-escalation]]
