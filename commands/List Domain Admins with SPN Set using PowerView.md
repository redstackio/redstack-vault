---
id: e729fcd8-3c73-483a-abff-1559cbcb5685
name: List Domain Admins with SPN Set using PowerView
type: command
executor: ''
data: Get-NetUser -SPN | ?{$_.memberof -match 'Domain Admins'}
output: null
created_at: '2023-01-12T17:49:32.489952+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List Domain Admins with SPN Set using PowerView

```bash
Get-NetUser -SPN | ?{$_.memberof -match 'Domain Admins'}
```


