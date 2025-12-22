---
id: 98f24a42-8335-4e8d-b246-29966eaf9c66
name: get-azureadms-scoped-role-membership
type: command
executor: powershell
data: Get-AzureADMSScopedRoleMembership -Id $_MEMBERSHIP_ID | Format-List
output: null
created_at: '2023-04-06T03:56:15.847850+00:00'
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

# get-azureadms-scoped-role-membership

## Command

```powershell
Get-AzureADMSScopedRoleMembership -Id $_MEMBERSHIP_ID | Format-List
```

## Description

Fetches and formats details of a scoped role membership in Azure AD, revealing assignments within administrative units.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Id | The GUID of the scoped role membership | Yes |
| $_MEMBERSHIP_ID | Placeholder for the membership ID | Yes |
| | Format-List | Pipe for formatted output |

## Examples

### Basic Usage

```powershell
Get-AzureADMSScopedRoleMembership -Id "membership-guid-123" | Format-List
```

### Advanced Usage

List all memberships:

```powershell
Get-AzureADMSScopedRoleMembership | Format-List *
```

## Expected Output

Formatted list with `Id`, `AdministrativeUnitId`, `RoleDefinitionId`, `RoleMemberInfo`. Example:

```
Id                 : membership-guid-123
AdministrativeUnitId : au-guid-456
RoleDefinitionId   : role-def-789
RoleMemberInfo     : @{Id= user-guid; DisplayName=John Doe}
```
Success if membership details are displayed.

## Related

- [[commands/get-azuread-directory-role]]
- [[procedures/Azure-AD-Administrative-Unit-Management]]
