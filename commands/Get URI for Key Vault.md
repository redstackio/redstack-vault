---
id: 11019f9e-c30b-464a-813c-c992ffd23b75
name: Get URI for Key Vault
type: command
executor: bash
data: 'az keyvault secret list --vault-name <KeyVaultName> --query ''[].id'' --output
  tsv

  '
output: null
created_at: '2020-07-14T19:07:50.934103+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get URI for Key Vault

```bash
az keyvault secret list --vault-name <KeyVaultName> --query '[].id' --output tsv

```
