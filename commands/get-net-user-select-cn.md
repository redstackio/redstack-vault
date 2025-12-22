---
id: ccbe37e1-50e0-4078-b22d-07daf7f771a2
type: command
executor: powershell
data: Get-NetUser | select cn
output: null
created_at: '2023-04-06T03:56:02.229081+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Net User with Select CN

## Command

```powershell
Get-NetUser | select cn
```

## Description

Lists common names (CN) of all domain users for quick reference.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Selects CN property | No |

## Examples

### Basic Usage

```powershell
Get-NetUser | select cn
```

## Expected Output

Column of CN values.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
