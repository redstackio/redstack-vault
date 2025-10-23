---
id: f7d47ba8-41a8-4c57-9e63-cb80e8ee3e13
type: code
language: Powershell
verified: false
created_at: '2023-05-24T08:06:49.823296+00:00'
updated_at: '2023-05-24T08:08:13.420255+00:00'
---

# Code Snippet f7d47ba8

**Language**: Powershell

```powershell
# Retrieve a list of subscriptions
$Token = 'eyJ0eX..'
$URI = 'https://management.azure.com/subscriptions/b3d2186f-0d10-4944-1c88-d7d853d36886/resources?api-version=2020-10-01'
$RequestParams = @{
 Method = 'GET'
 Uri = $URI
 Headers = @{
 'Authorization' = "Bearer $Token"
 }
}
(Invoke-RestMethod @RequestParams).value 

# List resources and check for runCommand privileges
$URI = 'https://management.azure.com/subscriptions/b3d2186f-0d10-4944-1c88-d7d853d36886/resourceGroups/<RG-NAME>/providers/Microsoft.Compute/virtualMachines/<RESOURCE/providers/Microsoft.Authorization/permissions?apiversion=2015-07-01'
```


