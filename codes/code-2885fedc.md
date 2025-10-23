---
id: 2885fedc-4c44-4794-b652-c520022ccf63
type: code
language: Powershell
verified: false
created_at: '2023-05-24T08:00:06.061040+00:00'
updated_at: '2023-05-24T08:06:29.008700+00:00'
---

# Code Snippet 2885fedc

**Language**: Powershell

```powershell
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

# List resources and check for runCommand privileges
$URI = 'https://management.azure.com/subscriptions/b413826f-108d-4049-8c11-d52d5d388768/resources?api-version=2020-10-01'
$URI = 'https://management.azure.com/subscriptions/b413826f-108d-4049-8c11-d52d5d388768/resourceGroups/<RG-NAME>/providers/Microsoft.Compute/virtualMachines/<RESOURCE/providers/Microsoft.Authorization/permissions?apiversion=2015-07-01'
```


