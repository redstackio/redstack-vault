---
id: 80056f84-8ffc-45a7-be82-cd5a5ebb39ed
name: retrieve-aadinternals-access-token
type: command
executor: powershell
data: >-
  Install-Module AADInternals -Scope CurrentUser

  Import-Module AADInternals

  $token = (Get-AADIntAccessTokenForExchanging -ClientId
  "9bc3ab49-b65d-410a-85ad-de819febfddc" -Tenant "your.onmicrosoft.com"
  -Resource "https://your.sharepoint.com")
output: null
created_at: '2023-04-06T03:56:28.947816+00:00'
updated_at: '2023-10-10T20:37:31.881047+00:00'
platforms:
  - Windows
tags:
  - authentication
  - azure-ad
verified: true
validated: true
---

# retrieve-aadinternals-access-token

## Command

```powershell
Install-Module AADInternals -Scope CurrentUser
Import-Module AADInternals
$token = (Get-AADIntAccessTokenForExchanging -ClientId "9bc3ab49-b65d-410a-85ad-de819febfddc" -Tenant "your.onmicrosoft.com" -Resource "https://your.sharepoint.com")
```

## Description

This command installs the AADInternals PowerShell module if needed and retrieves an Azure AD access token for SharePoint using the token exchange flow. Use this when you have valid credentials to authenticate against the tenant.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ClientId | Azure AD app client ID for SharePoint (fixed: 9bc3ab49-b65d-410a-85ad-de819febfddc) | Yes |
| -Tenant | Target tenant ID (e.g., your.onmicrosoft.com) | Yes |
| -Resource | SharePoint resource URI | Yes |
| -Scope | Installation scope (CurrentUser avoids admin rights) | No |

## Examples

### Basic Usage

```powershell
Install-Module AADInternals -Scope CurrentUser
Import-Module AADInternals
$token = (Get-AADIntAccessTokenForExchanging -ClientId "9bc3ab49-b65d-410a-85ad-de819febfddc" -Tenant "contoso.onmicrosoft.com" -Resource "https://contoso.sharepoint.com")
Write-Output $token
```

### Advanced Usage

Prompt for credentials if needed:
```powershell
$creds = Get-Credential
$token = (Get-AADIntAccessTokenForExchanging -ClientId "9bc3ab49-b65d-410a-85ad-de819febfddc" -Tenant "contoso.onmicrosoft.com" -Resource "https://contoso.sharepoint.com" -Credential $creds)
```

## Expected Output

A string containing the JWT bearer token, e.g., "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9...". No errors if authentication succeeds; errors indicate invalid creds or tenant.

## Related

- [[procedures/Password-Looting-from-SharePoint-and-SMB-Shares]]
- [[tools/AADInternals]]
