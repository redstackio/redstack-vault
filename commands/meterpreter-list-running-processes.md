---
id: d422ddb2-67e1-46a7-a17a-d759c01106ee
name: meterpreter-list-running-processes
type: command
executor: metasploit
data: ps
output: |-
  meterpreter > ps 

  Process List
  ============

   PID   PPID  Name                    Arch  Session  User                      Path
   ---   ----  ----                    ----  -------  ----                      ---- 

   516   492   csrss.exe               x64   1
   600   492   winlogon.exe            x64   1        NT AUTHORITY\SYSTEM C:\Windows\System32\winlogon.exe
   644   500   services.exe            x64   0
   668   500   lsass.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\lsass.exe
   772   644   svchost.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
   792   600   fontdrvhost.exe         x64   1        Font Driver Host\UMFD-1       C:\Windows\System32\fontdrvhost.exe
   800   500   fontdrvhost.exe         x64   0        Font Driver Host\UMFD-0       C:\Windows\System32\fontdrvhost.exe
   832   644   svchost.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
   ...
  ...
created_at: '2019-11-14T01:00:13.488979+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - meterpreter
  - process-enumeration
verified: true
validated: true
---

# Meterpreter List Running Processes

## Command

```metasploit
ps
```

## Description

This Meterpreter command enumerates all running processes on the target Windows system, displaying PID, parent PID, name, architecture (x86/x64), session, user, and path. It is essential for identifying migration targets during post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; lists all processes | No |

## Examples

### Basic Usage

```metasploit
ps
```

Run within an active Meterpreter session to view the process table.

### Advanced Usage

Pipe output for filtering: `ps | grep svchost` (though Meterpreter ps supports basic filtering via options like `ps -A` for all users).

## Expected Output

```
meterpreter > ps 

Process List
============

 PID   PPID  Name                    Arch  Session  User                      Path
 ---   ----  ----                    ----  -------  ----                      ---- 

 516   492   csrss.exe               x64   1
 600   492   winlogon.exe            x64   1        NT AUTHORITY\SYSTEM C:\Windows\System32\winlogon.exe
 644   500   services.exe            x64   0
 668   500   lsass.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\lsass.exe
 772   644   svchost.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 792   600   fontdrvhost.exe         x64   1        Font Driver Host\UMFD-1       C:\Windows\System32\fontdrvhost.exe
 800   500   fontdrvhost.exe         x64   0        Font Driver Host\UMFD-0       C:\Windows\System32\fontdrvhost.exe
 832   644   svchost.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 ...
...
```

Look for 'x64' under Arch to identify 64-bit processes.

## Related

- [[commands/meterpreter-migrate-to-process]]
- [[procedures/upgrade-windows-meterpreter-x32-to-x64]]
