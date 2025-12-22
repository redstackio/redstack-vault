---
type: command
executor: powershell
data: '. C:\\Tools\\GetApplicationProxyAssignedUsersAndGroups.ps1'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Azure AD
tags:
  - discovery
  - azure
  - script
verified: true
validated: true
---

# Import Get Application Proxy Assigned Users and Groups Script

## Command

```powershell
. C:\Tools\GetApplicationProxyAssignedUsersAndGroups.ps1
```

## Description

This command dot-sources (imports) a custom PowerShell script that defines the Get-ApplicationProxyAssignedUsersAndGroups function for enumerating user and group assignments to Application Proxy applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | Full path to the .ps1 script file | Yes (hardcoded as C:\Tools\GetApplicationProxyAssignedUsersAndGroups.ps1) |

## Examples

### Basic Usage

```powershell
. C:\Tools\GetApplicationProxyAssignedUsersAndGroups.ps1
```

### Advanced Usage

Import from a different path:

```powershell
. .\Scripts\GetApplicationProxyAssignedUsersAndGroups.ps1
```

## Expected Output

No output on success; the function is now available. Verify with:

```powershell
Get-Command Get-ApplicationProxyAssignedUsersAndGroups
```

Output:

```
CommandType     Name                                Version    Source
-----------     ----                                -------    ------
Function        Get-ApplicationProxyAssignedUsersAndGroups
```

## Related

- [[procedures/azure-application-proxy-enumeration]]
- [[commands/get-application-proxy-assigned-users-and-groups-by-object-id]]
