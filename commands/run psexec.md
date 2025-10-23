---
id: c235d3b7-4cf0-4968-ba45-ea570b38efd7
name: run psexec
type: command
executor: bash
data: '.\PsExec.exe -accepteula \\<remote_hostname> cmd

  PsExec64.exe \\remote_hostname> -u <username> -p <password> shell64.exe

  '
output: null
created_at: '2020-07-14T18:14:45.854406+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# run psexec

```bash
.\PsExec.exe -accepteula \\<remote_hostname> cmd
PsExec64.exe \\remote_hostname> -u <username> -p <password> shell64.exe

```


