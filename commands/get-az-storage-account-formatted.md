---
type: command
executor: powershell
data: Get-AzStorageAccount | Format-List
output: null
platforms:
  - Cloud
tags:
  - az-powershell
  - enumeration
  - storage
verified: true
validated: true
---

# Get-Az Storage Account Formatted

## Command

```powershell
Get-AzStorageAccount | Format-List
```

## Description

This command lists storage accounts in detailed list format. Use to identify data storage targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ResourceGroupName | Filter by resource group | No |
| Format-List | Displays in list view | Built-in |

## Examples

### Basic Usage

```powershell
Get-AzStorageAccount | Format-List
```

### Advanced Usage

Filter by kind:

```powershell
Get-AzStorageAccount -Kind Storage | Format-List
```

## Expected Output

List:

```
StorageAccountName : mystorage
Kind                : Storage
Location            : eastus
Sku                 : {Name: Standard_LRS, Tier: Standard}
...
```

## Related

- [[Azure Tenant Enumeration with Az PowerShell (Creds)]
- [[commands/get-az-resource]]
