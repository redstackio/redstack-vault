---
id: d6943eee-3957-4d92-8c7a-ac877e8b280c
name: Get Azure CLI Tokens
type: command
executor: bash
data: "# az cli - get tokens \naz account get-access-token \naz account get-access-token\
  \ --resource-type aad-graph\n# or Az\n(Get-AzAccessToken -ResourceUrl https://graph.microsoft.com).Token\n\
  # or from a managed identity using IDENTITY_HEADER and IDENTITY_ENDPOINT"
output: null
created_at: '2023-05-24T07:13:54.139549+00:00'
updated_at: '2023-05-24T07:13:54.186015+00:00'
---

# Get Azure CLI Tokens

```bash
# az cli - get tokens 
az account get-access-token 
az account get-access-token --resource-type aad-graph
# or Az
(Get-AzAccessToken -ResourceUrl https://graph.microsoft.com).Token
# or from a managed identity using IDENTITY_HEADER and IDENTITY_ENDPOINT
```
