---
id: 4902a1ba-1e85-42c9-b898-eae6c01d4a6d
name: Connect-to-Azure-with-Access-Token
type: command
executor: powershell
data: >-
  $token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1u...'

  $keyvaulttoken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...'

  Connect-AzAccount -AccessToken $token -AccountId $_CLIENT_ID
  -KeyVaultAccessToken $keyvaulttoken
output: null
created_at: '2023-05-24T18:03:17.783443+00:00'
updated_at: '2023-05-24T18:03:18.179034+00:00'
platforms:
  - Cloud
tags:
  - azure
  - authentication
  - managed-identity
verified: true
validated: true
---

# Connect-to-Azure-with-Access-Token

## Command

```powershell
$token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1u...'
$keyvaulttoken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...'
Connect-AzAccount -AccessToken $token -AccountId $_CLIENT_ID -KeyVaultAccessToken $keyvaulttoken
```

## Description

This command authenticates to the Az PowerShell module using bearer tokens from Managed Identity, bypassing interactive login. It sets the session context for the identity's account, enabling queries to Azure resources like Key Vault.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $token | Management API access token (from curl) | Yes |
| $keyvaulttoken | Key Vault access token (from curl) | Yes |
| -AccessToken $token | Specifies the management token for the account | Yes |
| -AccountId $_CLIENT_ID | Managed Identity client ID (e.g., 2e91a4fea0f2-46ee-8214-fa2ff6aa9abc) | Yes |
| -KeyVaultAccessToken $keyvaulttoken | Specifies the Key Vault token for secret access | Yes |

## Examples

### Basic Usage

```powershell
Connect-AzAccount -AccessToken $token -AccountId 'your-client-id' -KeyVaultAccessToken $keyvaulttoken
```

### With Token Assignment

First assign tokens from previous step, then connect.

## Expected Output

Welcome message:

```
Account: Managed Identity (your-client-id)
Environment: AzureCloud
TenantId: ...
Subscription: ...
```
Success: No errors, session active (check with Get-AzContext). Failure: InvalidToken error if tokens expired or invalid.

## Related

- [[procedures/Access-Azure-Key-Vault-Using-Managed-Identity]]
- [[commands/Get-Azure-Key-Vault-Access-Token]]
