---
id: cbd5d7f4-8821-40c5-be9e-ad8eb06f74e6
name: get-adprincipalgroupmembership-user
type: command
executor: powershell
data: Get-ADPrincipalGroupMembership -Identity $USER | Select Name
output: null
created_at: '2023-01-12T07:19:09.807764+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - Active Directory
  - Enumeration
verified: true
validated: true
---

# get-adprincipalgroupmembership-user

## Command

```powershell
Get-ADPrincipalGroupMembership -Identity $USER | Select Name
```

## Description

This PowerShell command uses the Active Directory module to retrieve all group memberships for a specified user identity, filtering to display only group names. It is used during domain enumeration to identify privileged group associations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-Identity` | The username or distinguished name of the target user (e.g., `john.doe`) | Yes |
| `$USER` | Placeholder for the user identity to query | Yes |
| `| Select Name` | Pipes output to select only the `Name` property for concise results | No |

## Examples

### Basic Usage

```powershell
Get-ADPrincipalGroupMembership -Identity "john.doe" | Select Name
```

### Advanced Usage

```powershell
Get-ADPrincipalGroupMembership -Identity "CN=John Doe,OU=Users,DC=domain,DC=com" | Select Name, DistinguishedName
```

## Expected Output

```

Name
----
Domain Users
Domain Admins
Enterprise Admins
```

A list of group names the user belongs to. If the user is in privileged groups, they will appear in the output, indicating potential escalation paths.

## Related

- [[procedures/Enumerate-User-Group-Membership-in-Active-Directory]]
- [[commands/get-netgroup-username-powerview]]
