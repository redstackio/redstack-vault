---
id: 6eca2d60-0c30-409e-bdbe-864b7c62f2a5
name: get-domain-object-acl-powerview
type: command
executor: powershell
data: >-
  Get-DomainObjectAcl -Identity $GROUP_NAME2 -ResolveGUIDs | ForEach-Object {$_
  | Add-Member NoteProperty 'IdentityName' $(Convert-SidToName
  $_.SecurityIdentifier); $_} | ?{$_.IdentityName -match $GROUP_NAME1}
output: null
created_at: '2023-01-12T07:34:23.268830+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - acl
  - discovery
verified: true
validated: true
---

# get-domain-object-acl-powerview

## Command

```powershell
Get-DomainObjectAcl -Identity $GROUP_NAME2 -ResolveGUIDs | ForEach-Object {$_ | Add-Member NoteProperty 'IdentityName' $(Convert-SidToName $_.SecurityIdentifier); $_} | ?{$_.IdentityName -match $GROUP_NAME1}
```

## Description

This PowerShell command retrieves the full ACL for a specified AD object (group) using PowerView, resolves SIDs to names, adds a custom IdentityName property, and filters for matches against a principal group/user. It is used to drill down into specific ACEs after initial ACL enumeration to confirm abusable permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity | Specifies the target AD object (e.g., group name in $GROUP_NAME2) | Yes |
| -ResolveGUIDs | Resolves GUIDs and SIDs to readable names | Yes |
| $GROUP_NAME2 | Variable for the target group/object identity | Yes |
| $GROUP_NAME1 | Variable for the principal/group to filter ACEs against | Yes |
| ForEach-Object {...} | Processes each ACL entry to add IdentityName using Convert-SidToName | Yes |
| ?{...} | Where-Object filter to match IdentityName | Yes |

## Examples

### Basic Usage

```powershell
$GROUP_NAME2 = 'Domain Admins'
$GROUP_NAME1 = 'LowPrivUsers'
Get-DomainObjectAcl -Identity $GROUP_NAME2 -ResolveGUIDs | ForEach-Object {$_ | Add-Member NoteProperty 'IdentityName' $(Convert-SidToName $_.SecurityIdentifier); $_} | ?{$_.IdentityName -match $GROUP_NAME1}
```

### Advanced Usage

```powershell
$GROUP_NAME2 = 'Enterprise Admins'
$GROUP_NAME1 = 'Contractors'
Get-DomainObjectAcl -Identity $GROUP_NAME2 -ResolveGUIDs | ForEach-Object {$_ | Add-Member NoteProperty 'IdentityName' $(Convert-SidToName $_.SecurityIdentifier); $_} | ?{$_.IdentityName -match $GROUP_NAME1} | Format-Table IdentityName, ActiveDirectoryRights -AutoSize
```

## Expected Output

Outputs filtered ACE details, such as:

IdentityName         : DOMAIN\LowPrivUsers
ActiveDirectoryRights: AddMembers, WriteDacl
SecurityIdentifier   : S-1-5-21-...
AccessControlType    : Allow

Look for rights like AddMembers or GenericAll indicating potential abuse.

## Related

- [[procedures/Enumerate-Domain-Group-ACLs-for-Abuse]]
- [[commands/find-interesting-domain-acls-powerview]]
