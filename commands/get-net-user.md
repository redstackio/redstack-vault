---
id: 61a984ec-c884-427d-a5d4-779423440995
type: command
executor: powershell
data: Get-NetUser
output: null
created_at: '2023-04-06T03:56:02.228963+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Net User

## Command

```powershell
Get-NetUser
```

## Description

Enumerates all domain users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | All users in domain | No |

## Examples

### Basic Usage

```powershell
Get-NetUser
```

## Expected Output

List of user objects with SamAccountName, Description, etc.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
