---
id: a73cdd95-4848-40ec-97d1-4ec5e3ea5292
name: Tasklist.exe List Running Processes
type: command
executor: command_prompt
data: tasklist.exe
output: 'C:\>tasklist.exe


  Image Name                     PID Session Name        Session#    Mem Usage

  ========================= ======== ================ =========== ============

  System Idle Process              0 Services                   0          8 K

  System                           4 Services                   0        140 K

  Registry                        88 Services                   0     70,192 K

  smss.exe                       336 Services                   0      1,060 K

  csrss.exe                      440 Services                   0      4,884 K

  wininit.exe                    512 Services                   0      6,044 K

  firefox.exe                   1724 Console                    1    111,388 K'
created_at: '2020-01-02T18:45:14.100849+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Tasklist.exe List Running Processes

```command_prompt
tasklist.exe
```

## Expected Output

```
C:\>tasklist.exe

Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0          8 K
System                           4 Services                   0        140 K
Registry                        88 Services                   0     70,192 K
smss.exe                       336 Services                   0      1,060 K
csrss.exe                      440 Services                   0      4,884 K
wininit.exe                    512 Services                   0      6,044 K
firefox.exe                   1724 Console                    1    111,388 K
```


