---
id: ca55cb17-69e8-492b-87cb-cde316928141
name: Create a Windows Service
type: command
executor: command_prompt
data: sc.exe create $_SERVICE_NAME binpath= "$_PATH\$_PROGRAM"
output: 'C:\Windows\system32>sc.exe create pwnSVC binpath= "C:\Windows\Tasks\runme.bat"

  [SC] CreateService SUCCESS'
created_at: '2020-04-28T21:10:21.094620+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Create a Windows Service

```command_prompt
sc.exe create $_SERVICE_NAME binpath= "$_PATH\$_PROGRAM"
```

## Expected Output

```
C:\Windows\system32>sc.exe create pwnSVC binpath= "C:\Windows\Tasks\runme.bat"
[SC] CreateService SUCCESS
```
