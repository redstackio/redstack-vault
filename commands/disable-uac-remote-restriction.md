---
type: command
executor: cmd
data: >-
  reg add
  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
  /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
output: null
platforms:
  - Windows
tags:
  - privilege-escalation
  - lateral-movement
verified: true
validated: true
---

# disable-uac-remote-restriction

## Command

```cmd
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
```

## Description

This command disables UAC remote token filtering, allowing local administrator accounts to perform remote actions with full privileges without UAC prompts. Useful for remote administration or attacks over RDP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System | Registry path for system policies | Yes |
| /v LocalAccountTokenFilterPolicy | Specifies the value name | Yes |
| /t REG_DWORD | Sets the value type to DWORD | Yes |
| /d 1 | Sets the value to 1 (disable filtering) | Yes |
| /f | Forces the operation without prompting | Yes |

## Examples

### Basic Usage

```cmd
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
```

### Verification

```cmd
reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy
```

## Expected Output

The operation completed successfully.

If queried, output shows:

LocalAccountTokenFilterPolicy    REG_DWORD    0x1

## Related

- [[procedures/windows-remote-desktop-services-shadowing-persistence]]
- [[commands/allow-remote-connections]]
