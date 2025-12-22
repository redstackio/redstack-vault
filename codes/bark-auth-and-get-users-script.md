---
id: a989e7fc-3e40-4d17-bb65-87fcdba1ed3d
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:14.584434+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - auth
  - aad
  - enum
validated: true
---

# bark-auth-and-get-users-script

## Code

```powershell
. .\BARK.ps1
$MyRefreshTokenRequest = Get-AZRefreshTokenWithUsernamePassword -username "user@contoso.onmicrosoft.com" -password "MyVeryCoolPassword" -TenantID "contoso.onmicrosoft.com"
$MyMSGraphToken = Get-MSGraphTokenWithRefreshToken -RefreshToken $MyRefreshTokenRequest.refresh_token -TenantID "contoso.onmicrosoft.com"
$MyAADUsers = Get-AllAzureADUsers -Token $MyMSGraphToken.access_token -ShowProgress
```

## Description

This PowerShell script uses BARK to authenticate via username/password, obtain Microsoft Graph tokens, and enumerate all Azure AD users, providing a complete user directory for reconnaissance.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| username | Azure AD username | user@contoso.onmicrosoft.com |
| password | Account password | MyVeryCoolPassword |
| TenantID | Tenant domain or GUID | contoso.onmicrosoft.com |

## Usage

Save as .ps1 and execute in PowerShell after downloading BARK. Used in initial recon to identify admin users or targets for phishing. Requires BARK.ps1 in the same directory.

## Detection

- Monitor Graph API calls for unusual user enumeration (beta endpoint /users).
- Azure AD sign-in logs for app=00000003-0000-0000-c000-000000000000 (Graph).
- PowerShell script block logging showing BARK functions.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/BARK]]
