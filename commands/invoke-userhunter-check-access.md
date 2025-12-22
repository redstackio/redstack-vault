---
id: 65f23d5c-6d62-48ca-a4c8-9cf28ebe9fdb
type: command
executor: powershell
data: Invoke-UserHunter -CheckAccess
output: null
created_at: '2023-04-06T03:56:02.231293+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Confirm Admin Access

## Command

```powershell
Invoke-UserHunter -CheckAccess
```

## Description

Confirms administrative access on hunted machines.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -CheckAccess | Verifies access | No |

## Examples

### Basic Usage

```powershell
Invoke-UserHunter -CheckAccess
```

## Expected Output

Access confirmation.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
