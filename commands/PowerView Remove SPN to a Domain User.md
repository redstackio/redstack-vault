---
id: 613ec3d3-fe39-4e2d-99e3-2b218aea3058
name: PowerView Remove SPN to a Domain User
type: command
executor: powershell
data: Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -Clear serviceprincipalname
output: PS C:\Users\dave\Documents> Set-DomainObject -Credential $Cred -Identity steve
  -Clear serviceprincipalname
created_at: '2020-06-25T20:16:48.076258+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerView Remove SPN to a Domain User

```powershell
Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -Clear serviceprincipalname
```

## Expected Output

```
PS C:\Users\dave\Documents> Set-DomainObject -Credential $Cred -Identity steve -Clear serviceprincipalname
```
