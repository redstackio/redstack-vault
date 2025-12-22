---
type: command
executor: powershell
data: Get-AzResource
platforms:
  - Cloud
tags:
  - azure
  - enumeration
  - resources
verified: true
validated: true
---

# get-azresource-list-all-resources

## Command

```powershell
Get-AzResource
```

## Description

This command lists all Azure resources in the current subscription, useful for initial reconnaissance to identify storage accounts, VMs, and other assets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; optionally pipe to filters like `| Where-Object {$_.Type -eq 'Microsoft.Storage/storageAccounts'}` | No |

## Examples

### Basic Usage

```powershell
Get-AzResource
```

### Filtered Usage

```powershell
Get-AzResource | Where-Object {$_.Type -eq 'Microsoft.Storage/storageAccounts'}
```

## Expected Output

A table of resources:

Name                  : mystorageaccount
ResourceId            : /subscriptions/.../resourceGroups/myRG/providers/Microsoft.Storage/storageAccounts/mystorageaccount
ResourceType          : Microsoft.Storage/storageAccounts
Location              : eastus
ResourceGroupName     : myRG

## Related

- [[procedures/Download-Azure-Storage-Blob]]
