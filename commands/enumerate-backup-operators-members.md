---
id: new-uuid-for-enumerate
name: enumerate-backup-operators-members
type: command
executor: powershell
data: Get-NetGroupMember -Identity "Backup Operators" -Recurse
output: null
created_at: '2023-04-06T03:56:06.525883+00:00'
updated_at: '2023-04-10T20:26:17.815665+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - active-directory
verified: true
validated: true
---

# enumerate-backup-operators-members

## Command

```powershell
Get-NetGroupMember -Identity "Backup Operators" -Recurse
```

## Description

This command uses the PowerView module to enumerate all members of the Backup Operators group in Active Directory, including recursive membership from nested groups. It is useful for identifying accounts with SeBackupPrivilege during reconnaissance or privilege verification in a compromised environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity | Name of the group to query (e.g., "Backup Operators") | Yes |
| -Recurse | Includes members from nested groups | No |

## Examples

### Basic Usage

```powershell
Get-NetGroupMember -Identity "Backup Operators"
```

### With Recursion

```powershell
Get-NetGroupMember -Identity "Backup Operators" -Recurse
```

## Expected Output

A table listing group members with columns like MemberName, MemberDomain, MemberSID, and GroupDomain. For example:

MemberName          MemberDomain    MemberSID
----------          ------------    ---------
Administrator       DOMAIN          S-1-5-21-...-500
UserAccount         DOMAIN          S-1-5-21-...-1001

## Related

- [[procedures/Abusing-Backup-Operators-Group-for-Sensitive-File-Access]]
- [[PowerView-Group-Enumeration]]
