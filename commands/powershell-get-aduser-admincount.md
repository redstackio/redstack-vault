---
type: command
executor: powershell
data: >-
  Get-ADUser -LDAPFilter "(objectCategory=person)(adminCount=1)" -Properties
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

# powershell-get-aduser-admincount

## Command

```powershell
Get-ADUser -LDAPFilter "(objectCategory=person)(adminCount=1)" -Properties adminCount
```

## Description

This PowerShell command uses the ActiveDirectory module to enumerate all user accounts in the domain that have the AdminCount attribute set to 1, indicating they are protected by AdminSDHolder.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -LDAPFilter | LDAP query string to filter users by adminCount=1 and objectCategory=person | Yes |
| -Properties | Specifies additional properties to retrieve, like adminCount | No |

## Examples

### Basic Usage

```powershell
Get-ADUser -LDAPFilter "(objectCategory=person)(adminCount=1)" -Properties adminCount | Select sAMAccountName, adminCount
```

### Advanced Usage

```powershell
Get-ADUser -LDAPFilter "(objectCategory=person)(adminCount=1)" -SearchBase "DC=domain,DC=com" -Properties adminCount, memberOf
```

## Expected Output

```
DistinguishedName : CN=Admin User,CN=Users,DC=domain,DC=com
Name              : Admin User
sAMAccountName    : adminuser
adminCount        : 1
```

## Related

- [[procedures/AdminCount-Abuse]]
- [[commands/powershell-get-adgroup-admincount]]
