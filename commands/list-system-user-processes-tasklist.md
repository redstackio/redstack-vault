---
type: command
executor: cmd
data: tasklist /v /fi "username eq system"
output: null
platforms:
  - Windows
tags:
  - enumeration
  - processes
verified: true
validated: true
---

# list-system-user-processes-tasklist

## Command

```cmd
tasklist /v /fi "username eq system"
```

## Description

Lists all processes running under the SYSTEM user account with verbose details, aiding in identifying elevated processes for potential exploitation in privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /v | Verbose mode: shows PID, session, memory, and command line | Yes |
| /fi "username eq system" | Filter: only processes where username equals 'system' | Yes |

## Examples

### Basic Usage

```cmd
tasklist /v /fi "username eq system"
```

### Advanced Usage

Export to file:

```cmd
tasklist /v /fi "username eq system" > system_processes.txt
```

## Expected Output

```
Image Name                     PID Session Name        Session#    Mem Usage             Status        User Name               CPU Time    Window Title
========================= ======== ================ =========== ============ ============== ========== ================ ================
svchost.exe                    1234 Services                   0     15,872 K      Running        NT AUTHORITY\SYSTEM      0:00:00
lsass.exe                      5678 Console                    1     12,345 K      Running        NT AUTHORITY\SYSTEM      0:01:23
```

Table of SYSTEM processes; success if processes listed without 'Access Denied'.

## Related

- [[procedures/windows-processes-and-tasks-enumeration-for-privilege-escalation]]
