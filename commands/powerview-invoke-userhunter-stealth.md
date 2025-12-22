---
type: command
executor: powershell
data: Invoke-UserHunter -Stealth
output: null
created_at: '2023-04-06T03:56:04Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - powerview
  - stealth
verified: true
validated: true
---

# powerview-invoke-userhunter-stealth

## Command

```powershell
Invoke-UserHunter -Stealth
```

## Description

Performs a stealthy version of user hunting by minimizing network queries and avoiding noisy LDAP calls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Stealth | Enables low-profile querying mode | Yes |

## Examples

### Basic Usage

```powershell
Invoke-UserHunter -Stealth
```

### Advanced Usage

```powershell
Invoke-UserHunter -Stealth -GroupName "Domain Admins"
```

## Expected Output

```
ComputerName : STEALTHHOST
UserName     : Admin
Status       : Stealth Query Complete
```
Similar to basic but with reduced footprint.

## Related

- [[procedures/Active-Directory-User-Enumeration]]
- [[tools/PowerView]]
