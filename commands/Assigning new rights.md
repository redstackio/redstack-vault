---
id: 0d414f78-cc2f-4cf2-9145-10d80fd67ef4
name: Assigning new rights
type: command
executor: bash
data: Add-UserRights -Rights "SeLoadDriverPrivilege","SeDebugPrivilege" -Identity
  'Bobby' -GPOIdentity 'SuperSecureGPO'
output: null
created_at: '2023-04-06T03:56:03.664962+00:00'
updated_at: '2023-04-10T20:26:15.994624+00:00'
---

# Assigning new rights

```bash
Add-UserRights -Rights "SeLoadDriverPrivilege","SeDebugPrivilege" -Identity 'Bobby' -GPOIdentity 'SuperSecureGPO'
```


