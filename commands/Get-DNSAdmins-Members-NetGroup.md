---
id: b9188f49-51b8-454b-9fb7-b72c6a6e3787
name: Get-DNSAdmins-Members-NetGroup
type: command
executor: powershell
data: Get-NetGroupMember -GroupName "DNSAdmins"
output: null
created_at: '2023-04-06T03:56:06.474584+00:00'
updated_at: '2023-10-10T20:26:10.325254+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - enumeration
verified: true
validated: true
---

# Get-DNSAdmins-Members-NetGroup

## Command

```powershell
Get-NetGroupMember -GroupName "DNSAdmins"
```

## Description

This PowerView command enumerates members of the DNSAdmins group in the current Active Directory domain, helping identify accounts eligible for DNS configuration abuse.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -GroupName | Name of the group to query (e.g., "DNSAdmins") | Yes |

## Examples

### Basic Usage

```powershell
Get-NetGroupMember -GroupName "DNSAdmins"
```

## Expected Output

```
MemberName            : user1
MemberDomain          : DOMAIN
MemberSID             : S-1-5-21-...-1001
...
```

A table listing group members with names, domains, and SIDs.

## Related

- [[procedures/Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation]]
