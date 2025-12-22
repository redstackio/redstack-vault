---
id: 4c87a9c7-3d08-4ebc-a26d-1ecfbfd7a12e
type: command
executor: powershell
data: >-
  . .\BARK.ps1 ; $MyRefreshTokenRequest = Get-AZRefreshTokenWithUsernamePassword
  -username "$_USERNAME" -password "$_PASSWORD" -TenantID "$_TENANT_ID" ;
  $MyMSGraphToken = Get-MSGraphTokenWithRefreshToken -RefreshToken
  $MyRefreshTokenRequest.refresh_token -TenantID "$_TENANT_ID" ; $MyAADUsers =
  Get-AllAzureADUsers -Token $MyMSGraphToken.access_token -ShowProgress
output: null
created_at: '2023-04-06T03:56:14.584511+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - aad
  - users
verified: true
validated: true
---

# bark-get-azure-ad-users

## Command

```powershell
. .\BARK.ps1 ; $MyRefreshTokenRequest = Get-AZRefreshTokenWithUsernamePassword -username "$_USERNAME" -password "$_PASSWORD" -TenantID "$_TENANT_ID" ; $MyMSGraphToken = Get-MSGraphTokenWithRefreshToken -RefreshToken $MyRefreshTokenRequest.refresh_token -TenantID "$_TENANT_ID" ; $MyAADUsers = Get-AllAzureADUsers -Token $MyMSGraphToken.access_token -ShowProgress
```

## Description

Full sequence to authenticate and enumerate all Azure AD users using BARK.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | AAD username | Yes |
| $_PASSWORD | Password | Yes |
| $_TENANT_ID | Tenant domain or ID | Yes |

## Examples

### Basic Usage

```powershell
. .\BARK.ps1 ; $MyRefreshTokenRequest = Get-AZRefreshTokenWithUsernamePassword -username "user@contoso.onmicrosoft.com" -password "MyVeryCoolPassword" -TenantID "contoso.onmicrosoft.com" ; $MyMSGraphToken = Get-MSGraphTokenWithRefreshToken -RefreshToken $MyRefreshTokenRequest.refresh_token -TenantID "contoso.onmicrosoft.com" ; $MyAADUsers = Get-AllAzureADUsers -Token $MyMSGraphToken.access_token -ShowProgress
```

## Expected Output

Array of user objects with progress bar.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/BARK]]
