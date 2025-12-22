---
type: command
executor: cmd
data: reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
output: null
platforms:
  - Windows
tags:
  - enumeration
  - startup
  - registry
verified: true
validated: true
---

# list-run-once-programs-registry-hkcu

## Command

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
```

## Description

Queries the HKCU RunOnce registry key to list programs set to run once at startup for the current user, useful for detecting persistence mechanisms.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce | Registry key for one-time startup programs | Built-in |

## Examples

### Basic Usage

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
```

### Advanced Usage

With value details:

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce /s
```

## Expected Output

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
    ProgramName    REG_SZ    C:\path\to\program.exe
```

Lists keys and values; empty if no entries.

## Related

- [[procedures/windows-processes-and-tasks-enumeration-for-privilege-escalation]]
