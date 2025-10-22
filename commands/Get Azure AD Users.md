---
id: 4c87a9c7-3d08-4ebc-a26d-1ecfbfd7a12e
name: Get Azure AD Users
type: command
executor: bash
data: '. .\BARK.ps1

  $MyRefreshTokenRequest = Get-AZRefreshTokenWithUsernamePassword -username "user@contoso.onmicrosoft.com"
  -password "MyVeryCoolPassword" -TenantID "contoso.onmicrosoft.com"

  $MyMSGraphToken = Get-MSGraphTokenWithRefreshToken -RefreshToken $MyRefreshTokenRequest.refresh_token
  -TenantID "contoso.onmicrosoft.com"

  $MyAADUsers = Get-AllAzureADUsers -Token $MyMSGraphToken.access_token -ShowProgress'
output: null
created_at: '2023-04-06T03:56:14.584511+00:00'
updated_at: '2023-04-10T20:19:39.807633+00:00'
---

# Get Azure AD Users

```bash
. .\BARK.ps1
$MyRefreshTokenRequest = Get-AZRefreshTokenWithUsernamePassword -username "user@contoso.onmicrosoft.com" -password "MyVeryCoolPassword" -TenantID "contoso.onmicrosoft.com"
$MyMSGraphToken = Get-MSGraphTokenWithRefreshToken -RefreshToken $MyRefreshTokenRequest.refresh_token -TenantID "contoso.onmicrosoft.com"
$MyAADUsers = Get-AllAzureADUsers -Token $MyMSGraphToken.access_token -ShowProgress
```
