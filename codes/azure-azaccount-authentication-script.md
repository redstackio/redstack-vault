---
id: 156acadd-382d-4e1b-bbd5-88853049942d
name: azure-azaccount-authentication-script
type: code
language: powershell
verified: true
created_at: '2023-05-30T13:47:18.322022+00:00'
updated_at: '2023-05-30T13:47:19.181302+00:00'
platforms:
  - Windows
tags:
  - cloud-auth
  - azure
validated: true
---

# azure-azaccount-authentication-script

## Code

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

## Description

This PowerShell script snippet demonstrates authentication to Azure using managed identity access tokens via the Az module, either with a single ARM token or combined with a Graph token, followed by resource enumeration. It provides a quick way to establish and verify cloud access in a compromised environment.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $token | ARM access token | 'eyJ0eXAiOiJKV1Qi...' |
| $graphaccesstoken | Microsoft Graph access token | 'eyJ0eXAiOiJKV1Qi...' |
| <ACCOUNT-ID> | Managed identity object ID | '12345678-1234-1234-1234-123456789012' |

## Usage

Execute in a PowerShell session on a system with Az module installed, after obtaining tokens (e.g., via IMDS endpoint). Use the single-token path for basic ARM access or the OR path for Graph-integrated sessions. Follow with Get-AzResource to confirm access and enumerate.

## Detection

- PowerShell execution logs showing Connect-AzAccount with -AccessToken.
- Azure AD sign-in logs for managed identity token redemptions from unusual IPs.
- Network traffic to login.microsoftonline.com with JWT validation.

## Related

- [[procedures/Authenticate-to-Azure-Using-Managed-Identity-Access-Tokens]]
- [[tools/Az-PowerShell-Module]]
