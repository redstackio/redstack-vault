---
id: c358fe85-39f3-4882-8708-8263dcb99047
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:03.237855+00:00'
updated_at: '2023-04-10T20:26:35.780565+00:00'
---

# Code Snippet c358fe85

**Language**: Powershell

```powershell
smbmap -H 10.10.10.10                # null session
smbmap -H 10.10.10.10 -R             # recursive listing
smbmap -H 10.10.10.10 -u invaliduser # guest smb session
smbmap -H 10.10.10.10 -d "DOMAIN.LOCAL" -u "USERNAME" -p "Password123*"
```
