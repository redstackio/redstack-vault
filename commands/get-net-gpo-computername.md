---
id: 263e8790-80cf-4775-bf86-0c1f2ac22274
type: command
executor: powershell
data: Get-NetGPO -ComputerName $_COMPUTER_NAME
output: null
created_at: '2023-04-06T03:56:02.230115+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Active Policy on Machine

## Command

```powershell
Get-NetGPO -ComputerName $_COMPUTER_NAME
```

## Description

Retrieves GPOs applied to a specific machine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName | Machine name | Yes |

## Examples

### Basic Usage

```powershell
Get-NetGPO -ComputerName 'PC01'
```

## Expected Output

Applied GPO list.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
