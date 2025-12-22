---
id: 84d815b3-0f9b-419f-84e5-bbc6cd24533c
type: command
executor: powershell
data: Get-NetSession -ComputerName $_COMPUTER_NAME
output: null
created_at: '2023-04-06T03:56:02.229365+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Enumerate Session Information for Machine

## Command

```powershell
Get-NetSession -ComputerName $_COMPUTER_NAME
```

## Description

Retrieves session information for users on a machine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName | Target machine | Yes |

## Examples

### Basic Usage

```powershell
Get-NetSession -ComputerName 'SERVER01'
```

## Expected Output

Session details like UserName, IdleTime.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
