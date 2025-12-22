---
id: 4dee54ec-0fb1-4c20-9475-8979a6e97572
type: command
executor: powershell
data: Get-NetDomainTrust
output: null
created_at: '2023-04-06T03:56:02.230793+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Net Domain Trust

## Command

```powershell
Get-NetDomainTrust
```

## Description

Enumerates trust relationships in the domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Current domain trusts | No |

## Examples

### Basic Usage

```powershell
Get-NetDomainTrust
```

## Expected Output

Trust details like Name, TrustType, Direction.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
