---
id: a989e7fc-3e40-4d17-bb65-87fcdba1ed3d
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:14.584434+00:00'
updated_at: '2023-04-10T20:19:39.811529+00:00'
---

# Code Snippet a989e7fc

**Language**: ps1

```ps1
. .\BARK.ps1
$MyRefreshTokenRequest = Get-AZRefreshTokenWithUsernamePassword -username "user@contoso.onmicrosoft.com" -password "MyVeryCoolPassword" -TenantID "contoso.onmicrosoft.com"
$MyMSGraphToken = Get-MSGraphTokenWithRefreshToken -RefreshToken $MyRefreshTokenRequest.refresh_token -TenantID "contoso.onmicrosoft.com"
$MyAADUsers = Get-AllAzureADUsers -Token $MyMSGraphToken.access_token -ShowProgress
```


