---
type: command
executor: powershell
data: Get-AzResource
output: null
platforms:
  - Cloud
tags:
  - az-powershell
  - enumeration
verified: true
validated: true
---

# Get-Az Resource

## Command

```powershell
Get-AzResource
```

## Description

This command lists all Azure resources visible to the authenticated user in the current subscription. Use it for initial discovery of the tenant's resource inventory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ResourceType | Filter by resource type (e.g., Microsoft.Compute/virtualMachines) | No |
| -ResourceName | Filter by specific resource name | No |
| -Location | Filter by resource location | No |

## Examples

### Basic Usage

```powershell
Get-AzResource
```

### Advanced Usage

Filter VMs:

```powershell
Get-AzResource -ResourceType "Microsoft.Compute/virtualMachines"
```

## Expected Output

Table format:

```
Name                Type                                    Location
----                ----                                    --------
myVM                Microsoft.Compute/virtualMachines       eastus
mystorage           Microsoft.Storage/storageAccounts      eastus
mywebapp            Microsoft.Web/sites                   eastus
```

## Related

- [[Azure Tenant Enumeration with Az PowerShell (Creds)]
- [[commands/connect-az-account-with-creds]]
