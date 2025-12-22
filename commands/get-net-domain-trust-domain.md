---
id: 1c344650-ae3a-4c9b-a7cd-070e4c4931d0
type: command
executor: powershell
data: Get-NetDomainTrust -Domain $_DOMAIN_NAME
output: null
created_at: '2023-04-06T03:56:02.230810+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Net Domain Trust with Domain Name

## Command

```powershell
Get-NetDomainTrust -Domain $_DOMAIN_NAME
```

## Description

Gets trusts for a specific domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Domain | Domain name | Yes |

## Examples

### Basic Usage

```powershell
Get-NetDomainTrust -Domain 'child.com'
```

## Expected Output

Specific trusts.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
