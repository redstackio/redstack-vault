---
id: 1c293bdf-8301-42b5-a703-270f213faa22
name: az-list-storage-accounts
type: command
executor: bash
data: az storage account list
output: null
created_at: '2023-05-25T04:48:48.223070+00:00'
updated_at: '2023-05-25T04:48:49.579271+00:00'
platforms:
  - Cloud
tags:
  - az-cli
  - enumeration
verified: true
validated: true
---

# az-list-storage-accounts

## Command

```bash
az storage account list
```

## Description

This command lists all storage accounts in the subscription, helping identify data repositories that could be accessed for exfiltration or further enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Lists all storage accounts with default JSON output | N/A |

## Examples

### Basic Usage

```bash
az storage account list
```

### Advanced Usage

Filter by location:
```bash
az storage account list --query "[?location=='East US']"
```

## Expected Output

JSON array example:
```
[
  {
    "id": "/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Storage/storageAccounts/mystorage",
    "kind": "StorageV2",
    "location": "East US",
    "name": "mystorage",
    "properties": {
      "primaryEndpoints": {
        "blob": "https://mystorage.blob.core.windows.net/"
      },
      "provisioningState": "Succeeded"
    },
    "sku": {
      "name": "Standard_LRS",
      "tier": "Standard"
    }
  }
]
```

## Related

- [[procedures/Azure-Tenant-Enumeration-with-Az-CLI]]
- [[tools/Azure-CLI]]
