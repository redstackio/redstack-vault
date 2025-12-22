---
id: 789a6fe0-48da-4e4f-8107-a82c4bbbc188
name: connect-azaccount-with-access-token-and-graph-token
type: command
executor: powershell
data: >-
  Connect-AzAccount -AccessToken $token -GraphAccessToken $graphToken -AccountId
  $_ACCOUNT_ID
output: null
created_at: '2023-05-30T13:47:18.323598+00:00'
updated_at: '2023-05-30T13:47:19.298036+00:00'
platforms:
  - Windows
tags:
  - cloud-auth
  - azure
  - graph
verified: true
validated: true
---

# connect-azaccount-with-access-token-and-graph-token

## Command

```powershell
Connect-AzAccount -AccessToken $token -GraphAccessToken $graphToken -AccountId $_ACCOUNT_ID
```

## Description

Establishes an Azure authentication context using both an ARM access token and a Microsoft Graph access token, allowing seamless operations across resource management and directory services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-AccessToken` | JWT for Azure Resource Manager ($token) | Yes |
| `-GraphAccessToken` | JWT for Microsoft Graph ($graphToken) | Yes |
| `-AccountId` | Managed identity object ID (placeholder: $_ACCOUNT_ID) | Yes |

## Examples

### Basic Usage

```powershell
$token = 'eyJ0eXAiOiJKV1Qi...'
$graphToken = 'eyJ0eXAiOiJKV1Qi...'
Connect-AzAccount -AccessToken $token -GraphAccessToken $graphToken -AccountId '12345678-1234-1234-1234-123456789012'
```

### Advanced Usage

Validate Graph access post-connection:

```powershell
Get-AzContext | Select-Object -ExpandProperty GraphToken
```

## Expected Output

Similar to single-token auth, but with Graph enabled: Confirms both scopes. Errors if tokens have mismatched audiences (e.g., Graph token not for https://graph.microsoft.com).

## Related

- [[commands/connect-azaccount-with-access-token]]
- [[procedures/Authenticate-to-Azure-Using-Managed-Identity-Access-Tokens]]
