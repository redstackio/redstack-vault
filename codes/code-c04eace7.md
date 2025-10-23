---
id: c04eace7-a485-4a41-94cf-fa4eb6e17086
type: code
language: Powershell
verified: false
created_at: '2023-05-24T08:08:13.412672+00:00'
updated_at: '2023-05-24T08:08:13.433836+00:00'
---

# Code Snippet c04eace7

**Language**: Powershell

```powershell
# Check for runCommand privileges
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


