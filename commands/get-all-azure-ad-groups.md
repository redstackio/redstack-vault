---
id: e9f0c673-5490-40dc-9fa8-13e80bcdc298
name: get-all-azure-ad-groups
type: command
executor: powershell
data: Get-AzureADGroup -All $true
output: null
created_at: '2023-05-23T19:33:22.165807+00:00'
updated_at: '2023-05-23T19:33:22.785549+00:00'
platforms:
  - Cloud
tags:
  - azure-ad
  - enumeration
  - groups
verified: true
validated: true
---

# Get All Azure AD Groups

## Command

```powershell
Get-AzureADGroup -All $true
```

## Description

Lists all groups in the Azure AD tenant, including security groups and Office 365 groups, to map organizational structure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -All | Fetches all groups | Yes |
| $true | Enables full retrieval | Built-in |

## Examples

### Basic Usage

```powershell
Get-AzureADGroup -All $true
```

### Advanced Usage

Filter by type: Get-AzureADGroup -All $true | Where-Object {$_.GroupType -eq "Security"}

## Expected Output

ObjectId                             DisplayName    Description
--------                             -----------    -----------
11111111-...                        IT Admins      IT Department Administrators
22222222-...                        Sales Team     Sales group

## Related

- [[procedures/azure-ad-enumeration-using-powershell-with-credentials]]
