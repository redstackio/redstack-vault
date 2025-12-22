---
id: 9753a5c3-ac40-4157-a22d-3055a280528d
type: command
executor: powershell
data: (Get-DomainPolicy).\"system access\"
output: null
created_at: '2023-04-06T03:56:02.228521+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get System Access Policy Configuration

## Command

```powershell
(Get-DomainPolicy)."system access"
```

## Description

Extracts the system access policy from the domain policy, focusing on account lockout and password policies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Relies on prior Get-DomainPolicy execution | No |

## Examples

### Basic Usage

```powershell
(Get-DomainPolicy)."system access"
```

## Expected Output

Hashtable with keys like 'LockoutDuration', 'MinPwdLen', showing policy values.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
