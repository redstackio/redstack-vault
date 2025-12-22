---
type: command
executor: powershell
data: Get-AzKeyVault
output: null
platforms:
  - Cloud
tags:
  - az-powershell
  - enumeration
  - secrets
verified: true
validated: true
---

# Get-Az Key Vault

## Command

```powershell
Get-AzKeyVault
```

## Description

This command lists Azure Key Vaults. Use to discover secrets management resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -VaultName | Specific vault name | No |
| -ResourceGroupName | Filter by resource group | No |

## Examples

### Basic Usage

```powershell
Get-AzKeyVault
```

### Advanced Usage

Detailed:

```powershell
Get-AzKeyVault | Format-List
```

## Expected Output

Table:

```
VaultName   Location
---------   --------
mykeyvault  eastus
```

## Related

- [[Azure Tenant Enumeration with Az PowerShell (Creds)]
- [[commands/get-az-role-assignment-for-user]]
