---
id: c74dca4a-cc76-4d97-bec3-580b93cd94e0
type: command
executor: powershell
data: Find-GPOComputerAdmin -ComputerName $_COMPUTER_NAME
output: null
created_at: '2023-04-06T03:56:02.230160+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Users in Local Admin Group

## Command

```powershell
Find-GPOComputerAdmin -ComputerName $_COMPUTER_NAME
```

## Description

Finds users in a machine's local admin group via GPO.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName | Target machine | Yes |

## Examples

### Basic Usage

```powershell
Find-GPOComputerAdmin -ComputerName 'PC01'
```

## Expected Output

Admin user list.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
