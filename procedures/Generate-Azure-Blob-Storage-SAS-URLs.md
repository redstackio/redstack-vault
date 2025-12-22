---
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.471883+00:00'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Remote Services]]'
sub_techniques: []
tags:
  - azure-storage
  - azure-storage-blob
  - cloud-azure
  - sas-url
commands:
  - '[[commands/powershell-install-az-module]]'
  - '[[commands/powershell-connect-az-account]]'
  - '[[commands/powershell-get-storage-account-context]]'
  - '[[commands/powershell-new-container-sas-token]]'
  - '[[commands/bash-az-login]]'
  - '[[commands/bash-az-generate-container-sas]]'
platforms:
  - Cloud
tools:
  - '[[tools/Az-PowerShell]]'
  - '[[tools/Azure-CLI]]'
validated: true
---

# Generate-Azure-Blob-Storage-SAS-URLs

## Summary

This procedure demonstrates how to generate Shared Access Signature (SAS) URLs for Azure Blob Storage containers, providing time-limited, granular access to storage resources without exposing full account keys. It is useful in red team engagements for simulating lateral movement in Azure environments by creating temporary access tokens for data exfiltration or manipulation.

## Description

Azure SAS tokens allow delegated access to Blob Storage, enabling operations like read (r), write (w), delete (d), and list (l) on containers or blobs. Attackers with initial access to Azure credentials can generate these tokens to pivot to storage resources, bypassing broader account key exposure. This procedure covers both Azure PowerShell and Azure CLI methods, assuming a compromised user or service principal with Storage Blob Data Contributor permissions. The process involves authentication, context retrieval, token generation with specified permissions and expiry, and URL construction. In a pentest scenario, this can facilitate persistence or data staging in cloud storage.

## Requirements

1. Active Azure subscription with a storage account and Blob container
2. Permissions: Storage Blob Data Contributor or Owner role on the resource group/storage account
3. Local machine with PowerShell 5.1+ or Azure CLI 2.0+
4. Network access to Azure endpoints (no firewall blocks on ports 443)

## Defense

- Restrict SAS permissions to least privilege (e.g., read-only for sharing)
- Enforce short expiry durations (minutes/hours) and revoke if compromised
- Mandate HTTPS-only for SAS to prevent MITM token theft
- Enable Azure Storage analytics logging and monitor for anomalous SAS usage via Azure Monitor or Sentinel
- Implement just-in-time access with Azure PIM for management operations

## Objectives

1. Authenticate to Azure and retrieve storage account context
2. Generate a SAS token for a Blob container with rwdl permissions
3. Construct and validate a functional SAS URL for container access

## Instructions

This procedure provides two paths: Azure PowerShell (recommended for Windows environments) and Azure CLI (cross-platform). Follow one based on your setup.

### Step 1: Install Az PowerShell Module

**Context**: Ensure the Az module is installed for Azure resource management cmdlets. This step is skipped if already installed.

**Command** ([[commands/powershell-install-az-module]]):
```powershell
Install-Module -Name Az -AllowClobber -Scope CurrentUser
```

> This installs the module for the current user. Run in an elevated PowerShell session if needed.

**Expected Output**: Installation progress and confirmation: "The 'Az' package was installed successfully."

### Step 2: Connect to Azure Account (PowerShell)

**Context**: Authenticate your session to Azure using interactive login or service principal.

**Command** ([[commands/powershell-connect-az-account]]):
```powershell
Connect-AzAccount
```

> This opens a browser for login. For automation, use -ServicePrincipal with credentials.

**Expected Output**: JSON response with tenant, subscription, and user details, confirming successful authentication.

### Step 3: Get Storage Account Context (PowerShell)

**Context**: Retrieve the context object for the target storage account, which is required for SAS generation.

**Command** ([[commands/powershell-get-storage-account-context]]):
```powershell
$context = (Get-AzStorageAccount -ResourceGroupName $_RESOURCE_GROUP -Name $_STORAGE_ACCOUNT).Context
```

> Replace placeholders with actual values. This queries the storage account details.

**Expected Output**: $context variable assigned with StorageContext object containing account keys and endpoints.

### Step 4: Generate Container SAS Token (PowerShell)

**Context**: Create the SAS token with permissions (rwdl: read, write, delete, list) and a 2-hour expiry.

**Command** ([[commands/powershell-new-container-sas-token]]):
```powershell
$token = New-AzStorageContainerSASToken -Name $_CONTAINER -Context $_CONTEXT -Permission "rwdl" -ExpiryTime $_EXPIRY
```

> Permissions can be customized (e.g., "r" for read-only). Expiry is relative to now.

**Expected Output**: $token string starting with "?sv=..." containing SAS parameters.

### Step 5: Construct SAS URL (PowerShell)

**Context**: Append the token to the container endpoint to form the usable URL.

No specific command; use string concatenation:
```powershell
$url = "https://$_STORAGE_ACCOUNT.blob.core.windows.net/$_CONTAINER" + $token
```

**Expected Output**: Full URL like "https://mystorageaccount.blob.core.windows.net/mycontainer?sv=2022-11-02..."

### Alternative: Azure CLI Path

If using CLI, start from Step 6.

### Step 6: Login to Azure CLI

**Context**: Authenticate the CLI session.

**Command** ([[commands/bash-az-login]]):
```bash
az login
```

> Opens browser for login, similar to PowerShell.

**Expected Output**: List of subscriptions and confirmation: "Please go to ... and login."

### Step 7: Generate Container SAS Token (CLI)

**Context**: Generate the SAS token using CLI, with HTTPS-only and specified expiry.

**Command** ([[commands/bash-az-generate-container-sas]]):
```bash
token=$(az storage container generate-sas --name $_CONTAINER --account-name $_STORAGE_ACCOUNT --permissions rwdl --expiry $_EXPIRY --https-only --output tsv)
```

> Expiry in ISO format (e.g., 2024-01-01T23:59Z). Output as TSV for variable capture.

**Expected Output**: $token variable with SAS string (e.g., "sv=2022-11-02&ss=b&srt=co&sp=rwdl...").

### Step 8: Construct SAS URL (CLI)

**Context**: Build the URL by appending the token as a query parameter.

No specific command; use variable substitution:
```bash
url="https://$_STORAGE_ACCOUNT.blob.core.windows.net/$_CONTAINER?${token}"
```

**Expected Output**: Full URL ready for HTTP requests (e.g., via curl to test access).
