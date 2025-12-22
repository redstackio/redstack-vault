---
id: ee988eda-92a8-459f-8e84-cf6dd95af577
type: command
executor: powershell
data: Get-NetUser -SamAccountName $_SAM_ACCOUNT_NAME
output: null
created_at: '2023-04-06T03:56:02.229053+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Net User with SamAccountName

## Command

```powershell
Get-NetUser -SamAccountName $_SAM_ACCOUNT_NAME
```

## Description

Retrieves details for a specific user by SamAccountName.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -SamAccountName | Username (e.g., 'admin') | Yes |

## Examples

### Basic Usage

```powershell
Get-NetUser -SamAccountName 'jdoe'
```

## Expected Output

Single user object details.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
