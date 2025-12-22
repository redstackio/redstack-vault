---
type: command
executor: powershell
data: Get-ADDomainController -Filter * | Select-Object Name
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - reconnaissance
  - active-directory
  - powershell
verified: true
validated: true
---

# get-addomaincontroller-list-all

## Command

```powershell
Get-ADDomainController -Filter * | Select-Object Name
```

## Description

Retrieves a list of all domain controllers in the current AD domain using the Active Directory PowerShell module, filtering for all and selecting names.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Filter * | Queries all DC objects | Yes |
| Select-Object Name | Outputs only the Name property | Yes |

## Examples

### Basic Usage

```powershell
Get-ADDomainController -Filter * | Select-Object Name
```

### With Additional Properties

```powershell
Get-ADDomainController -Filter * | Select-Object Name, IPv4Address
```

## Expected Output

Name
----
DC01
DC02

## Related

- [[procedures/Active-Directory-Domain-Controller-Lookup]]
