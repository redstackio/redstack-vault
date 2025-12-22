---
id: 65ec7a77-f5ed-4e2c-b234-4247e5cf83f1
name: get-netgroup-username-powerview
type: command
executor: powershell
data: Get-NetGroup -UserName $USER
output: null
created_at: '2023-01-12T07:19:09.806499+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - Active Directory
  - Enumeration
  - PowerView
verified: true
validated: true
---

# get-netgroup-username-powerview

## Command

```powershell
Get-NetGroup -UserName $USER
```

## Description

This PowerShell command from the PowerView module queries Active Directory via LDAP to find all groups that contain a specified username as a member. It is ideal for stealthy enumeration in compromised environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-UserName` | The username to search for in group memberships (e.g., `john.doe`) | Yes |
| `$USER` | Placeholder for the target username | Yes |

## Examples

### Basic Usage

```powershell
Get-NetGroup -UserName "john.doe"
```

### Advanced Usage

```powershell
Get-NetGroup -UserName "john.doe" | Select Name, Description
```

## Expected Output

```

Name                  : Domain Admins
Description           : Designated administrators of the domain
GroupScope            : DomainLocal
GroupProperty         : SecurityEnabled, Universal
DistinguishedName     : CN=Domain Admins,CN=Users,DC=domain,DC=com
```

Output includes group details like name, description, and scope. Privileged groups indicate high-value access.

## Related

- [[procedures/Enumerate-User-Group-Membership-in-Active-Directory]]
- [[commands/get-adprincipalgroupmembership-user]]
