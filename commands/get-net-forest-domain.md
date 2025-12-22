---
id: 97886fb0-7e94-4021-bd94-e575a320698e
type: command
executor: powershell
data: Get-NetForestDomain
output: null
created_at: '2023-04-06T03:56:02.230955+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Enumerate Forest Domains

## Command

```powershell
Get-NetForestDomain
```

## Description

Lists domains in the forest.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Current forest | No |

## Examples

### Basic Usage

```powershell
Get-NetForestDomain
```

## Expected Output

Forest domain list.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
