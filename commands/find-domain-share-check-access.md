---
id: bf26a184-4f02-4bdd-aee0-ba7b82241606
type: command
executor: powershell
data: Find-DomainShare -CheckShareAccess
output: null
created_at: '2023-04-06T03:56:02.229958+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Enumerate Domain Shares with User Access

## Command

```powershell
Find-DomainShare -CheckShareAccess
```

## Description

Checks which domain shares the current user can access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -CheckShareAccess | Tests access | No |

## Examples

### Basic Usage

```powershell
Find-DomainShare -CheckShareAccess
```

## Expected Output

Accessible shares only.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
