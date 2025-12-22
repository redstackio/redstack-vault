---
id: e2ba6d1d-af6e-43f5-9e65-becb4d7e3a48
type: command
executor: powershell
data: Get-NetGroupMember -GroupName \"$_GROUP_NAME\" -Domain $_DOMAIN_NAME
output: null
created_at: '2023-04-06T03:56:02.229630+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Get Group Members

## Command

```powershell
Get-NetGroupMember -GroupName "$_GROUP_NAME" -Domain $_DOMAIN_NAME
```

## Description

Lists members of a specific domain group.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -GroupName | Group name (e.g., 'Domain Admins') | Yes |
| -Domain | Domain name | Yes |

## Examples

### Basic Usage

```powershell
Get-NetGroupMember -GroupName 'Domain Admins' -Domain 'example.com'
```

## Expected Output

Member objects.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
