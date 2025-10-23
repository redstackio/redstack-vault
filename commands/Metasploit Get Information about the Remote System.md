---
id: aabb688b-3b56-4089-ad5c-09a145e0e215
name: Metasploit Get Information about the Remote System
type: command
executor: metasploit
data: sysinfo
output: "meterpreter > ps\n\nProcess List\n============\n\n PID   PPID  Name     \
  \          Arch  Session  User                          Path\n ---   ----  ----\
  \               ----  -------  ----                          ----\n 0     0    \
  \ [System Process]                                                \n 4     0   \
  \  System             x64   0                                      \n 268   4  \
  \   smss.exe           x64   0        NT AUTHORITY\\SYSTEM           \\SystemRoot\\\
  System32\\smss.exe\n 304   460   svchost.exe        x64   0        NT AUTHORITY\\\
  SYSTEM           C:\\Windows\\system32\\svchost.exe\n 340   332   csrss.exe    \
  \      x64   0        NT AUTHORITY\\SYSTEM           C:\\Windows\\system32\\csrss.exe\n\
  \ 376   332   wininit.exe        x64   0        NT AUTHORITY\\SYSTEM           C:\\\
  Windows\\system32\\wininit.exe\n..."
created_at: '2020-07-09T00:23:35.322215+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Get Information about the Remote System

```metasploit
sysinfo
```

## Expected Output

```
meterpreter > ps

Process List
============

 PID   PPID  Name               Arch  Session  User                          Path
 ---   ----  ----               ----  -------  ----                          ----
 0     0     [System Process]                                                
 4     0     System             x64   0                                      
 268   4     smss.exe           x64   0        NT AUTHORITY\SYSTEM           \SystemRoot\System32\smss.exe
 304   460   svchost.exe        x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\svchost.exe
 340   332   csrss.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 376   332   wininit.exe        x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\wininit.exe
...
```


