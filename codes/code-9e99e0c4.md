---
id: 9e99e0c4-769d-4c6e-954e-a7d33e40193f
type: code
language: Powershell
verified: false
created_at: '2023-05-23T22:22:41.689760+00:00'
updated_at: '2023-05-23T22:26:37.952555+00:00'
---

# Code Snippet 9e99e0c4

**Language**: Powershell

```powershell
# az cli - get tokens 
az account get-access-token 
az account get-access-token --resource-type aad-graph

# or Az
(Get-AzAccessToken -ResourceUrl https://graph.microsoft.com).Token

# or KUDU Debug Console Powershell - System Assigned Managed Identity
$resourceURI = "https://storage.azure.com"
$tokenAuthURI = $env:IDENTITY_ENDPOINT + "?resource=$resourceURI&api-version=2019-08-01"
$tokenResponse = Invoke-RestMethod -Method Get -Headers @{"X-IDENTITY-HEADER"="$env:IDENTITY_HEADER"} -Uri $tokenAuthURI
$accessToken = $tokenResponse.access_token
$accessToken

# or KUDU Debug Console Powershell - User Assigned Managed Identity
# Include a client_id or principal_id
$resourceURI = "https://storage.azure.com/"
$client_id = "d5845093-6622-4827-ad6a-xxxxxxxxxx"
$tokenAuthURI = $env:IDENTITY_ENDPOINT + "?resource=$resourceURI&client_id=$client_id&api-version=2019-08-01"
$tokenResponse = Invoke-RestMethod -Method Get -Headers @{"X-IDENTITY-HEADER"="$env:IDENTITY_HEADER"} -Uri $tokenAuthURI
$accessToken = $tokenResponse.access_token
$accessToken
```


