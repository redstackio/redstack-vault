---
id: 59ce86ed-852f-40d3-b482-b0007eedbc7a
name: get-ad-forest-by-identity
type: command
executor: powershell
data: Get-ADForest -Identity <ForestName>
output: null
created_at: '2023-04-06T03:56:02.419973+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
platforms:
  - Windows
tags:
  - ad-recon
  - forest-enumeration
verified: true
validated: true
---

# get-ad-forest-by-identity

## Command

```powershell
Get-ADForest -Identity $_ForestName
```

## Description

Queries a specific Active Directory forest by name to retrieve its configuration details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_ForestName | FQDN of the target forest | Yes |

## Examples

### Basic Usage

```powershell
Get-ADForest -Identity "example.com"
```

### With Error Handling

```powershell
try { Get-ADForest -Identity "example.com" } catch { Write-Output "Forest not found" }
```

## Expected Output

Similar to default forest query but for the specified forest:

```
Name                  : example.com
Domains               : {example.com}
...
```

## Related

- [[procedures/active-directory-recon-using-ad-module]]
- [[commands/get-ad-forest-default]]
