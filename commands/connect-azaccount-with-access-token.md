---
id: 7fb068d2-cd1c-4259-821d-617f4bab0c4c
name: connect-azaccount-with-access-token
type: command
executor: powershell
data: Connect-AzAccount -AccessToken $token -AccountId $_ACCOUNT_ID
output: null
created_at: '2023-05-30T13:47:18.322998+00:00'
updated_at: '2023-05-30T13:47:19.298036+00:00'
platforms:
  - Windows
tags:
  - cloud-auth
  - azure
verified: true
validated: true
---

# connect-azaccount-with-access-token

## Command

```powershell
Connect-AzAccount -AccessToken $token -AccountId $_ACCOUNT_ID
```

## Description

Authenticates a PowerShell session to Azure Resource Manager using a provided access token and account ID, typically from a managed identity. This establishes a context for Az module cmdlets without interactive login.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-AccessToken` | The JWT access token variable (e.g., $token) | Yes |
| `-AccountId` | Object ID of the managed identity account (placeholder: $_ACCOUNT_ID) | Yes |

## Examples

### Basic Usage

```powershell
$token = 'eyJ0eXAiOiJKV1Qi...'  # Set token first
Connect-AzAccount -AccessToken $token -AccountId '12345678-1234-1234-1234-123456789012'
```

### Advanced Usage

With error handling:

```powershell
try { Connect-AzAccount -AccessToken $token -AccountId $_ACCOUNT_ID -ErrorAction Stop } catch { Write-Error 'Auth failed: Invalid token or ID' }
```

## Expected Output

Success: 
```
EnvironmentName : AzureCloud
Account         : SystemAssignedManagedIdentity
TenantId        : xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
SubscriptionId  : xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Context         : Microsoft.Azure.Commands.Common.Authentication.Abstractions.AzureContext
```
Failure: Error like "AADSTS70002: Error validating credentials" if token expired.

## Related

- [[commands/set-access-token-variable]]
- [[procedures/Authenticate-to-Azure-Using-Managed-Identity-Access-Tokens]]
