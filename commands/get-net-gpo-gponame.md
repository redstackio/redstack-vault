---
id: d8cb6ef9-09a7-46be-a7dc-8f2e32ba125a
type: command
executor: powershell
data: Get-NetGPO -GPOname $_GPO_GUID
output: null
created_at: '2023-04-06T03:56:02.230401+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Net GPO

## Command

```powershell
Get-NetGPO -GPOname $_GPO_GUID
```

## Description

Retrieves a specific GPO by GUID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -GPOname | GPO GUID | Yes |

## Examples

### Basic Usage

```powershell
Get-NetGPO -GPOname '{GUID}'
```

## Expected Output

GPO details.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
