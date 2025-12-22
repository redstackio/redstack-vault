---
id: unknown
type: command
executor: powershell
data: Get-NetComputer -Ping
output: null
created_at: '2023-04-06T03:56:02.229600+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Net Computer Ping

## Command

```powershell
Get-NetComputer -Ping
```

## Description

Pings domain computers to find live hosts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Ping | Performs ping check | No |

## Examples

### Basic Usage

```powershell
Get-NetComputer -Ping
```

## Expected Output

Live computer list.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
