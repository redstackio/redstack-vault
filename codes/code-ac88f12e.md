---
id: ac88f12e-0ee0-467a-8a84-2a8e1c77b223
type: code
language: Powershell
verified: false
created_at: '2023-05-24T08:06:28.996772+00:00'
updated_at: '2023-05-24T08:06:49.831442+00:00'
---

# Code Snippet ac88f12e

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
