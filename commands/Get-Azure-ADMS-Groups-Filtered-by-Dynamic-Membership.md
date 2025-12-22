---
type: command
executor: powershell
data: 'Get-AzureADMSGroup | Where-Object {$_.GroupTypes -eq ''DynamicMembership''}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Azure
tags:
  - discovery
  - azure-ad
verified: true
validated: true
---

# Get-Azure-ADMS-Groups-Filtered-by-Dynamic-Membership

## Command

```powershell
Get-AzureADMSGroup | Where-Object {$_.GroupTypes -eq 'DynamicMembership'}
```

## Description

This PowerShell command enumerates all Azure AD Microsoft 365 groups and filters to show only those with dynamic membership enabled. Use it during reconnaissance to identify groups that automatically manage membership based on user attributes, which can be abused for persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Get-AzureADMSGroup | Retrieves all Microsoft 365 groups in the tenant | Yes (built-in cmdlet) |
| Where-Object {$_.GroupTypes -eq 'DynamicMembership'} | Filters results to groups with dynamic membership type | Yes |

## Examples

### Basic Usage

```powershell
Get-AzureADMSGroup | Where-Object {$_.GroupTypes -eq 'DynamicMembership'}
```

Connect to Azure AD first with `Connect-AzureAD`.

### Advanced Usage

```powershell
Get-AzureADMSGroup -SearchString "sensitive" | Where-Object {$_.GroupTypes -eq 'DynamicMembership'}
```

Filters dynamic groups by name containing 'sensitive'.

## Expected Output

```
Id                                   DisplayName             Description
--                                   -----------             -----------
12345678-1234-1234-1234-123456789abc Vendor Access Group     Dynamic group for vendors
87654321-4321-4321-4321-cba987654321 IT Admins               Dynamic admins group
```

Lists group IDs, display names, and descriptions for dynamic groups.

## Related

- [[procedures/Abuse-Azure-Dynamic-Group-Membership-and-Guest-Vendor-Rules]]
- [[commands/Create-Azure-Dynamic-Group-Rule-for-Guest-Vendors]]
