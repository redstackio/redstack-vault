---
id: d422ddb2-67e1-46a7-a17a-d759c01106ee
name: Meterpreter List Running Processes
type: command
executor: metasploit
data: ps
output: "meterpreter > ps \n\nProcess List\n============\n\n PID   PPID  Name    \
  \                Arch  Session  User                      Path\n ---   ----  ----\
  \                    ----  -------  ----                      ---- \n\n 516   492\
  \   csrss.exe               x64   1\n 600   492   winlogon.exe            x64  \
  \ 1        NT AUTHORITY\\SYSTEM C:\\Windows\\System32\\winlogon.exe\n 644   500\
  \   services.exe            x64   0\n 668   500   lsass.exe               x64  \
  \ 0        NT AUTHORITY\\SYSTEM           C:\\Windows\\System32\\lsass.exe\n 772\
  \   644   svchost.exe             x64   0        NT AUTHORITY\\SYSTEM          \
  \ C:\\Windows\\System32\\svchost.exe\n 792   600   fontdrvhost.exe         x64 \
  \  1        Font Driver Host\\UMFD-1       C:\\Windows\\System32\\fontdrvhost.exe\n\
  \ 800   500   fontdrvhost.exe         x64   0        Font Driver Host\\UMFD-0  \
  \     C:\\Windows\\System32\\fontdrvhost.exe\n 832   644   svchost.exe         \
  \    x64   0        NT AUTHORITY\\SYSTEM           C:\\Windows\\System32\\svchost.exe\n\
  \ ...\n..."
created_at: '2019-11-14T01:00:13.488979+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Meterpreter List Running Processes

```metasploit
ps
```

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


