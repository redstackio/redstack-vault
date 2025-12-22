---
id: 31bcb7c2-3bfd-4831-81f0-6c5779931feb
name: retrieve-snaffpoint-bearer-token
type: command
executor: powershell
data: '$token = (.\GetBearerToken.exe https://your.sharepoint.com)'
output: null
created_at: '2023-04-06T03:56:28.947752+00:00'
updated_at: '2023-10-10T20:37:31.881047+00:00'
platforms:
  - Windows
tags:
  - authentication
  - sharepoint
verified: true
validated: true
---

# retrieve-snaffpoint-bearer-token

## Command

```powershell
$token = (.\GetBearerToken.exe https://your.sharepoint.com)
```

## Description

This command uses the GetBearerToken.exe utility bundled with SnaffPoint to fetch a bearer token for SharePoint access. It prompts for credentials interactively and is simpler for quick token retrieval.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://your.sharepoint.com | Target SharePoint site URL | Yes |

## Examples

### Basic Usage

```powershell
$token = (.\GetBearerToken.exe https://contoso.sharepoint.com)
Write-Output $token
```

### Advanced Usage

Run from SnaffPoint directory:
```powershell
cd C:\Tools\SnaffPoint
$token = (.\GetBearerToken.exe https://contoso.sharepoint.com)
```

## Expected Output

Bearer token string assigned to $token, e.g., "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9...". Success if no prompt errors; failure if invalid URL or creds.

## Related

- [[procedures/Password-Looting-from-SharePoint-and-SMB-Shares]]
- [[tools/SnaffPoint]]
