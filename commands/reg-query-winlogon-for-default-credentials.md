---
type: command
executor: cmd
data: >-
  reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" 2>nul |
  findstr "DefaultUserName DefaultDomainName DefaultPassword"
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

# reg-query-winlogon-for-default-credentials

## Command

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" 2>nul | findstr "DefaultUserName DefaultDomainName DefaultPassword"
```

## Description

Filters Winlogon for default credential values.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 2>nul | Suppress errors | No |
| findstr | Filter strings | Yes |

## Examples

### Basic Usage

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" 2>nul | findstr "DefaultUserName DefaultDomainName DefaultPassword"
```

## Expected Output

```
    DefaultUserName    REG_SZ    admin
    DefaultPassword    REG_SZ    pass
```

## Related

- [[procedures/windows-password-and-credential-query-via-registry]]
