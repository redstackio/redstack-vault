---
id: 3144595e-1d68-49f7-b353-0acb0062bf94
name: find-lsass-pid
type: command
executor: cmd
data: tasklist /fi "imagename eq lsass.exe"
output: null
created_at: '2023-04-06T03:56:27.177120+00:00'
updated_at: '2023-04-10T20:37:14.787792+00:00'
platforms:
  - Windows
tags:
  - discovery
  - process
verified: true
validated: true
---

# find-lsass-pid

## Command

```cmd
tasklist /fi "imagename eq lsass.exe"
```

## Description

This command queries the Windows task list to find the process ID (PID) of lsass.exe, the Local Security Authority process that handles authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /fi "imagename eq lsass.exe" | Filters the tasklist to show only processes named lsass.exe | Yes |

## Examples

### Basic Usage

```cmd
tasklist /fi "imagename eq lsass.exe"
```

## Expected Output

```
Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============ 
lsass.exe                      1234 Services                   0    145,280 K
```

Extract the PID (e.g., 1234) for use in dumping commands.

## Related

- [[procedures/windows-lsass-mini-dump-for-mimikatz]]
