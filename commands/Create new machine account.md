---
id: c1ca3dc4-9329-4a3c-9ab9-d8243dbdb237
name: Create New Machine Account
type: command
executor: bash
data: 'powermad@windows> . .\Powermad.ps1

  powermad@windows> $password = ConvertTo-SecureString ''ComputerPassword'' -AsPlainText
  -Force

  powermad@windows> New-MachineAccount -MachineAccount "ControlledComputer" -Password
  $($password) -Domain "domain.local" -DomainController "DomainController.domain.local"
  -Verbose'
output: null
created_at: '2023-04-06T03:56:03.096209+00:00'
updated_at: '2023-04-10T20:26:11.555942+00:00'
---

# Create New Machine Account

```bash
powermad@windows> . .\Powermad.ps1
powermad@windows> $password = ConvertTo-SecureString 'ComputerPassword' -AsPlainText -Force
powermad@windows> New-MachineAccount -MachineAccount "ControlledComputer" -Password $($password) -Domain "domain.local" -DomainController "DomainController.domain.local" -Verbose
```


