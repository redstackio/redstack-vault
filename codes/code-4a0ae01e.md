---
id: 4a0ae01e-fadd-4b12-97f6-21999a13d71b
type: code
language: Powershell
verified: false
created_at: '2023-05-24T07:13:54.138703+00:00'
updated_at: '2023-05-24T07:13:54.186427+00:00'
---

# Code Snippet 4a0ae01e

**Language**: Powershell

```powershell
# or KUDU Debug Console Powershell - System Assigned Managed Identity
$resourceURI = "https://storage.azure.com"
$tokenAuthURI = $env:IDENTITY_ENDPOINT + "?resource=$resourceURI&api-version=2019-08-01"
$tokenResponse = Invoke-RestMethod -Method Get -Headers @{"X-IDENTITY-HEADER"="$env:IDENTITY_HEADER"} -Uri $tokenAuthURI
$accessToken = $tokenResponse.access_token
$accessToken

```
