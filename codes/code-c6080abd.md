---
id: c6080abd-090a-4e1c-b46f-ce6c9fba7b41
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.253937+00:00'
updated_at: '2023-05-23T22:22:06.885681+00:00'
---

# Code Snippet c6080abd

**Language**: Powershell

```powershell
# az cli - get tokens 
az account get-access-token 
az account get-access-token --resource-type aad-graph
# or Az
(Get-AzAccessToken -ResourceUrl https://graph.microsoft.com).Token
# or from a managed identity using IDENTITY_HEADER and IDENTITY_ENDPOINT
```
