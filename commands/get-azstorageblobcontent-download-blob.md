---
type: command
executor: powershell
data: >-
  Get-AzStorageBlobContent -Container <CONTAINER_NAME> -Blob <BLOB_NAME>
  -Context (Get-AzStorageAccount -Name <STORAGE_ACCOUNT_NAME> -ResourceGroupName
  <RESOURCE_GROUP_NAME>).Context -Destination <LOCAL_PATH>
platforms:
  - Cloud
tags:
  - azure
  - storage
  - blob
  - download
verified: true
validated: true
---

# get-azstorageblobcontent-download-blob

## Command

```powershell
Get-AzStorageBlobContent -Container $_CONTAINER_NAME -Blob $_BLOB_NAME -Context (Get-AzStorageAccount -Name $_STORAGE_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME).Context -Destination $_LOCAL_PATH
```

## Description

Downloads the content of a specific blob from an Azure Storage container to a local path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CONTAINER_NAME | Name of the container holding the blob | Yes |
| $_BLOB_NAME | Name of the target blob | Yes |
| $_STORAGE_ACCOUNT_NAME | Name of the storage account | Yes |
| $_RESOURCE_GROUP_NAME | Name of the resource group | Yes |
| $_LOCAL_PATH | Local destination path (optional, defaults to current dir) | No |

## Examples

### Basic Usage

```powershell
Get-AzStorageBlobContent -Container "mycontainer" -Blob "sensitivefile.txt" -Context (Get-AzStorageAccount -Name "mystorageaccount" -ResourceGroupName "myRG").Context
```

### With Destination

```powershell
Get-AzStorageBlobContent -Container "mycontainer" -Blob "sensitivefile.txt" -Context (Get-AzStorageAccount -Name "mystorageaccount" -ResourceGroupName "myRG").Context -Destination "C:\Downloads\"
```

## Expected Output

Blob downloaded to local path with message: "Blob content retrieved successfully."

## Related

- [[procedures/Download-Azure-Storage-Blob]]
