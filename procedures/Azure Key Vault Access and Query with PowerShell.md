---
id: a6461648-12dc-48ff-8aa8-bb19f75a16f0
name: Azure Key Vault Access and Query with PowerShell
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.671609+00:00'
updated_at: '2023-05-24T18:05:46.342442+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
platforms:
- Cloud
tags:
- '[[Cloud - Azure]]'
- '[[Key Vault]]'
- '[[KeyVault Secrets]]'
commands:
- '[[Connect to Azure]]'
- '[[Get Key Vault Access Token]]'
- '[[Query Key Vault]]'
---

# Azure Key Vault Access and Query with PowerShell

**Status**: ✓ Verified

## Summary

Accessing Azure Key Vault using Managed Identity is a method for securely storing and accessing sensitive information such as passwords, certificates, and API keys. This procedure allows applications and services running in Azure to access the Key Vault without requiring the use of secrets within t

## Description

# Description

Accessing Azure Key Vault using Managed Identity is a method for securely storing and accessing sensitive information such as passwords, certificates, and API keys. This procedure allows applications and services running in Azure to access the Key Vault without requiring the use of secrets within the code. Managed Identity provides an Azure Active Directory identity for the application or service, which can be used to authenticate and authorize access to the Key Vault. This reduces the risk of secrets being accidentally exposed or leaked, and simplifies the management of secrets for developers and administrators.

From an offensive perspective, an attacker may attempt to compromise the Managed Identity or steal the access token to gain access to sensitive information stored in the Key Vault. This can be accomplished through techniques such as Access Token Manipulation and Credential Dumping.

The business value of this procedure is that it allows for secure storage and management of sensitive information, reducing the risk of data breaches and ensuring compliance with regulations such as GDPR and HIPAA.

## Requirements

To successfully execute this procedure, ensure the following prerequisites:

1. PowerShell is installed and accessible.

1. cURL is installed and accessible.

1. Environment variables `IDENTITY_ENDPOINT` and `IDENTITY_HEADER` are set with the appropriate values.

1. Proper permissions are granted to access Azure Key Vault and Azure Management APIs.

## Defense

To enhance security and protect your Azure Key Vault and Azure resources, consider implementing the following defense measures:

1. Safeguard and limit access to environment variables containing sensitive information.

1. Regularly review and audit access control settings and permissions for Key Vault and Azure resources.

1. Monitor logs and enable diagnostic logging to detect and respond to any suspicious activities.

## Objectives

The primary objectives of this procedure are as follows:

1. Obtain an access token for Azure Key Vault using cURL commands.

1. Connect to Azure using PowerShell with the acquired access tokens.

1. Query Azure Key Vault and retrieve the list of Key Vaults.

1. Retrieve specific secrets from the designated Key Vault.

# Instructions

*<u>Overv*iew</u>

**Code**: [[# keyvault access token
curl "$IDENTITY_ENDPOINT?r]]

> This command demonstrates how to access an Azure Key Vault using Managed Identity. The command first retrieves access tokens for the Key Vault and Management APIs using the Identity Endpoint and Identity Header. Then, it connects to the Azure account using the Connect-AzAccount cmdlet and passes the access tokens and the Managed Identity Client ID. Finally, it queries the Key Vault and its secrets using the Get-AzKeyVault and Get-AzKeyVaultSecret cmdlets.

## Steps

To access an Azure Key Vault using Managed Identity, follow these steps:

          **  1. Retrieve the access token for the Key Vault and Management APIs using the Identity Endpoint and Identity Header.**

**Command** ([[Get Key Vault Access Token]]):

```bash
curl "$IDENTITY_ENDPOINT?resource=https://vault.azure.net&apiversion=2017-09-01" -H secret:$IDENTITY_HEADER
curl "$IDENTITY_ENDPOINT?resource=https://management.azure.com&apiversion=2017-09-01" -H secret:$IDENTITY_HEADER
```

**Command** ([[Connect to Azure]]):

```powershell
PS> $token = 'eyJ0..'

PS> $keyvaulttoken = 'eyJ0..'

PS Az> Connect-AzAccount -AccessToken $token -AccountId 2e91a4fea0f2-46ee-8214-fa2ff6aa9abc -KeyVaultAccessToken $keyvaulttoken
```

**Command** ([[Query Key Vault]]):

```powershell
PS Az> Get-AzKeyVault
PS Az> Get-AzKeyVaultSecret -VaultName ResearchKeyVault
PS Az> Get-AzKeyVaultSecret -VaultName ResearchKeyVault -Name Reader -AsPlainText
```

## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Commands Used

- [[Connect to Azure]]
- [[Get Key Vault Access Token]]
- [[Query Key Vault]]

## Tags

- [[Cloud - Azure]]
- [[Key Vault]]
- [[KeyVault Secrets]]
