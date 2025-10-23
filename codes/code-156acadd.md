---
id: 156acadd-382d-4e1b-bbd5-88853049942d
type: code
language: Powershell
verified: false
created_at: '2023-05-30T13:47:18.322022+00:00'
updated_at: '2023-05-30T13:47:19.181302+00:00'
---

# Code Snippet 156acadd

**Language**: Powershell

```powershell
# Login using an Access Token
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


