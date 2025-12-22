---
id: unknown
type: command
executor: powershell
data: Get-NetForestDomain Forest $_FOREST_NAME
output: null
created_at: '2023-04-06T03:56:02.231000+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Net Forest Domain with Forest

## Command

```powershell
Get-NetForestDomain Forest $_FOREST_NAME
```

## Description

Enumerates domains in a specific forest.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Forest | Forest name | Yes |

## Examples

### Basic Usage

```powershell
Get-NetForestDomain Forest 'forest.com'
```

## Expected Output

Specified forest domains.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
