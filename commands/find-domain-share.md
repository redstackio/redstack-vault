---
id: dff86b86-d2ca-4861-91e7-43288d143f17
type: command
executor: powershell
data: Find-DomainShare
output: null
created_at: '2023-04-06T03:56:02.229924+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Enumerate Domain Shares

## Command

```powershell
Find-DomainShare
```

## Description

Lists all shares in the domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | All shares | No |

## Examples

### Basic Usage

```powershell
Find-DomainShare
```

## Expected Output

Share paths, types, notes.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
