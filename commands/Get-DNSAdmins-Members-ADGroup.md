---
id: aad84aaf-ba66-4fff-8ee1-d9a47881c7d9
name: Get-DNSAdmins-Members-ADGroup
type: command
executor: powershell
data: Get-ADGroupMember -Identity DNSAdmins
output: null
created_at: '2023-04-06T03:56:06.474672+00:00'
updated_at: '2023-10-10T20:26:10.325254+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - enumeration
verified: true
validated: true
---

# Get-DNSAdmins-Members-ADGroup

## Command

```powershell
Get-ADGroupMember -Identity DNSAdmins
```

## Description

This native Active Directory cmdlet retrieves members of the DNSAdmins group, useful for confirming access rights in privilege escalation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity | Name or DN of the group (e.g., DNSAdmins) | Yes |

## Examples

### Basic Usage

```powershell
Get-ADGroupMember -Identity DNSAdmins
```

## Expected Output

```
distinguishedName : CN=user1,CN=Users,DC=domain,DC=com
Name              : user1
objectClass       : user
...
```

A list of member objects with DNs and classes.

## Related

- [[procedures/Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation]]
