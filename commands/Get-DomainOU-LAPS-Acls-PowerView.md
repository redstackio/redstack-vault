---
id: a9b24e80-3402-4721-81af-e064ea076ae6
name: Get-DomainOU-LAPS-Acls-PowerView
type: command
executor: powershell
data: >-
  Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs | Where-Object
  {($_.ObjectAceType -like 'ms-Mcs-AdmPwd') -and ($_.ActiveDirectoryRights
  -match 'ReadProperty')} | ForEach-Object {$_ | Add-Member NoteProperty
  'IdentityName' $(Convert-SidToName $_.SecurityIdentifier); $_}
output: |-
  ObjectDN          : OU=Computers,DC=domain,DC=local
  AceType           : AccessAllowed
  ObjectAceType     : ms-Mcs-AdmPwd
  ActiveDirectoryRights: ReadProperty
  IdentityReference : DOMAIN\LAPSReaders
  IdentityName      : DOMAIN\LAPSReaders
  SecurityIdentifier: S-1-5-21-...-1111
created_at: '2023-01-12T18:59:53.015414+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - active-directory
verified: true
validated: true
---

# Get-DomainOU-LAPS-Acls-PowerView

## Command

```powershell
Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs | Where-Object {($_.ObjectAceType -like 'ms-Mcs-AdmPwd') -and ($_.ActiveDirectoryRights -match 'ReadProperty')} | ForEach-Object {$_ | Add-Member NoteProperty 'IdentityName' $(Convert-SidToName $_.SecurityIdentifier); $_}
```

## Description

This PowerShell command uses the PowerView module to enumerate all Organizational Units (OUs) in the current domain, retrieve their Access Control Entries (ACEs), resolve GUIDs to friendly names, and filter for permissions allowing ReadProperty access to the ms-Mcs-AdmPwd attribute used by LAPS. It enhances the output by adding resolved identity names for SIDs. Use this during Active Directory reconnaissance to identify who can read local admin passwords stored via LAPS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Get-DomainOU | Enumerates all OUs in the domain; no parameters needed | Built-in |
| Get-DomainObjectAcl | Retrieves ACLs for input objects; -ResolveGUIDs resolves GUIDs to names | Yes (flag) |
| Where-Object | Filters ACEs where ObjectAceType matches 'ms-Mcs-AdmPwd' and rights include 'ReadProperty' | Built-in |
| ForEach-Object | Adds a custom 'IdentityName' property by resolving the SecurityIdentifier SID | Built-in |
| Convert-SidToName | PowerView function to convert SID to account name; requires domain access | Implicit |

## Examples

### Basic Usage

```powershell
Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs | Where-Object {($_.ObjectAceType -like 'ms-Mcs-AdmPwd') -and ($_.ActiveDirectoryRights -match 'ReadProperty')} | ForEach-Object {$_ | Add-Member NoteProperty 'IdentityName' $(Convert-SidToName $_.SecurityIdentifier); $_}
```

Run directly in a PowerShell session with PowerView imported to list LAPS permissions.

### Advanced Usage

```powershell
Get-DomainOU -Domain domain.local | Get-DomainObjectAcl -ResolveGUIDs | Where-Object {($_.ObjectAceType -like 'ms-Mcs-AdmPwd') -and ($_.ActiveDirectoryRights -match 'ReadProperty')} | Export-Csv -Path laps_permissions.csv -NoTypeInformation
```

Specifies a target domain and exports results to CSV for offline analysis.

## Expected Output

Description of what output to expect when the command runs successfully.

```
ObjectDN          : OU=Computers,DC=domain,DC=local
AceType           : AccessAllowed
ObjectAceType     : ms-Mcs-AdmPwd
ActiveDirectoryRights: ReadProperty
IdentityReference : DOMAIN\LAPSReaders
IdentityName      : DOMAIN\LAPSReaders
SecurityIdentifier: S-1-5-21-1234567890-1234567890-1234567890-1111
InheritanceFlags  : None
PropagationFlags  : None
AccessControlType : Allow
IsInherited       : False

ObjectDN          : OU=Servers,DC=domain,DC=local
AceType           : AccessAllowed
ObjectAceType     : ms-Mcs-AdmPwd
ActiveDirectoryRights: ReadProperty
IdentityReference : DOMAIN\Admins
IdentityName      : DOMAIN\Domain Admins
SecurityIdentifier: S-1-5-21-1234567890-1234567890-1234567890-512
InheritanceFlags  : All
PropagationFlags  : InheritOnly
AccessControlType : Allow
IsInherited       : True
```

The output lists ACL entries for OUs with LAPS read permissions, including resolved identities. Empty output indicates no accessible LAPS configurations or insufficient permissions.

## Related

- [[procedures/Enumerate-OUs-for-LAPS-Permissions]]
- [[tools/PowerView]]
