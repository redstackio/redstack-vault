---
type: command
executor: powershell
data: >-
  Get-ADGroup -LDAPFilter "(objectCategory=group)(adminCount=1)" -Properties
  adminCount
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - active-directory
  - enumeration
verified: true
validated: true
---

# powershell-get-adgroup-admincount

## Command

```powershell
Get-ADGroup -LDAPFilter "(objectCategory=group)(adminCount=1)" -Properties adminCount
```

## Description

Enumerates all groups in the Active Directory domain with AdminCount set to 1 using the ActiveDirectory module.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -LDAPFilter | LDAP filter for groups with adminCount=1 | Yes |
| -Properties | Retrieves adminCount property | No |

## Examples

### Basic Usage

```powershell
Get-ADGroup -LDAPFilter "(objectCategory=group)(adminCount=1)"
```

### Advanced Usage

```powershell
Get-ADGroup -LDAPFilter "(objectCategory=group)(adminCount=1)" | Select Name, adminCount
```

## Expected Output

```
DistinguishedName : CN=Domain Admins,CN=Users,DC=domain,DC=com
Name              : Domain Admins
adminCount        : 1
```

## Related

- [[procedures/AdminCount-Abuse]]
- [[commands/powershell-get-aduser-admincount]]
