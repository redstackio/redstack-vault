---
id: 8a9aecb2-ddd2-4389-b417-7f53f5ed6e74
type: command
executor: powershell
data: Get-NetLoggedon -ComputerName $_COMPUTER_NAME
output: null
created_at: '2023-04-06T03:56:02.229311+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Enumerate User Logged on Machine

## Command

```powershell
Get-NetLoggedon -ComputerName $_COMPUTER_NAME
```

## Description

Lists users currently logged on to a specific machine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName | Target machine name | Yes |

## Examples

### Basic Usage

```powershell
Get-NetLoggedon -ComputerName 'SERVER01'
```

## Expected Output

Logged-on user list.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
