---
id: dec9fd13-e799-43d4-a0b7-ab0baf6101b3
name: get-all-ad-groups
type: command
executor: powershell
data: Get-ADGroup -Filter *
output: null
created_at: '2023-04-06T03:56:02.419615+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
platforms:
  - Windows
tags:
  - ad-recon
  - group-enumeration
verified: true
validated: true
---

# get-all-ad-groups

## Command

```powershell
Get-ADGroup -Filter *
```

## Description

Lists all group objects in the domain to identify security and distribution groups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Filter * | Retrieves all groups | Yes |

## Examples

### Basic Usage

```powershell
Get-ADGroup -Filter *
```

### With Properties

```powershell
Get-ADGroup -Filter * -Properties GroupCategory
```

## Expected Output

Group list:

```
DistinguishedName : CN=Domain Admins,CN=Users,DC=contoso,DC=com
Name              : Domain Admins
GroupScope        : DomainLocal
...
```

## Related

- [[procedures/active-directory-recon-using-ad-module]]
- [[commands/get-all-ad-computers]]
