---
id: e729fcd8-3c73-483a-abff-1559cbcb5685
name: get-netuser-spn-filter-domain-admins-powerview
type: command
executor: powershell
data: 'Get-NetUser -SPN | Where-Object {$_.memberof -match ''Domain Admins''}'
output: null
created_at: '2023-01-12T17:49:32.489952+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - powerview
  - privilege-escalation
verified: true
validated: true
---

# get-netuser-spn-filter-domain-admins-powerview

## Command

```powershell
Get-NetUser -SPN | Where-Object {$_.memberof -match 'Domain Admins'}
```

## Description

This command uses PowerView to enumerate network users with SPNs and filters for those in the Domain Admins group, highlighting high-privilege Kerberoasting targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -SPN | Filters users with Service Principal Names | Yes |
| Where-Object | PowerShell filter for 'Domain Admins' in memberOf | Yes |

## Examples

### Basic Usage

```powershell
Get-NetUser -SPN | Where-Object {$_.memberof -match 'Domain Admins'}
```

### Advanced Usage

```powershell
Get-NetUser -SPN | Where-Object {$_.memberof -match 'Domain Admins'} | Select SamAccountName, MemberOf
```

## Expected Output

SamAccountName : admin-svc
MemberOf       : {CN=Domain Admins,CN=Users,DC=corp,DC=local}

(Filtered list; no output if no admin SPNs.)

## Related

- [[procedures/Find-Kerberoastable-Users-with-SPNs]]
