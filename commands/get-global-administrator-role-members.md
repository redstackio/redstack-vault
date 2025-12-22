---
id: b9a5bdf2-fbbf-4992-82c4-297e83094599
name: get-global-administrator-role-members
type: command
executor: powershell
data: >-
  Get-AzureADDirectoryRole -Filter "DisplayName eq 'Global Administrator'" |
  Get-AzureADDirectoryRoleMember
output: null
created_at: '2023-05-23T19:33:22.167812+00:00'
updated_at: '2023-05-23T19:33:22.785549+00:00'
platforms:
  - Cloud
tags:
  - azure-ad
  - enumeration
  - roles
verified: true
validated: true
---

# Get Global Administrator Role Members

## Command

```powershell
Get-AzureADDirectoryRole -Filter "DisplayName eq 'Global Administrator'" | Get-AzureADDirectoryRoleMember
```

## Description

Queries the Global Administrator directory role and lists its direct members to identify top-privilege accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Filter | OData filter for role display name | Yes |
| DisplayName eq 'Global Administrator' | Exact match for the role | Built-in |

## Examples

### Basic Usage

```powershell
Get-AzureADDirectoryRole -Filter "DisplayName eq 'Global Administrator'" | Get-AzureADDirectoryRoleMember
```

### Advanced Usage

Select UPNs: ... | Select-Object DisplayName, UserPrincipalName

## Expected Output

ObjectId                             DisplayName    UserPrincipalName
--------                             -----------    -----------------
55555555-...                        Admin User     admin@contoso.onmicrosoft.com

## Related

- [[procedures/azure-ad-enumeration-using-powershell-with-credentials]]
