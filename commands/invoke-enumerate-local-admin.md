---
id: 4e5162ce-9a7a-4294-9190-906b7e642562
type: command
executor: powershell
data: Invoke-EnumerateLocalAdmin -Verbose
output: null
created_at: '2023-04-06T03:56:02.231175+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Find Local Admins on All Machines of the Domain

## Command

```powershell
Invoke-EnumerateLocalAdmin -Verbose
```

## Description

Enumerates local admins across all domain machines.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Verbose | Detailed output | No |

## Examples

### Basic Usage

```powershell
Invoke-EnumerateLocalAdmin -Verbose
```

## Expected Output

Admin mappings per machine.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
