---
id: 8cc49da0-1f92-4f7b-8d41-f1e35431fd1e
type: code
language: Powershell
verified: false
created_at: '2023-05-24T18:02:20.816096+00:00'
updated_at: '2023-05-24T18:03:01.269898+00:00'
---

# Code Snippet 8cc49da0

**Language**: Powershell

```powershell
# keyvault access token
curl "$IDENTITY_ENDPOINT?resource=https://vault.azure.net&apiversion=2017-09-01" -H secret:$IDENTITY_HEADER
curl "$IDENTITY_ENDPOINT?resource=https://management.azure.com&apiversion=2017-09-01" -H secret:$IDENTITY_HEADER

# connect
PS> $token = 'eyJ0..'
PS> $keyvaulttoken = 'eyJ0..'
PS Az> Connect-AzAccount -AccessToken $token -AccountId 2e91a4fea0f2-46ee-8214-fa2ff6aa9abc -KeyVaultAccessToken $keyvaulttoken

# query the vault and the secrets
PS Az> Get-AzKeyVault
PS Az> Get-AzKeyVaultSecret -VaultName ResearchKeyVault
PS Az> Get-AzKeyVaultSecret -VaultName ResearchKeyVault -Name Reader -AsPlainText
```


