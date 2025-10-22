---
id: bd9cf456-5e57-4e1c-9a09-685580eb2635
name: Query Active Directory User by SID for DCSync Rights
type: command
executor: powershell
data: Get-ObjectAcl -Identity "dc=$_DC1,dc=$_DC2" -ResolveGUIDs | ? {$_.SecurityIdentifier
  -match "$_SID"}
output: 'PS C:\> Get-ObjectAcl -Identity "dc=megabank,dc=local" -ResolveGUIDs | ?
  {$_.SecurityIdentifier -match "S-1-5-21-3072663084-364016917-1341370565-7601"}

  AceQualifier           : AccessAllowed

  ObjectDN               : DC=megabank,DC=local

  ActiveDirectoryRights  : ExtendedRight

  ObjectAceType          : DS-Replication-Get-Changes-In-Filtered-Set

  vObjectSID              : S-1-5-21-3072663084-364016917-1341370565

  InheritanceFlags       : None

  BinaryLength           : 56

  AceType                : AccessAllowedObject

  ObjectAceFlags         : ObjectAceTypePresent'
created_at: '2020-03-20T22:38:48.722323+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Query Active Directory User by SID for DCSync Rights

```powershell
Get-ObjectAcl -Identity "dc=$_DC1,dc=$_DC2" -ResolveGUIDs | ? {$_.SecurityIdentifier -match "$_SID"}
```

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
