---
id: 37ec76c0-b447-4c25-9c34-2bd1bb0ed8b9
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.282834+00:00'
updated_at: '2023-05-24T07:54:08.720862+00:00'
---

# Code Snippet 37ec76c0

**Language**: Powershell

```powershell
PS C:\Tools> $token = 'eyJ0e..'
PS C:\Tools> Connect-AzAccount -AccessToken $token -AccountId <ACCOUNT-ID>

# Access Token and Graph Token
PS C:\Tools> $token = 'eyJ0eX..'
PS C:\Tools> $graphaccesstoken = 'eyJ0eX..'
PS C:\Tools> Connect-AzAccount -AccessToken $token -GraphAccessToken $graphaccesstoken -AccountId <ACCOUNT-ID>
PS C:\Tools> Get-AzResource
# ERROR: 'this.Client.SubscriptionId' cannot be null.
# ---> The managed identity has no rights on any of the Azure resources. Switch to to GraphAPI
```
