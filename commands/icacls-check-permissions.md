---
id: 6806dced-703c-47fa-a0be-8f36f3b22c2b
name: icacls-check-permissions
type: command
executor: cmd
data: icacls $_PATH
output: null
created_at: '2023-04-06T03:56:29.437216+00:00'
updated_at: '2023-04-10T20:37:36.999118+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - permissions
verified: true
validated: true
---

# icacls-check-permissions

## Command

```cmd
icacls $_PATH
```

## Description

Displays or modifies Access Control Lists (ACLs) for files and folders on Windows, useful for auditing service binary permissions during privilege escalation reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PATH | Target file or directory path (e.g., C:\\Program Files\\Service) | Yes |

## Examples

### Basic Usage

```cmd
icacls "C:\Program Files\VulnerableService"
```

### Recursive Check

```cmd
icacls "C:\Program Files\VulnerableService" /T
```

## Expected Output

C:\Program Files\VulnerableService NT AUTHORITY\SYSTEM:(I)(OI)(F)
BUILTIN\Administrators:(I)(OI)(F)
BUILTIN\Users:(I)(OI)(RX)

Indicates weak perms if Users has (F) or (M).

## Related

- [[procedures/Windows-Local-Service-Permissions-Escalation]]
