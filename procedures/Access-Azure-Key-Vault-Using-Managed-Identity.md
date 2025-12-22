---
id: a6461648-12dc-48ff-8aa8-bb19f75a16f0
name: Access-Azure-Key-Vault-Using-Managed-Identity
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.671609+00:00'
updated_at: '2023-05-24T18:05:46.342442+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - >-
    [[techniques/Steal Application Access Token|T1528 - Steal Application Access
    Token]]
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Key Vault]]'
  - '[[tags/KeyVault Secrets]]'
commands:
  - '[[commands/Get-Azure-Key-Vault-Access-Token]]'
  - '[[commands/Connect-to-Azure-with-Access-Token]]'
  - '[[commands/Query-Azure-Key-Vault-Secrets]]'
tools: []
validated: true
---

# Access-Azure-Key-Vault-Using-Managed-Identity

## Summary

This procedure demonstrates how to access Azure Key Vault secrets using Managed Identity authentication via PowerShell. It involves retrieving access tokens for Key Vault and Azure Management APIs, connecting to Azure with those tokens, and querying the vault to retrieve secrets. From an offensive security perspective, this technique can be used to steal application access tokens or dump credentials stored in Key Vault after compromising a managed identity in an Azure environment.

## Description

Azure Key Vault is a service for securely storing and accessing secrets like passwords, certificates, and keys. Managed Identities allow Azure resources (e.g., VMs) to authenticate to services like Key Vault without embedding credentials in code. An attacker with access to a compromised Azure resource can exploit the managed identity to request tokens via the IMDS (Instance Metadata Service) endpoint and use them to query sensitive data.

This procedure assumes execution from an Azure VM or similar resource with a managed identity enabled. It uses environment variables provided by Azure ($IDENTITY_ENDPOINT and $IDENTITY_HEADER) to fetch tokens without explicit credentials. Offensively, this maps to stealing application tokens (T1528) and credential dumping (T1003) in cloud environments, enabling further lateral movement or data exfiltration.

## Requirements

1. Execution on an Azure resource (e.g., VM) with a system-assigned or user-assigned Managed Identity enabled and appropriate RBAC permissions (e.g., Key Vault Secrets User role).
2. PowerShell 5.1+ with Az PowerShell module installed (Install-Module -Name Az -AllowClobber).
3. curl utility available (pre-installed on Linux VMs; use Invoke-RestMethod in pure PowerShell if needed).
4. Environment variables $IDENTITY_ENDPOINT (e.g., http://169.254.169.254/metadata/identity/oauth2/token) and $IDENTITY_HEADER (e.g., Metadata: true) set by Azure.
5. Network access to Azure APIs (no firewall blocks on outbound HTTPS to vault.azure.net and management.azure.com).

## Defense

- Limit Managed Identity permissions to least privilege (e.g., use conditional access policies and just-in-time access).
- Enable Azure Key Vault diagnostics logging and monitor for unusual token requests or secret access via Microsoft Sentinel or Azure Monitor.
- Implement network security groups (NSGs) to restrict IMDS access and audit PowerShell execution with Microsoft Defender for Cloud.
- Rotate secrets regularly and use private endpoints for Key Vault to prevent public access.

## Objectives

1. Obtain access tokens for Azure Key Vault and Management APIs using the Managed Identity endpoint.
2. Authenticate to Azure PowerShell using the acquired tokens.
3. Enumerate Key Vaults and extract specific secrets in plaintext.
4. Achieve unauthorized access to sensitive credentials stored in Key Vault for further exploitation.

## Instructions

### Step 1: Retrieve Access Tokens

**Context**: Use the Managed Identity endpoint to request tokens for Key Vault and Azure Management scopes. This step leverages the IMDS to obtain bearer tokens without stored credentials, a common vector for token theft in compromised Azure resources.

**Command** ([[commands/Get-Azure-Key-Vault-Access-Token]]):
```bash
curl "$IDENTITY_ENDPOINT?resource=https://vault.azure.net&api-version=2017-09-01" -H secret:$IDENTITY_HEADER
curl "$IDENTITY_ENDPOINT?resource=https://management.azure.com&api-version=2017-09-01" -H secret:$IDENTITY_HEADER
```

> These commands fetch JSON responses containing 'access_token' fields. Copy the tokens for use in the next step. If successful, you'll see JWT tokens in the output; errors indicate insufficient identity permissions or missing env vars.

### Step 2: Connect to Azure

**Context**: Use the tokens to authenticate to the Az PowerShell module, associating the session with the Managed Identity's client ID. This establishes a context for querying Azure resources without interactive login.

**Command** ([[commands/Connect-to-Azure-with-Access-Token]]):
```powershell
$token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1u...
$keyvaulttoken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...
Connect-AzAccount -AccessToken $token -AccountId $_CLIENT_ID -KeyVaultAccessToken $keyvaulttoken
```

> Replace placeholders with actual token values and the Managed Identity's client ID (e.g., from Azure portal). Success is indicated by a welcome message showing the subscription context; failures show authentication errors.

### Step 3: Query Key Vault and Secrets

**Context**: Once connected, enumerate available Key Vaults and retrieve secrets. This step dumps sensitive data like API keys or passwords, enabling escalation in the cloud environment.

**Command** ([[commands/Query-Azure-Key-Vault-Secrets]]):
```powershell
Get-AzKeyVault
Get-AzKeyVaultSecret -VaultName $_VAULT_NAME
Get-AzKeyVaultSecret -VaultName $_VAULT_NAME -Name $_SECRET_NAME -AsPlainText
```

> Specify the vault and secret names based on enumeration results. Expected output includes vault lists and secret values in plaintext. Verify access by checking for non-empty secret content; permission denied errors indicate RBAC issues.

For a complete scripted execution, refer to the full code snippet [[codes/PowerShell-Azure-Key-Vault-Access-Script]].
