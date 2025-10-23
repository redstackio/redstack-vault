---
id: f41aca5f-9e27-46f2-b88a-716a7ae2c797
type: code
language: Powershell
verified: false
created_at: '2023-05-24T07:56:10.482578+00:00'
updated_at: '2023-05-30T13:38:04.009616+00:00'
---

# Code Snippet f41aca5f

**Language**: Powershell

```powershell
# Login using an Acess Token
PS C:\Tools> $token = 'eyJ0e..'
PS C:\Tools> Connect-AzAccount -AccessToken $token -AccountId <ACCOUNT-ID>

OR

# Login using an Access token and Graph Access Token
PS C:\Tools> $token = 'eyJ0eX..'
PS C:\Tools> $graphaccesstoken = 'eyJ0eX..'
PS C:\Tools> Connect-AzAccount -AccessToken $token -GraphAccessToken $graphaccesstoken -AccountId <ACCOUNT-ID>

# Access Azure Resources using the authenticated account
PS C:\Tools> Get-AzResource
```


