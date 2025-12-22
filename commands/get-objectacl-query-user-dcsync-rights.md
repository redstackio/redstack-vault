---
id: bd9cf456-5e57-4e1c-9a09-685580eb2635
name: get-objectacl-query-user-dcsync-rights
type: command
executor: powershell
data: >-
  Get-ObjectAcl -Identity "dc=$_DC1,dc=$_DC2" -ResolveGUIDs | ?
  {$_.SecurityIdentifier -match "$_SID"}
output: >-
  PS C:\> Get-ObjectAcl -Identity "dc=megabank,dc=local" -ResolveGUIDs | ?
  {$_.SecurityIdentifier -match "S-1-5-21-3072663084-364016917-1341370565-7601"}


  AceQualifier           : AccessAllowed

  ObjectDN               : DC=megabank,DC=local

  ActiveDirectoryRights  : ExtendedRight

  ObjectAceType          : DS-Replication-Get-Changes-In-Filtered-Set

  vObjectSID              : S-1-5-21-3072663084-364016917-1341370565

  InheritanceFlags       : None

  BinaryLength           : 56

  AceType                : AccessAllowedObject

  ObjectAceFlags         : ObjectAceTypePresent
created_at: '2020-03-20T22:38:48.722323+00:00'
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

# get-objectacl-query-user-dcsync-rights

## Command

```powershell
Get-ObjectAcl -Identity "dc=$_DC1,dc=$_DC2" -ResolveGUIDs | ? {$_.SecurityIdentifier -match "$_SID"}
```

## Description

This PowerView command queries Access Control Entries (ACEs) on the domain's naming context to check if a specific user SID has been granted replication privileges required for DCSync attacks. It resolves GUIDs for readability and filters for the target SID, identifying extended rights like DS-Replication-Get-Changes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity "dc=$_DC1,dc=$_DC2" | Specifies the domain DN (e.g., dc=megabank,dc=local) to query ACLs on | Yes |
| -ResolveGUIDs | Translates GUIDs to human-readable names for ACE types | Yes |
| ? {$_.SecurityIdentifier -match "$_SID"} | PowerShell filter to match the target user SID | Yes |
| $_DC1, $_DC2 | Domain components (e.g., megabank, local) | Yes |
| $_SID | The Security Identifier of the user to check (e.g., S-1-5-21-...) | Yes |

## Examples

### Basic Usage

```powershell
Get-ObjectAcl -Identity "dc=megabank,dc=local" -ResolveGUIDs | ? {$_.SecurityIdentifier -match "S-1-5-21-3072663084-364016917-1341370565-500"}
```

### Advanced Usage

```powershell
$sid = "S-1-5-21-3072663084-364016917-1341370565-500"; Get-ObjectAcl -Identity "dc=megabank,dc=local" -ResolveGUIDs | ? {$_.SecurityIdentifier -match $sid} | Select-Object ActiveDirectoryRights, ObjectAceType, AceQualifier
```

> This pipes to select key fields for quicker review of rights.

## Expected Output

```
PS C:\> Get-ObjectAcl -Identity "dc=megabank,dc=local" -ResolveGUIDs | ? {$_.SecurityIdentifier -match "S-1-5-21-3072663084-364016917-1341370565-7601"}

AceQualifier           : AccessAllowed
ObjectDN               : DC=megabank,DC=local
ActiveDirectoryRights  : ExtendedRight
ObjectAceType          : DS-Replication-Get-Changes-In-Filtered-Set
vObjectSID              : S-1-5-21-3072663084-364016917-1341370565
InheritanceFlags       : None
BinaryLength           : 56
AceType                : AccessAllowedObject
ObjectAceFlags         : ObjectAceTypePresent
```

## Related

- [[procedures/Query-Active-Directory-User-for-DCSync-Rights]]
- [[commands/get-aduser-list-users-with-sid]]
