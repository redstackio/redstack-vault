---
id: a1c9c047-cdd2-4ed3-8d61-d5ba17cb022d
type: code
language: Powershell
verified: false
created_at: '2023-05-24T07:54:08.675240+00:00'
updated_at: '2023-05-24T07:54:51.686182+00:00'
---

# Code Snippet a1c9c047

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


