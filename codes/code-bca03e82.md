---
id: bca03e82-95df-4398-9a6a-aa7561870cbc
type: code
language: Powershell
verified: false
created_at: '2023-05-24T07:54:51.644300+00:00'
updated_at: '2023-05-24T07:56:10.512701+00:00'
---

# Code Snippet bca03e82

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
