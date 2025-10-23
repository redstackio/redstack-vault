---
id: b6627471-cb7f-4971-b734-a65009c3a604
name: Enumerate Domain Group ACLs
type: command
executor: ''
data: Find-InterestingDomainAcl -ResolveGUIDs | ?{$_.IdentityReferenceName -match
  $GROUP_NAME}
output: null
created_at: '2023-01-12T07:34:23.268122+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Enumerate Domain Group ACLs

```bash
Find-InterestingDomainAcl -ResolveGUIDs | ?{$_.IdentityReferenceName -match $GROUP_NAME}
```


