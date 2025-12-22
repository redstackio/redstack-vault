---
id: unknown
type: command
executor: powershell
data: Get-NetComputer -FullData
output: null
created_at: '2023-04-06T03:56:02.229400+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Net Computer Full Data

## Command

```powershell
Get-NetComputer -FullData
```

## Description

Retrieves full details of all domain computers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -FullData | Includes all properties | No |

## Examples

### Basic Usage

```powershell
Get-NetComputer -FullData
```

## Expected Output

Detailed computer objects.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
