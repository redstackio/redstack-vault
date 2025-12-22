---
id: ff9c4dce-fc93-4e30-8eba-fa9f596e791e
type: command
executor: powershell
data: Invoke-UserHunter
output: null
created_at: '2023-04-06T03:56:02.231218+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Find Computers Where Domain Admin Has Session

## Command

```powershell
Invoke-UserHunter
```

## Description

Hunts for sessions of domain admins or specified users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Defaults to Domain Admins | No |

## Examples

### Basic Usage

```powershell
Invoke-UserHunter
```

## Expected Output

Machines with DA sessions.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
