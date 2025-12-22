---
type: command
executor: powershell
data: Get-AzVM | Format-List
output: null
platforms:
  - Cloud
tags:
  - az-powershell
  - enumeration
  - compute
verified: true
validated: true
---

# Get-Az VM Formatted

## Command

```powershell
Get-AzVM | Format-List
```

## Description

This command lists all virtual machines in detail format. Use for enumerating compute resources and their configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Name | Specific VM name | No |
| -ResourceGroupName | Filter by resource group | No |
| Format-List | Displays properties in list view | Built-in |

## Examples

### Basic Usage

```powershell
Get-AzVM | Format-List
```

### Advanced Usage

Specific VM:

```powershell
Get-AzVM -Name "myVM" | Format-List
```

## Expected Output

List view:

```
Name            : myVM
Location        : eastus
VMSize          : Standard_D2s_v3
ProvisioningState : Succeeded
...
```

## Related

- [[Azure Tenant Enumeration with Az PowerShell (Creds)]
- [[commands/get-az-resource]]
