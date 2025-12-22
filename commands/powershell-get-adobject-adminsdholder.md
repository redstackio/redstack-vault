---
type: command
executor: powershell
data: >-
  Get-ADObject -Identity "CN=AdminSDHolder,CN=System,DC=$_DOMAIN,DC=com"
  -Properties adminCount
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - active-directory
  - query
verified: true
validated: true
---

# powershell-get-adobject-adminsdholder

## Command

```powershell
Get-ADObject -Identity "CN=AdminSDHolder,CN=System,DC=$_DOMAIN,DC=com" -Properties adminCount
```

## Description

Retrieves the AdminSDHolder object and its adminCount property to check the status of AD protection mechanisms.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity | Distinguished name of AdminSDHolder | Yes |
| -Properties | Includes adminCount | No |
| $_DOMAIN | Domain name (e.g., example) | Yes |

## Examples

### Basic Usage

```powershell
Get-ADObject -Identity "CN=AdminSDHolder,CN=System,DC=domain,DC=com"
```

### Advanced Usage

```powershell
Get-ADObject -Identity "CN=AdminSDHolder,CN=System,DC=domain,DC=com" -Properties * | Select adminCount, nTSecurityDescriptor
```

## Expected Output

```
DistinguishedName : CN=AdminSDHolder,CN=System,DC=domain,DC=com
adminCount        : 1
```

## Related

- [[procedures/AdminCount-Abuse]]
