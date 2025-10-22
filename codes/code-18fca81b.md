---
id: 18fca81b-effd-4fc0-8767-67a54725c3a3
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:02.419367+00:00'
updated_at: '2023-04-10T20:36:08.326426+00:00'
---

# Code Snippet 18fca81b

**Language**: Powershell

```powershell
Get-ADUser -Filter * -Identity <user> -Properties *

#Get a specific "string" on a user's attribute
Get-ADUser -Filter 'Description -like "*wtver*"' -Properties Description | select Name, Description
```
