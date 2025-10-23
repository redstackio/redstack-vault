---
id: ddd86e30-9eea-4bb0-bbe6-921bf53e7f6c
type: code
language: ''
verified: false
created_at: '2023-05-24T08:06:28.998411+00:00'
updated_at: '2023-05-24T08:06:49.831834+00:00'
---

# Code Snippet ddd86e30

```
# Retrieve a list of subscriptions
$Token = 'eyJ0eX..'
$URI = 'https://management.azure.com/subscriptions/b3d2186f-0d10-4944-1c88-d7d853d36886/resourceGroups/<RG-NAME>/providers/Microsoft.Compute/virtualMachines/<RESOURCE/providers/Microsoft.Authorization/permissions?apiversion=2015-07-01'
$RequestParams = @{
 Method = 'GET'
 Uri = $URI
 Headers = @{
 'Authorization' = "Bearer $Token"
 }
}
(Invoke-RestMethod @RequestParams).value 
```


