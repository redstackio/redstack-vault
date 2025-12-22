---
type: command
executor: command_prompt
data: reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
output: |-
  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
      AutoAdminLogon    REG_SZ    1
      DefaultPassword    REG_SZ    Password123
      DefaultUserName    REG_SZ    testuser
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - registry
  - credentials
verified: true
validated: true
---

# Reg-Query-Autologon-Registry-Keys

## Command

```command_prompt
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

## Description

Queries the Winlogon registry key for auto-logon credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| reg query | Registry query command | Yes |
| "HKLM\..." | Key path | Yes |

## Examples

### Basic Usage

```command_prompt
reg query HKLM\SOFTWARE\...
```

### Advanced Usage

```command_prompt
reg query "HKLM\..." /v DefaultPassword
```

Specific value.

## Expected Output

Registry values including passwords.

## Related

- [[procedures/List-Windows-Autologon-Credentials-from-Registry]]
