---
id: 301c0647-3342-4f78-8088-7ec8e479de1a
name: Set user password in Azure AD
type: command
executor: bash
data: (Get-AzureADUser -All $true | ?{$_.UserPrincipalName -eq "<Username>@<TENANT
  NAME>.onmicrosoft.com"}).ObjectId | SetAzureADUserPassword -Password $Password -Verbose
output: null
created_at: '2023-04-06T03:56:15.848123+00:00'
updated_at: '2023-04-10T20:19:31.152057+00:00'
---

# Set user password in Azure AD

```bash
(Get-AzureADUser -All $true | ?{$_.UserPrincipalName -eq "<Username>@<TENANT NAME>.onmicrosoft.com"}).ObjectId | SetAzureADUserPassword -Password $Password -Verbose
```
