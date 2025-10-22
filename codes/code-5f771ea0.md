---
id: 5f771ea0-40b4-4d94-b822-71fbb1d1e514
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:03.096811+00:00'
updated_at: '2023-04-10T20:26:11.554516+00:00'
---

# Code Snippet 5f771ea0

**Language**: ps1

```ps1
impacket@linux> getTGT.py -dc-ip 'DomainController.domain.local' 'domain.local'/'DomainController':'ComputerPassword'

cmd@windows> Rubeus.exe asktgt /user:"DomainController" /password:"ComputerPassword" /domain:"domain.local" /dc:"DomainController.domain.local" /nowrap
```
