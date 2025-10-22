---
id: 54e4b22f-fd15-44ca-ac9e-db5b7940c2b4
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:31.111611+00:00'
updated_at: '2023-04-10T20:38:05.487937+00:00'
---

# Code Snippet 54e4b22f

**Language**: ps1

```ps1
PS> $pass = ConvertTo-SecureString 'supersecurepassword' -AsPlainText -Force
PS> $cred = New-Object System.Management.Automation.PSCredential ('DOMAIN\Username', $pass)
```
