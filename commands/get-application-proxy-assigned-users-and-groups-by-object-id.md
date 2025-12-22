---
type: command
executor: powershell
data: Get-ApplicationProxyAssignedUsersAndGroups -ObjectId <OBJECT-ID>
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Azure AD
tags:
  - discovery
  - azure
verified: true
validated: true
---

# Get Application Proxy Assigned Users and Groups by Object ID

## Command

```powershell
Get-ApplicationProxyAssignedUsersAndGroups -ObjectId <OBJECT-ID>
```

## Description

This command uses a custom function to retrieve users and groups assigned to a specific Azure AD application (by Object ID), focusing on Application Proxy configurations to map access rights.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ObjectId | The Object ID of the target application or service principal | Yes |

## Examples

### Basic Usage

```powershell
Get-ApplicationProxyAssignedUsersAndGroups -ObjectId "12345678-1234-1234-1234-123456789abc"
```

### Advanced Usage

Pipe to format for readability:

```powershell
Get-ApplicationProxyAssignedUsersAndGroups -ObjectId "12345678-1234-1234-1234-123456789abc" | Format-Table UserPrincipalName, DisplayName -AutoSize
```

## Expected Output

List of assigned principals:

```
PrincipalType     PrincipalDisplayName     ObjectId
-------------     ---------------------     --------
User              john.doe@contoso.com     11111111-1111-1111-1111-111111111111
Group             Finance Users            22222222-2222-2222-2222-222222222222
```

## Related

- [[procedures/azure-application-proxy-enumeration]]
- [[commands/import-get-application-proxy-assigned-users-and-groups-script]]
