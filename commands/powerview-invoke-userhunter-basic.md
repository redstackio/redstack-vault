---
type: command
executor: powershell
data: Invoke-UserHunter
output: null
created_at: '2023-04-06T03:56:04Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - powerview
  - hunter
verified: true
validated: true
---

# powerview-invoke-userhunter-basic

## Command

```powershell
Invoke-UserHunter
```

## Description

Uses PowerView's Invoke-UserHunter to query LDAP for domain computers with active sessions from Domain Admins or specified users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Default: Hunts Domain Admin sessions | No |

## Examples

### Basic Usage

```powershell
Invoke-UserHunter
```

### Advanced Usage

```powershell
Invoke-UserHunter -UserName specificuser
```

## Expected Output

```
ComputerName : WORKSTATION01
UserName     : Administrator
SessionID    : 1
```
Lists computers and users with sessions.

## Related

- [[procedures/Active-Directory-User-Enumeration]]
- [[tools/PowerView]]
