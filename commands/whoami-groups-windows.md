---
id: 5ba0d3fe-a687-41cf-b9e2-da04cb9fb6b9
name: whoami-groups-windows
type: command
executor: cmd
data: whoami /groups
output: null
created_at: '2023-04-06T03:56:28.626541+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - discovery
verified: true
validated: true
---

# whoami-groups-windows

## Command

```cmd
whoami /groups
```

## Description

Displays the current user's group memberships, including SIDs, attributes, and types, useful for identifying admin or domain group affiliations during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /groups | Lists all group memberships for the current user | Yes |

## Examples

### Basic Usage

```cmd
whoami /groups
```

### With Filtering (manual post-process)

Pipe to findstr for specific groups: `whoami /groups | findstr Administrators`

## Expected Output

```
GROUP NAME                                    TYPE             SID          ATTRIBUTES
=====================================================================================================
BUILTIN\Administrators                        Alias            S-1-5-32-544 Enabled
BUILTIN\Users                                 Alias            S-1-5-32-545 Enabled
NT AUTHORITY\INTERACTIVE                      WellKnownGroup   S-1-1-1       Enabled
...
```

Shows groups with enabled status; look for high-priv like Domain Admins.

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/whoami-privileges-windows]]
