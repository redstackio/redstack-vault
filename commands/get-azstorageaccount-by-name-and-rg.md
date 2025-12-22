---
type: command
executor: powershell
data: >-
  Get-AzStorageAccount -Name <STORAGE_ACCOUNT_NAME> -ResourceGroupName
  <RESOURCE_GROUP_NAME>
platforms:
  - Cloud
tags:
  - azure
  - storage
  - account
verified: true
validated: true
---

# get-azstorageaccount-by-name-and-rg

## Command

```powershell
Get-AzStorageAccount -Name $_STORAGE_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME
```

## Description

Retrieves details of a specific Azure Storage account by name and resource group, providing context for blob and container operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_STORAGE_ACCOUNT_NAME | Name of the storage account | Yes |
| $_RESOURCE_GROUP_NAME | Name of the resource group containing the account | Yes |

## Examples

### Basic Usage

```powershell
Get-AzStorageAccount -Name "mystorageaccount" -ResourceGroupName "myRG"
```

## Expected Output

StorageAccountName : mystorageaccount
ResourceGroupName  : myRG
PrimaryLocation    : eastus
ProvisioningState  : Succeeded
StatusOfPrimary    : Available

Context            : Microsoft.Azure.Storage.Auth.StorageCredentials

## Related

- [[procedures/Download-Azure-Storage-Blob]]
