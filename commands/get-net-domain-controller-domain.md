---
id: 00b0fb72-5e1b-4be1-ba07-c546e80a3ead
type: command
executor: powershell
data: Get-NetDomainController -Domain $_DOMAIN_NAME
output: null
created_at: '2023-04-06T03:56:02.228808+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Domain Controllers for Specific Domain

## Command

```powershell
Get-NetDomainController -Domain $_DOMAIN_NAME
```

## Description

Lists domain controllers for a specified domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Domain | Target domain name (e.g., child.domain.com) | Yes |

## Examples

### Basic Usage

```powershell
Get-NetDomainController -Domain 'example.com'
```

## Expected Output

Filtered DC list similar to base command.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
