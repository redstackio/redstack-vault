---
type: command
executor: powershell
data: >-
  Get-DomainObjectAcl -Identity "$_GPO_IDENTITY" -ResolveGUIDs | Where-Object
  {($_.ActiveDirectoryRights.ToString() -match
  "GenericWrite|AllExtendedWrite|WriteDacl|WriteProperty|WriteMember|GenericAll|WriteOwner")}
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - active-directory
  - acl-enumeration
verified: true
validated: true
---

# Get-DomainObjectAcl-Filter-Write-Access

## Command

```powershell
Get-DomainObjectAcl -Identity "$_GPO_IDENTITY" -ResolveGUIDs | Where-Object {($_.ActiveDirectoryRights.ToString() -match "GenericWrite|AllExtendedWrite|WriteDacl|WriteProperty|WriteMember|GenericAll|WriteOwner")}
```

## Description

This PowerShell command, part of the PowerView module, retrieves the access control list (ACL) for a specified Active Directory object (e.g., a GPO) and filters it to show only entries granting write-related permissions. Use this during Active Directory enumeration to identify misconfigured GPOs that can be exploited for policy modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_GPO_IDENTITY | The name or GUID of the GPO or AD object to query (e.g., "SuperSecureGPO") | Yes |
| -ResolveGUIDs | Resolves GUIDs in the ACL to friendly names for readability | No (recommended) |
| -match "GenericWrite\|..." | Regex pattern matching write rights; customize as needed | Built-in |

## Examples

### Basic Usage

```powershell
Get-DomainObjectAcl -Identity "Default Domain Policy" -ResolveGUIDs | Where-Object {($_.ActiveDirectoryRights.ToString() -match "GenericWrite")}
```

### Advanced Usage

```powershell
Get-DomainGPO -All | ForEach-Object { Get-DomainObjectAcl -Identity $_.Name -ResolveGUIDs | Where-Object {($_.ActiveDirectoryRights.ToString() -match "WriteDacl|GenericAll") } }
```

## Expected Output

A filtered list of ACL entries, e.g.:

Identity                  : SuperSecureGPO
ActiveDirectoryRights     : GenericWrite
AccessControlType         : Allow
SecurityIdentifier        : S-1-5-21-... (Domain Users)

This indicates the queried group has write access to the GPO.

## Related

- [[Related Procedure: Exploit-Group-Policy-Objects-with-Write-Access]]
- [[Related Command: Get-DomainGPO-All]]
