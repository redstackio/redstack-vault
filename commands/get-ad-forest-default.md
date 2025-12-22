---
id: cddbcd3b-d2f8-42b5-89ec-b7a22f16b37a
name: get-ad-forest-default
type: command
executor: powershell
data: Get-ADForest
output: null
created_at: '2023-04-06T03:56:02.419914+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
platforms:
  - Windows
tags:
  - ad-recon
  - forest-enumeration
verified: true
validated: true
---

# get-ad-forest-default

## Command

```powershell
Get-ADForest
```

## Description

Retrieves detailed properties of the current Active Directory forest, including domains, sites, and configuration partitions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Defaults to current forest | No |

## Examples

### Basic Usage

```powershell
Get-ADForest
```

### Select Specific Properties

```powershell
Get-ADForest | Select-Object Name, Domains
```

## Expected Output

Forest object with properties like:

```
Name                  : contoso.com
Domains               : {contoso.com, child.contoso.com}
...
```

## Related

- [[procedures/active-directory-recon-using-ad-module]]
- [[commands/enumerate-domains-of-forest]]
