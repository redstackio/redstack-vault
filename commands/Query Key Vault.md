---
id: cc7b10d4-1809-4e63-8cbb-f0726940ab7e
name: Query Key Vault
type: command
executor: bash
data: 'PS Az> Get-AzKeyVault

  PS Az> Get-AzKeyVaultSecret -VaultName ResearchKeyVault

  PS Az> Get-AzKeyVaultSecret -VaultName ResearchKeyVault -Name Reader -AsPlainText'
output: null
created_at: '2023-05-24T18:03:17.783985+00:00'
updated_at: '2023-05-24T18:03:18.179034+00:00'
---

# Query Key Vault

```bash
PS Az> Get-AzKeyVault
PS Az> Get-AzKeyVaultSecret -VaultName ResearchKeyVault
PS Az> Get-AzKeyVaultSecret -VaultName ResearchKeyVault -Name Reader -AsPlainText
```


