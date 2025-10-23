---
id: b761ecd6-34e2-43a9-9f45-c3957e851486
name: Get all Azure AD users and select only their User Principal Name
type: command
executor: bash
data: Get-AzureADUser -All $true | select UserPrincipalName
output: null
created_at: '2023-05-23T19:33:22.164808+00:00'
updated_at: '2023-05-23T19:33:22.785549+00:00'
---

# Get all Azure AD users and select only their User Principal Name

```bash
Get-AzureADUser -All $true | select UserPrincipalName
```


