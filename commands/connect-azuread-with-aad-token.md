---
id: a3bf5def-a02e-44f4-bcd3-75a5876eb51b
name: connect-azuread-with-aad-token
type: command
executor: powershell
data: >-
  Connect-AzureAD -AadAccessToken $AADToken -TenantId $_TENANT_ID -AccountId
  $_ACCOUNT_ID
output: null
created_at: '2023-05-30T13:47:18.322713+00:00'
updated_at: '2023-05-30T13:47:19.298036+00:00'
platforms:
  - Windows
tags:
  - cloud-auth
  - azuread
verified: true
validated: true
---

# connect-azuread-with-aad-token

## Command

```powershell
Connect-AzureAD -AadAccessToken $AADToken -TenantId $_TENANT_ID -AccountId $_ACCOUNT_ID
```

## Description

Authenticates to Azure AD using a provided AAD access token, tenant ID, and account ID for directory operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-AadAccessToken` | AAD JWT token ($AADToken) | Yes |
| `-TenantId` | Azure AD tenant GUID (placeholder: $_TENANT_ID) | Yes |
| `-AccountId` | Account object ID (placeholder: $_ACCOUNT_ID) | Yes |

## Examples

### Basic Usage

```powershell
Connect-AzureAD -AadAccessToken $AADToken -TenantId 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' -AccountId '12345678-1234-1234-1234-123456789012'
```

### Advanced Usage

With output capture:

```powershell
$result = Connect-AzureAD -AadAccessToken $AADToken -TenantId $_TENANT_ID -AccountId $_ACCOUNT_ID; $result.Account
```

## Expected Output

"Welcome To Azure AD PowerShell" or context details. Test with Get-AzureADCurrentSessionTenantId. Errors: Invalid tenant or token audience mismatch.

## Related

- [[commands/set-aadtoken-variable]]
- [[procedures/Authenticate-to-Azure-Using-Managed-Identity-Access-Tokens]]
