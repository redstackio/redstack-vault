---
id: 5d94ecb7-83ca-4a13-bad3-e795b9838b84
name: Delete a Windows Service
type: command
executor: command_prompt
data: sc.exe delete $_SERVICE_NAME
output: 'C:\Windows\system32>sc.exe delete pwnSVC

  [SC] DeleteService SUCCESS'
created_at: '2020-04-28T21:10:21.095995+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Delete a Windows Service

```command_prompt
sc.exe delete $_SERVICE_NAME
```

## Expected Output

```
C:\Windows\system32>sc.exe delete pwnSVC
[SC] DeleteService SUCCESS
```


