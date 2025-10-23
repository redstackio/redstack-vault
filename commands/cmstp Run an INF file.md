---
id: b5428658-adfc-4265-be49-f8c7a295a246
name: cmstp Run an INF file
type: command
executor: command_prompt
data: cmstp.exe /ni /s C:\$_DEST_DIR\$_FILE_NAME.inf
output: C:\>cmstp.exe /ni /s C:\Windows\Tasks\pwn.inf
created_at: '2019-11-20T19:04:07.104296+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# cmstp Run an INF file

```command_prompt
cmstp.exe /ni /s C:\$_DEST_DIR\$_FILE_NAME.inf
```

## Expected Output

```
C:\>cmstp.exe /ni /s C:\Windows\Tasks\pwn.inf
```


