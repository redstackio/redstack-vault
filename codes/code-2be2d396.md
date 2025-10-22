---
id: 2be2d396-33ad-47b0-ab8e-8a523ef08656
type: code
language: Powershell
verified: false
created_at: '2023-05-24T07:13:54.138552+00:00'
updated_at: '2023-05-24T07:13:54.186427+00:00'
---

# Code Snippet 2be2d396

**Language**: Powershell

```powershell
# az cli - get tokens 
az account get-access-token 
az account get-access-token --resource-type aad-graph

# or Az
(Get-AzAccessToken -ResourceUrl https://graph.microsoft.com).Token
```
