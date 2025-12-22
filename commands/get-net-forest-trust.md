---
id: 8678470d-c44a-4559-80ad-12a42712e497
type: command
executor: powershell
data: Get-NetForestTrust
output: null
created_at: '2023-04-06T03:56:02.230979+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Map Forest Trust

## Command

```powershell
Get-NetForestTrust
```

## Description

Maps trust relationships in the forest.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Current forest | No |

## Examples

### Basic Usage

```powershell
Get-NetForestTrust
```

## Expected Output

Forest trust details.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
