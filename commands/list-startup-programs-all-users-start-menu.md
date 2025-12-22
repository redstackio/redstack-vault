---
type: command
executor: cmd
data: 'dir "C:\\Documents and Settings\\All Users\\Start Menu\\Programs\\Startup"'
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

# list-startup-programs-all-users-start-menu

## Command

```cmd
dir "C:\Documents and Settings\All Users\Start Menu\Programs\Startup"
```

## Description

Lists contents of the all-users Startup folder, identifying shortcuts that execute at boot for all users (note: legacy path for Windows XP/2003; use C:\ProgramData\... on modern systems).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "C:\Documents and Settings\All Users\Start Menu\Programs\Startup" | Path to all-users Startup directory | Yes |

## Examples

### Basic Usage

```cmd
dir "C:\Documents and Settings\All Users\Start Menu\Programs\Startup"
```

### Advanced Usage

Recursive list:

```cmd
dir /s "C:\Documents and Settings\All Users\Start Menu\Programs\Startup"
```

## Expected Output

```
 Volume in drive C is OS
 Directory of C:\Documents and Settings\All Users\Start Menu\Programs\Startup

04/06/2023  03:56 PM    <DIR>          .
               0 File(s)              0 bytes
```

Directory listing; check for .lnk files pointing to executables.

## Related

- [[procedures/windows-processes-and-tasks-enumeration-for-privilege-escalation]]
