---
type: command
executor: powershell
data: '([adsisearcher]''(AdminCount=1)'').FindAll() | ForEach-Object { $_.Properties }'
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

# powershell-adsisearcher-admincount

## Command

```powershell
([adsisearcher]'(AdminCount=1)').FindAll() | ForEach-Object { $_.Properties }
```

## Description

Uses the .NET DirectorySearcher class to query Active Directory for all objects with AdminCount=1, without requiring the ActiveDirectory module.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '(AdminCount=1)' | LDAP filter for adminCount=1 | Yes |
| FindAll() | Executes the search | Yes |

## Examples

### Basic Usage

```powershell
([adsisearcher]'(AdminCount=1)').FindAll()
```

### Advanced Usage

```powershell
([adsisearcher]'(AdminCount=1)').FindAll() | Select -ExpandProperty properties | Select name
```

## Expected Output

```
adminCount : {1}
name       : {Admin User}
dn         : {CN=Admin User,CN=Users,DC=domain,DC=com}
```

## Related

- [[procedures/AdminCount-Abuse]]
- [[commands/powershell-get-aduser-admincount]]
