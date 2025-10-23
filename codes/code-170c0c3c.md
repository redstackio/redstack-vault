---
id: 170c0c3c-0a41-4d5e-bb2d-92ce0610b5fd
type: code
language: Powershell
verified: false
created_at: '2023-05-24T08:08:13.412352+00:00'
updated_at: '2023-05-24T08:08:13.433836+00:00'
---

# Code Snippet 170c0c3c

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


