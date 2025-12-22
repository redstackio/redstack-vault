---
type: command
executor: cmd
data: reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
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

# list-startup-programs-registry-hkcu

## Command

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

## Description

Queries the HKCU Run registry key to list user-specific startup programs that execute at logon.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKCU\Software\Microsoft\Windows\CurrentVersion\Run | Registry key for user startup programs | Built-in |

## Examples

### Basic Usage

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

### Advanced Usage

Export values:

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run /s > run_keys.txt
```

## Expected Output

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
    MyApp    REG_SZ    C:\path\to\app.exe
```

Registry entries; values point to executables for review.

## Related

- [[procedures/windows-processes-and-tasks-enumeration-for-privilege-escalation]]
