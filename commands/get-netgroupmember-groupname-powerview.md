---
id: e2ba6d1d-af6e-43f5-9e65-becb4d7e3a48
name: get-netgroupmember-groupname-powerview
type: command
executor: powershell
data: Get-NetGroupMember -GroupName "Domain Admins"
output: null
created_at: '2023-04-06T03:56:02.229630+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - Active Directory
  - Enumeration
  - PowerView
verified: true
validated: true
---

# get-netgroupmember-groupname-powerview

## Command

```powershell
Get-NetGroupMember -GroupName "Domain Admins"
```

## Description

This PowerShell command from PowerView enumerates all members (users and groups) of a specified Active Directory group. It is used to verify if target users belong to privileged groups during discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-GroupName` | The name of the group to query members for (e.g., `Domain Admins`) | Yes |
| `-Domain` | Optional domain specifier if querying a non-current domain | No |

## Examples

### Basic Usage

```powershell
Get-NetGroupMember -GroupName "Domain Admins"
```

### Advanced Usage

```powershell
Get-NetGroupMember -GroupName "Domain Admins" -Domain "child.domain.com" | Select MemberName, MemberDomain
```

## Expected Output

```

MemberName             : john.doe
MemberDomain           : domain.com
MemberType             : User
IsGroup                : False
IsSecurity             : True
```

A list of members with details like name, domain, and type. Presence of target users confirms membership.

## Related

- [[procedures/Enumerate-User-Group-Membership-in-Active-Directory]]
- [[commands/get-netgroup-username-powerview]]
