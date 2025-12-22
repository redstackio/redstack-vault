---
id: 1f7a760b-b104-4466-81b0-0fd6d44a2468
name: get-azuread-user-by-object-id
type: command
executor: powershell
data: Get-AzureADUser -ObjectId $_USER_ID | Format-List
output: null
created_at: '2023-04-06T03:56:15.848018+00:00'
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

# get-azuread-user-by-object-id

## Command

```powershell
Get-AzureADUser -ObjectId $_USER_ID | Format-List
```

## Description

Retrieves and formats details of a user in Azure AD by object ID, useful for profiling targets from prior enumerations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ObjectId | The GUID of the user | Yes |
| $_USER_ID | Placeholder for the user's object ID | Yes |
| | Format-List | Pipe for formatted output |

## Examples

### Basic Usage

```powershell
Get-AzureADUser -ObjectId "user-guid-123" | Format-List
```

### Advanced Usage

Select specific properties:

```powershell
Get-AzureADUser -ObjectId $_USER_ID | Select UserPrincipalName, DisplayName, AccountEnabled | Format-List
```

## Expected Output

Formatted user object with `ObjectId`, `UserPrincipalName`, `DisplayName`, etc. Example:

```
ObjectId           : user-guid-123
UserPrincipalName  : john.doe@tenant.onmicrosoft.com
DisplayName        : John Doe
AccountEnabled     : True
```
Success if user details are shown.

## Related

- [[commands/set-azuread-user-password-by-upn]]
- [[procedures/Azure-AD-Administrative-Unit-Management]]
