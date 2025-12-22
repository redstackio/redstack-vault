---
id: c722b4f8-26d5-4bab-908a-d32524f9291a
type: command
executor: powershell
data: 'Get-DomainGPOLocalGroup | Select-Object GPODisplayName, GroupName'
output: null
created_at: '2023-04-06T03:56:02.229800+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get GPOs Modifying Local Group Memberships

## Command

```powershell
Get-DomainGPOLocalGroup | Select-Object GPODisplayName, GroupName
```

## Description

Finds GPOs that modify local group memberships.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Selects display name and group | No |

## Examples

### Basic Usage

```powershell
Get-DomainGPOLocalGroup | Select-Object GPODisplayName, GroupName
```

## Expected Output

GPO and group pairs.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
