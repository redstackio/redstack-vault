---
id: a3bf5def-a02e-44f4-bcd3-75a5876eb51b
name: set-access-token-variable
type: command
executor: powershell
data: >-
  $token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...' # Replace with
  actual access token
output: null
created_at: '2023-05-30T13:47:18.322713+00:00'
updated_at: '2023-05-30T13:47:19.298036+00:00'
platforms:
  - Windows
tags:
  - cloud-auth
  - azure
verified: true
validated: true
---

# set-access-token-variable

## Command

```powershell
$token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...' # Replace with actual access token
```

## Description

Assigns a JWT access token from an Azure Managed Identity to the $token variable for use in subsequent Azure authentication commands. This prepares the token for passing to Connect-AzAccount.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$token` | Variable name to store the token | Yes |
| `'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...'` | The JWT access token string (placeholder; replace with real token) | Yes |

## Examples

### Basic Usage

```powershell
$token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1...' # Shortened example token
Write-Output $token  # Verify it's set
```

### Advanced Usage

Combine with token retrieval:

```powershell
# Assuming token fetched earlier
$token = (Invoke-RestMethod -Uri 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/' -Headers @{"Metadata"="true"} -Method GET).access_token
```

## Expected Output

No direct output from the assignment. Use `Write-Output $token` to confirm: Displays the full JWT string if set correctly. Errors occur if the token format is invalid (e.g., missing quotes).

## Related

- [[commands/connect-azaccount-with-access-token]]
- [[procedures/Authenticate-to-Azure-Using-Managed-Identity-Access-Tokens]]
