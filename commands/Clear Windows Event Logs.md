---
id: 2b05aa34-daea-4416-b5e1-20fb126b07ba
name: Clear Windows Event Logs
type: command
executor: bash
data: 'cmd.exe /c wevtutil.exe cl System

  cmd.exe /c wevtutil.exe cl Security'
output: null
created_at: '2023-04-06T03:56:27.717967+00:00'
updated_at: '2023-04-10T20:37:20.507449+00:00'
---

# Clear Windows Event Logs

```bash
cmd.exe /c wevtutil.exe cl System
cmd.exe /c wevtutil.exe cl Security
```


