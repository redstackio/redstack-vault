---
id: d55b1a15-9efe-4387-b217-af9d7d09afc5
name: PowerView Reset a Domain User's Password
type: command
executor: powershell
data: Set-DomainUserPassword -Identity $_TARGET_USER -AccountPassword $NewPassword
  -Credential $Cred
output: PS C:\Users\Bob > Set-DomainUserPassword -Identity alice -AccountPassword
  $NewPassword -Credential $Cred
created_at: '2020-06-25T22:16:45.303287+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerView Reset a Domain User's Password

```powershell
Set-DomainUserPassword -Identity $_TARGET_USER -AccountPassword $NewPassword -Credential $Cred
```

## Expected Output

```
PS C:\Users\Bob > Set-DomainUserPassword -Identity alice -AccountPassword $NewPassword -Credential $Cred
```


