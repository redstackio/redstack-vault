---
id: a255185b-efc9-4012-a8ef-64ade39fe1e9
name: get-azuread-directory-role
type: command
executor: powershell
data: Get-AzureADDirectoryRole -ObjectId $_ROLE_ID
output: null
created_at: '2023-04-06T03:56:15.847909+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
  - Cloud
tags:
  - discovery
  - azure-ad
verified: true
validated: true
---

# get-azuread-directory-role

## Command

```powershell
Get-AzureADDirectoryRole -ObjectId $_ROLE_ID
```

## Description

Retrieves details of a directory role in Azure AD by its object ID. Helps in discovering role definitions and their scopes for privilege analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ObjectId | The GUID of the directory role | Yes |
| $_ROLE_ID | Placeholder for the role's object ID | Yes |

## Examples

### Basic Usage

```powershell
Get-AzureADDirectoryRole -ObjectId "role-guid-123"
```

### Advanced Usage

Get all roles first, then details:

```powershell
Get-AzureADDirectoryRole | ForEach { Get-AzureADDirectoryRole -ObjectId $_.ObjectId }
```

## Expected Output

Object with `ObjectId`, `DisplayName`, `Description`, `RoleTemplateId`. Example:

```
ObjectId           : role-guid-123
DisplayName        : User Administrator
Description        : Can manage user accounts
RoleTemplateId     : 7888d69c-8bd9-48b2-aca0-5a2d4d7f6b8e
```
Success if role details are returned.

## Related

- [[commands/get-azureadms-scoped-role-membership]]
- [[procedures/Azure-AD-Administrative-Unit-Management]]
