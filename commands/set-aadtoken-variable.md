---
id: 66b4a8a1-7c96-4955-adbe-163e516d7ca7
name: set-aadtoken-variable
type: command
executor: powershell
data: >-
  $AADToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...' # Replace with
  actual AAD token
output: null
created_at: '2023-05-30T13:47:18.323455+00:00'
updated_at: '2023-05-30T13:47:19.298036+00:00'
platforms:
  - Windows
tags:
  - cloud-auth
  - azuread
verified: true
validated: true
---

# set-aadtoken-variable

## Command

```powershell
$AADToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...' # Replace with actual AAD token
```

## Description

Sets an AAD-specific access token into the $AADToken variable for use with Connect-AzureAD.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$AADToken` | Variable for AAD token | Yes |
| `'eyJ0eXAiOiJKV1Qi...'` | JWT token for Azure AD (placeholder) | Yes |

## Examples

### Basic Usage

```powershell
$AADToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...' 
```

## Expected Output

No output. Verify: `Write-Output $AADToken` shows the token.

## Related

- [[commands/connect-azuread-with-aad-token]]
- [[procedures/Authenticate-to-Azure-Using-Managed-Identity-Access-Tokens]]
