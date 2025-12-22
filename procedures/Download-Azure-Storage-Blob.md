---
type: procedure
verified: true
submitted: true
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/Azure Storage]]'
  - '[[tags/Azure Storage Blob]]'
  - '[[tags/Cloud - Azure]]'
  - '[[tags/List and download blobs]]'
commands:
  - '[[commands/get-azresource-list-all-resources]]'
  - '[[commands/get-azstorageaccount-by-name-and-rg]]'
  - '[[commands/get-azstoragecontainer-in-account]]'
  - '[[commands/get-azstorageblobcontent-download-blob]]'
tools:
  - '[[tools/az-powershell-module]]'
validated: true
---

# Download-Azure-Storage-Blob

## Summary

This procedure enables an attacker with valid Azure credentials to download the contents of a specific blob from an Azure Storage account, facilitating the exfiltration of sensitive data such as intellectual property or PII stored in cloud blobs.

## Description

In an attack scenario, once an adversary has obtained credentials to an Azure subscription (e.g., via credential dumping or misconfiguration exploitation), they can enumerate and access Azure Storage resources to steal data. This procedure uses the Azure PowerShell module (Az) to list resources, identify a target storage account, enumerate containers, and download blob contents. The downloaded data can then be exfiltrated over alternative protocols like HTTPS or C2 channels. This targets cloud environments where Azure Storage is used for data persistence, and success depends on the attacker's role having read permissions on the storage account. Expected outcomes include obtaining raw blob files locally for further analysis or leakage.

## Requirements

1. Azure PowerShell module (Az) installed and imported.
2. Valid Azure credentials with at least Reader access to the target resource group and Storage Blob Data Reader role on the storage account.
3. Authentication via Connect-AzAccount using the credentials.
4. Network access to Azure endpoints (no firewall blocks on Azure management ports).

## Defense

- Implement least-privilege access controls using Azure RBAC to restrict read permissions on storage accounts.
- Enable Azure Storage analytics logging and monitor for unusual download patterns, such as large data transfers from unexpected IPs.
- Use Azure Defender for Storage to detect anomalous access and encryption at rest/transit to mitigate data exposure.

## Objectives

1. Enumerate Azure resources to identify target storage accounts.
2. Access and list containers within the storage account.
3. Download the contents of a specific blob for exfiltration.
4. Validate successful data retrieval without triggering alerts.

## Instructions

### Step 1: Enumerate Azure Resources

**Context**: Begin by listing all Azure resources in the subscription to identify potential storage accounts and their resource groups. This step provides the necessary details like storage account names and resource group names for subsequent actions.

**Command** ([[commands/get-azresource-list-all-resources]]):
```powershell
Get-AzResource
```

This command retrieves a list of all resources. If the subscription has many resources, pipe to Where-Object to filter for storage accounts: `Get-AzResource | Where-Object {$_.Type -eq 'Microsoft.Storage/storageAccounts'}`. Expected output includes resource names, types, and resource groups.

### Step 2: Retrieve Specific Storage Account Details

**Context**: Using the storage account name and resource group identified in Step 1, fetch detailed information about the target storage account to obtain its context for further operations.

**Command** ([[commands/get-azstorageaccount-by-name-and-rg]]):
```powershell
Get-AzStorageAccount -Name <STORAGE_ACCOUNT_NAME> -ResourceGroupName <RESOURCE_GROUP_NAME>
```

Replace placeholders with actual values from Step 1. This retrieves the account object, including its context needed for container and blob operations. Expected output: Storage account properties like location, SKU, and primary endpoints.

### Step 3: List Containers in the Storage Account

**Context**: With the storage account context, enumerate the containers to identify where the target blob resides. This helps in scoping the download to the correct container.

**Command** ([[commands/get-azstoragecontainer-in-account]]):
```powershell
Get-AzStorageContainer -Context (Get-AzStorageAccount -Name <STORAGE_ACCOUNT_NAME> -ResourceGroupName <RESOURCE_GROUP_NAME>).Context
```

This lists all containers in the account. Expected output: A table of container names, public access levels, and legal hold status. Note the target container name for the next step.

### Step 4: Download Blob Content

**Context**: Finally, download the contents of the specific blob from the identified container. This step retrieves the file locally, completing the exfiltration preparation.

**Command** ([[commands/get-azstorageblobcontent-download-blob]]):
```powershell
Get-AzStorageBlobContent -Container <CONTAINER_NAME> -Blob <BLOB_NAME> -Context (Get-AzStorageAccount -Name <STORAGE_ACCOUNT_NAME> -ResourceGroupName <RESOURCE_GROUP_NAME>).Context -Destination <LOCAL_PATH>
```

Specify the blob name and optional local destination path (defaults to current directory with blob name). Expected output: The blob file downloaded to the specified path, with a confirmation message like "Blob downloaded successfully."

If the blob is large, monitor progress; for private blobs, ensure credentials have access.
