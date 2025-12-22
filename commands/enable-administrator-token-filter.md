---
id: 359ae4a0-5f47-41a2-b084-ac3d8c50bd5a
name: enable-administrator-token-filter
type: command
executor: cmd
data: >-
  reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v
  FilterAdministratorToken /t REG_DWORD /f /d 1
output: null
created_at: '2023-04-06T03:56:30.837586+00:00'
updated_at: '2023-10-10T20:37:57.936960+00:00'
platforms:
  - Windows
tags:
  - registry
  - uac
verified: true
validated: true
---

# enable-administrator-token-filter

## Command

```cmd
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v FilterAdministratorToken /t REG_DWORD /f /d 1
```

## Description

This command sets the FilterAdministratorToken registry value to 1, enabling UAC token filtering for the built-in Administrator account. This restricts remote administrative actions unless fully elevated, often used defensively but checked offensively for bypass needs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System | Registry path for system policies | Yes |
| /v FilterAdministratorToken | Specifies the value name to set | Yes |
| /t REG_DWORD | Sets the value type to 32-bit DWORD | Yes |
| /f | Forces overwrite without prompt | Yes |
| /d 1 | Sets the value data to 1 (enable filtering) | Yes |

## Examples

### Basic Usage

```cmd
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v FilterAdministratorToken /t REG_DWORD /f /d 1
```

### Verification

```cmd
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v FilterAdministratorToken
```

## Expected Output

The operation completed successfully.

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
    FilterAdministratorToken    REG_DWORD    0x1

## Related

- [[procedures/Remote-Command-Execution-with-Impacket-Using-Credentials]]
- [[commands/impacket-wmiexec-execute-with-password]]
