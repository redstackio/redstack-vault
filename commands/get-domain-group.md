---
id: unknown
type: command
executor: powershell
data: Get-DomainGroup
output: null
created_at: '2023-04-06T03:56:02.229500+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Domain Group

## Command

```powershell
Get-DomainGroup
```

## Description

Enumerates all domain groups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | All groups | No |

## Examples

### Basic Usage

```powershell
Get-DomainGroup
```

## Expected Output

Group list.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
