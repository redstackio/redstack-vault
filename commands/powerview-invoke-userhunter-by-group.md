---
type: command
executor: powershell
data: Invoke-UserHunter -GroupName $_GROUP_NAME
output: null
created_at: '2023-04-06T03:56:04Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - powerview
  - group
verified: true
validated: true
---

# powerview-invoke-userhunter-by-group

## Command

```powershell
Invoke-UserHunter -GroupName $_GROUP_NAME
```

## Description

Hunts for computers with sessions from members of a specified AD group, such as RDPUsers, via LDAP queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -GroupName $_GROUP_NAME | AD group name (e.g., RDPUsers) | Yes |

## Examples

### Basic Usage

```powershell
Invoke-UserHunter -GroupName "RDPUsers"
```

### Advanced Usage

```powershell
Invoke-UserHunter -GroupName "Server Operators" -Verbose
```

## Expected Output

```
ComputerName : SERVER01
GroupName    : RDPUsers
Users        : user1, user2
```
Shows group-related sessions per computer.

## Related

- [[procedures/Active-Directory-User-Enumeration]]
- [[tools/PowerView]]
