---
id: 016abdac-4e78-4953-ac46-572f4e39356e
name: enumerate-domains-of-forest
type: command
executor: powershell
data: (Get-ADForest).Domains
output: null
created_at: '2023-04-06T03:56:02.420033+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
platforms:
  - Windows
tags:
  - ad-recon
  - forest-enumeration
verified: true
validated: true
---

# enumerate-domains-of-forest

## Command

```powershell
(Get-ADForest).Domains
```

## Description

This command extracts the list of domains within the current Active Directory forest, providing a quick overview of the domain structure for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses the current forest context | No |

## Examples

### Basic Usage

```powershell
(Get-ADForest).Domains
```

### With Output to Variable

```powershell
$domains = (Get-ADForest).Domains; $domains | ForEach-Object { Write-Output $_ }
```

## Expected Output

A string array listing domain names, e.g.:

```
contoso.com
child.contoso.com
```

## Related

- [[procedures/active-directory-recon-using-ad-module]]
- [[commands/get-ad-forest-default]]
