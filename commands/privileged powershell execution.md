---
id: 14691c01-ac7d-4863-b816-3ec84beab755
name: privileged powershell execution
type: command
executor: command_prompt
data: 'runas /user:hostname\Administrator /savecred "powershell -ExecutionPolicy Bypass
  -File C:\Users\security\AppData\Local\Temp\boom.ps1"

  '
output: null
created_at: '2020-07-14T18:15:08.367975+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# privileged powershell execution

```command_prompt
runas /user:hostname\Administrator /savecred "powershell -ExecutionPolicy Bypass -File C:\Users\security\AppData\Local\Temp\boom.ps1"

```


