---
id: f7577401-5977-4544-9488-6b1d661f7342
name: Get user with specific string in Description attribute
type: command
executor: bash
data: Get-ADUser -Filter 'Description -like "*wtver*"' -Properties Description | select
  Name, Description
output: null
created_at: '2023-04-06T03:56:02.419468+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
---

# Get user with specific string in Description attribute

```bash
Get-ADUser -Filter 'Description -like "*wtver*"' -Properties Description | select Name, Description
```


