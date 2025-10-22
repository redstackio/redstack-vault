---
id: 1f7a760b-b104-4466-81b0-0fd6d44a2468
name: Retrieve user in Azure AD
type: command
executor: bash
data: Get-AzureADUser -ObjectId <RoleMemberInfo.Id> | fl
output: null
created_at: '2023-04-06T03:56:15.848018+00:00'
updated_at: '2023-04-10T20:19:31.152057+00:00'
---

# Retrieve user in Azure AD

```bash
Get-AzureADUser -ObjectId <RoleMemberInfo.Id> | fl
```
