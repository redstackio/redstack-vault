---
id: 53e395d8-cdf3-4219-9cfd-de6a16371318
name: get-azureadms-administrative-unit
type: command
executor: powershell
data: Get-AzureADMSAdministrativeUnit -Id $_ADMIN_UNIT_ID
output: null
created_at: '2023-04-06T03:56:15.847714+00:00'
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

# get-azureadms-administrative-unit

## Command

```powershell
Get-AzureADMSAdministrativeUnit -Id $_ADMIN_UNIT_ID
```

## Description

Retrieves details of a specific administrative unit in Azure AD by its ID. This is useful for discovering scoped delegations and configurations during reconnaissance of Azure environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Id | The GUID of the administrative unit | Yes |
| $_ADMIN_UNIT_ID | Placeholder for the unit's object ID | Yes |

## Examples

### Basic Usage

```powershell
Get-AzureADMSAdministrativeUnit -Id "12345678-1234-1234-1234-123456789abc"
```

### Advanced Usage

Pipe to select specific properties:

```powershell
Get-AzureADMSAdministrativeUnit -Id $_ADMIN_UNIT_ID | Select DisplayName, Description
```

## Expected Output

Returns an object with properties like `Id`, `DisplayName`, `Description`, `Visibility`. Example:

```
Id                 : 12345678-1234-1234-1234-123456789abc
DisplayName        : Marketing AU
Description        : Scoped unit for marketing team
Visibility         : Public
```
Success if the unit details are displayed without access denied errors.

## Related

- [[commands/get-azureadms-administrative-unit-member]]
- [[procedures/Azure-AD-Administrative-Unit-Management]]
