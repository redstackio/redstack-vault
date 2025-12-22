---
type: command
executor: powershell
data: Get-AzRoleAssignment -SignInName "$_USERNAME@$_TENANT_NAME.onmicrosoft.com"
output: null
platforms:
  - Cloud
tags:
  - az-powershell
  - enumeration
  - rbac
verified: true
validated: true
---

# Get-Az Role Assignment for User

## Command

```powershell
Get-AzRoleAssignment -SignInName "$_USERNAME@$_TENANT_NAME.onmicrosoft.com"
```

## Description

This command retrieves role-based access control (RBAC) assignments for a specific user, showing permissions across scopes. Use to assess the authenticated user's privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -SignInName | User's email (e.g., test@contoso.onmicrosoft.com) | Yes |
| -Scope | Limit to specific scope (e.g., subscription ID) | No |
| -RoleDefinitionName | Filter by role (e.g., Owner) | No |

## Examples

### Basic Usage

```powershell
Get-AzRoleAssignment -SignInName "test@contoso.onmicrosoft.com"
```

### Advanced Usage

At subscription scope:

```powershell
Get-AzRoleAssignment -SignInName "test@contoso.onmicrosoft.com" -Scope "/subscriptions/zzzz-zzzz-zzzz-zzzz"
```

## Expected Output

Table:

```
DisplayName RoleDefinitionName          Scope
----------- -------------------          -----
test        Contributor                 /subscriptions/...
test        Reader                      /subscriptions/...
```

## Related

- [[Azure Tenant Enumeration with Az PowerShell (Creds)]
- [[commands/connect-az-account-with-creds]]
