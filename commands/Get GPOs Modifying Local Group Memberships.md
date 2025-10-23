---
id: c722b4f8-26d5-4bab-908a-d32524f9291a
name: Get GPOs Modifying Local Group Memberships
type: command
executor: bash
data: Get-DomainGPOLocalGroup | Select-Object GPODisplayName, GroupName
output: null
created_at: '2023-04-06T03:56:02.229800+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
---

# Get GPOs Modifying Local Group Memberships

```bash
Get-DomainGPOLocalGroup | Select-Object GPODisplayName, GroupName
```


