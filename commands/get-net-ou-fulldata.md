---
id: 34d57516-4621-43b8-b94f-b6a666571870
type: command
executor: powershell
data: Get-NetOU -FullData
output: null
created_at: '2023-04-06T03:56:02.230280+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Net OU Full Data

## Command

```powershell
Get-NetOU -FullData
```

## Description

Enumerates all OUs with full details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -FullData | All OU properties | No |

## Examples

### Basic Usage

```powershell
Get-NetOU -FullData
```

## Expected Output

OU structure details.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
