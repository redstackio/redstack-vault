---
type: command
executor: powershell
data: >-
  Get-AzStorageContainer -Context (Get-AzStorageAccount -Name
  <STORAGE_ACCOUNT_NAME> -ResourceGroupName <RESOURCE_GROUP_NAME>).Context
platforms:
  - Cloud
tags:
  - azure
  - storage
  - container
verified: true
validated: true
---

# get-azstoragecontainer-in-account

## Command

```powershell
Get-AzStorageContainer -Context (Get-AzStorageAccount -Name $_STORAGE_ACCOUNT_NAME -ResourceGroupName $_RESOURCE_GROUP_NAME).Context
```

## Description

Lists all containers in a specified Azure Storage account using its context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_STORAGE_ACCOUNT_NAME | Name of the storage account | Yes |
| $_RESOURCE_GROUP_NAME | Name of the resource group | Yes |

## Examples

### Basic Usage

```powershell
Get-AzStorageContainer -Context (Get-AzStorageAccount -Name "mystorageaccount" -ResourceGroupName "myRG").Context
```

## Expected Output

Name              : mycontainer
PublicAccess      : Off
HasLegalHold      : False
HasImmutabilityPolicy : False

## Related

- [[procedures/Download-Azure-Storage-Blob]]
