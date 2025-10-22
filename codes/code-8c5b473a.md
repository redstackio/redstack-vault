---
id: 8c5b473a-1cbc-479a-b958-4bb3ad504757
type: code
language: Powershell
verified: false
created_at: '2023-05-24T08:06:49.823189+00:00'
updated_at: '2023-05-24T08:08:13.420058+00:00'
---

# Code Snippet 8c5b473a

**Language**: Powershell

```powershell
# Retrieve a list of subscriptions
$Token = 'eyJ0eX..'
$URI = 'https://management.azure.com/subscriptions?api-version=2020-01-01'
# $URI = 'https://graph.microsoft.com/v1.0/applications'
$RequestParams = @{
 Method = 'GET'
 Uri = $URI
 Headers = @{
 'Authorization' = "Bearer $Token"
 }
}
(Invoke-RestMethod @RequestParams).value 
```
