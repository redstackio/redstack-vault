---
id: 610622fc-af92-4ba7-bcab-20136a8128ed
type: command
executor: powershell
data: Get-AvailableVMDisks ; Get-VMDisk
output: null
created_at: '2023-04-06T03:56:14.586956+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
tags:
  - vm
  - disk
verified: true
validated: true
---

# powerzure-get-available-vm-disks

## Command

```powershell
Get-AvailableVMDisks ; Get-VMDisk
```

## Description

Lists available VM disks and downloads a specific one for offline analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Enumerates in current subscription | No |

## Examples

### Basic Usage

```powershell
Get-AvailableVMDisks ; Get-VMDisk -DiskName targetdisk
```

## Expected Output

Disk list and download progress.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/PowerZure]]
