---
id: 5a0e4b09-75e4-4ecd-8c0b-910aa2cd4aa3
name: Get all properties of a specific user
type: command
executor: bash
data: Get-ADUser -Filter * -Identity <user> -Properties *
output: null
created_at: '2023-04-06T03:56:02.419419+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
---

# Get all properties of a specific user

```bash
Get-ADUser -Filter * -Identity <user> -Properties *
```
