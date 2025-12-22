---
id: a0a290e2-22f2-4cce-919d-a23465df7459
type: command
executor: powershell
data: Get-DomainGroup -Identity $_GROUP_NAME | Select-Object -ExpandProperty Member
output: null
created_at: '2023-04-06T03:56:02.229697+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Enumerate Group Members

## Command

```powershell
Get-DomainGroup -Identity $_GROUP_NAME | Select-Object -ExpandProperty Member
```

## Description

Expands members of a group by identity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity | Group identity | Yes |

## Examples

### Basic Usage

```powershell
Get-DomainGroup -Identity 'Domain Admins' | Select-Object -ExpandProperty Member
```

## Expected Output

Raw member DNs.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
