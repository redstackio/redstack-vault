---
id: c996d5b7-869d-45f5-b9e8-127ae7aec094
name: get-azureadms-administrative-unit-member
type: command
executor: powershell
data: Get-AzureADMSAdministrativeUnitMember -Id $_ADMIN_UNIT_ID
output: null
created_at: '2023-04-06T03:56:15.847790+00:00'
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

# get-azureadms-administrative-unit-member

## Command

```powershell
Get-AzureADMSAdministrativeUnitMember -Id $_ADMIN_UNIT_ID
```

## Description

Lists all members (users, groups, devices) of a specific administrative unit in Azure AD. Essential for enumerating scoped access during discovery phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Id | The GUID of the administrative unit | Yes |
| $_ADMIN_UNIT_ID | Placeholder for the unit's object ID | Yes |

## Examples

### Basic Usage

```powershell
Get-AzureADMSAdministrativeUnitMember -Id "12345678-1234-1234-1234-123456789abc"
```

### Advanced Usage

Filter for users only:

```powershell
Get-AzureADMSAdministrativeUnitMember -Id $_ADMIN_UNIT_ID | Where-Object { $_.AdditionalProperties.'@odata.type' -eq '#microsoft.graph.user' }
```

## Expected Output

Array of member objects with `Id`, `DisplayName`, and type. Example:

```
Id                 : user-guid-1
DisplayName        : John Doe
@odata.type        : #microsoft.graph.user

Id                 : group-guid-1
DisplayName        : Marketing Group
@odata.type        : #microsoft.graph.group
```
Success if members are listed; empty array if no members.

## Related

- [[commands/get-azureadms-administrative-unit]]
- [[procedures/Azure-AD-Administrative-Unit-Management]]
