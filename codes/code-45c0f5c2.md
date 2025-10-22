---
id: 45c0f5c2-48c8-4207-bcb3-4df4246195c1
type: code
language: Powershell
verified: false
created_at: '2023-05-30T13:38:03.980187+00:00'
updated_at: '2023-05-30T13:47:18.351914+00:00'
---

# Code Snippet 45c0f5c2

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
