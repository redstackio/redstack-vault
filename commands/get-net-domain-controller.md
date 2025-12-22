---
id: 0ea4acba-de84-4cfc-b8e5-184ccd535f41
type: command
executor: powershell
data: Get-NetDomainController
output: null
created_at: '2023-04-06T03:56:02.228737+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Domain Controllers

## Command

```powershell
Get-NetDomainController
```

## Description

Enumerates domain controllers in the current domain, providing details for targeting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Current domain | No |

## Examples

### Basic Usage

```powershell
Get-NetDomainController
```

## Expected Output

Table with ComputerName, IPv4Address, OperatingSystem, Site.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
