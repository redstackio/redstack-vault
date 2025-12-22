---
id: 748a1f6a-01db-4c3b-8346-af1bc2f24954
type: command
executor: powershell
data: Find-LocalAdminAccess -Verbose
output: null
created_at: '2023-04-06T03:56:02.231133+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Find Machines Where Current User Has Local Admin Access

## Command

```powershell
Find-LocalAdminAccess -Verbose
```

## Description

Identifies machines where the current user has local admin rights.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Verbose | Detailed output | No |

## Examples

### Basic Usage

```powershell
Find-LocalAdminAccess -Verbose
```

## Expected Output

Accessible admin machines.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
