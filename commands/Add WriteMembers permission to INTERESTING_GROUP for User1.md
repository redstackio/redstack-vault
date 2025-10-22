---
id: 1cf96d68-f017-4582-b4ec-960d2136c8b9
name: Add WriteMembers permission to INTERESTING_GROUP for User1
type: command
executor: bash
data: Add-DomainObjectAcl -TargetIdentity "INTERESTING_GROUP" -Rights WriteMembers
  -PrincipalIdentity User1
output: null
created_at: '2023-04-06T03:56:06.850472+00:00'
updated_at: '2023-04-10T20:36:10.633986+00:00'
---

# Add WriteMembers permission to INTERESTING_GROUP for User1

```bash
Add-DomainObjectAcl -TargetIdentity "INTERESTING_GROUP" -Rights WriteMembers -PrincipalIdentity User1
```
