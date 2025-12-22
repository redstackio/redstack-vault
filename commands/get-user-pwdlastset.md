---
id: ed7b2e45-d3f0-473e-8c4c-648ac4ff9577
type: command
executor: powershell
data: Get-UserProperty -Properties pwdlastset
output: null
created_at: '2023-04-06T03:56:02.229192+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Check Last Password Change

## Command

```powershell
Get-UserProperty -Properties pwdlastset
```

## Description

Checks the last password set timestamp for users to identify stale accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Properties | Specifies pwdlastset | Yes |

## Examples

### Basic Usage

```powershell
Get-UserProperty -Properties pwdlastset
```

## Expected Output

Timestamps for password changes.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
