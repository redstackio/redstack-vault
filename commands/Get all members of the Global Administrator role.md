---
id: b9a5bdf2-fbbf-4992-82c4-297e83094599
name: Get all members of the Global Administrator role
type: command
executor: bash
data: Get-AzureADDirectoryRole -Filter "DisplayName eq 'Global Administrator'" | Get-AzureADDirectoryRoleMember
output: null
created_at: '2023-05-23T19:33:22.167812+00:00'
updated_at: '2023-05-23T19:33:22.785549+00:00'
---

# Get all members of the Global Administrator role

```bash
Get-AzureADDirectoryRole -Filter "DisplayName eq 'Global Administrator'" | Get-AzureADDirectoryRoleMember
```


