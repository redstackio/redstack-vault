---
id: 3f6c0851-fd6a-4602-8540-3f3632591306
name: reg-query-autologon-creds
type: command
executor: command_prompt
data: reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
output: |-
  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
      DefaultPassword    REG_SZ    Password123
created_at: '2020-03-17T23:49:26.705170+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - registry
  - credentials
verified: true
validated: true
---

# reg-query-autologon-creds

## Command

```command_prompt
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

## Description

Queries registry for auto-logon credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| reg query | Registry query command | Yes |
| Key path | Winlogon key | Yes |

## Examples

### Basic Usage

```command_prompt
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v DefaultPassword
```

## Expected Output

Registry values including passwords.

## Related

- [[procedures/List-Windows-Autologon-Credentials]]
