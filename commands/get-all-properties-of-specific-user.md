---
id: 5a0e4b09-75e4-4ecd-8c0b-910aa2cd4aa3
name: get-all-properties-of-specific-user
type: command
executor: powershell
data: Get-ADUser -Identity <user> -Properties *
output: null
created_at: '2023-04-06T03:56:02.419419+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
platforms:
  - Windows
tags:
  - ad-recon
  - user-enumeration
verified: true
validated: true
---

# get-all-properties-of-specific-user

## Command

```powershell
Get-ADUser -Identity $_User -Properties *
```

## Description

Retrieves all properties for a specific AD user account to profile credentials and memberships.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_User | Username or DN of the target user | Yes |
| -Properties * | All available attributes | Yes |

## Examples

### Basic Usage

```powershell
Get-ADUser -Identity "jdoe" -Properties *
```

### Select Key Properties

```powershell
Get-ADUser -Identity "jdoe" -Properties * | Select Name, EmailAddress, MemberOf
```

## Expected Output

User object:

```
DistinguishedName : CN=John Doe,CN=Users,DC=contoso,DC=com
Name              : John Doe
EmailAddress      : jdoe@contoso.com
MemberOf          : {CN=Domain Users,...}
...
```

## Related

- [[procedures/active-directory-recon-using-ad-module]]
- [[commands/get-user-with-specific-string-in-description]]
