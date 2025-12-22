---
type: command
executor: cmd
data: reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - autologin
verified: true
validated: true
---

# reg-query-winlogon-for-autologin-settings

## Command

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

## Description

Dumps the Winlogon registry key to check for autologin configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Key path | Specific registry path | Yes |

## Examples

### Basic Usage

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

## Expected Output

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
    AutoAdminLogon    REG_SZ    1
    DefaultPassword    REG_SZ    *****
```

## Related

- [[procedures/windows-password-and-credential-query-via-registry]]
