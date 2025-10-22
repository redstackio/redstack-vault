---
id: ba94fedb-3317-4ef7-94e2-ae6b240eabdf
type: code
language: Powershell
verified: false
created_at: '2023-05-24T08:06:49.823477+00:00'
updated_at: '2023-05-24T08:08:13.420439+00:00'
---

# Code Snippet ba94fedb

**Language**: Powershell

```powershell
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
