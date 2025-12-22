---
type: command
executor: cmd
data: 'dir "C:\\Documents and Settings\\%username%\\Start Menu\\Programs\\Startup"'
output: null
platforms:
  - Windows
tags:
  - enumeration
  - startup
  - filesystem
verified: true
validated: true
---

# list-startup-programs-current-user-start-menu

## Command

```cmd
dir "C:\Documents and Settings\%username%\Start Menu\Programs\Startup"
```

## Description

Lists contents of the current user's Startup folder for user-specific autostart programs (legacy path; modern: %APPDATA%\Microsoft\Windows\Start Menu\...).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "C:\Documents and Settings\%username%\Start Menu\Programs\Startup" | Path to user Startup directory (%username% expands automatically) | Yes |

## Examples

### Basic Usage

```cmd
dir "C:\Documents and Settings\%username%\Start Menu\Programs\Startup"
```

### Advanced Usage

With details:

```cmd
dir /a "C:\Documents and Settings\%username%\Start Menu\Programs\Startup"
```

## Expected Output

```
 Directory of C:\Documents and Settings\user\Start Menu\Programs\Startup

04/06/2023  03:56 PM    <DIR>          .
               0 File(s)              0 bytes
```

Shows user shortcuts; inspect targets for malicious entries.

## Related

- [[procedures/windows-processes-and-tasks-enumeration-for-privilege-escalation]]
