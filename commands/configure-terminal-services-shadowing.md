---
type: command
executor: cmd
data: >-
  reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal
  Services" /v Shadow /t REG_DWORD /d 4
output: null
platforms:
  - Windows
tags:
  - persistence
  - lateral-movement
verified: true
validated: true
---

# configure-terminal-services-shadowing

## Command

```cmd
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v Shadow /t REG_DWORD /d 4
```

## Description

This command configures the Windows registry to enable Remote Desktop Services shadowing without requiring user consent, allowing remote viewing of user sessions. Use this in persistence scenarios where elevated access is available.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services | Registry path for Terminal Services policies | Yes |
| /v Shadow | Specifies the value name to set | Yes |
| /t REG_DWORD | Sets the value type to DWORD | Yes |
| /d 4 | Sets the value to 4 (view without permission) | Yes |

## Examples

### Basic Usage

```cmd
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v Shadow /t REG_DWORD /d 4
```

### Verification

```cmd
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v Shadow
```

## Expected Output

The operation completed successfully.

If queried, output shows:

Shadow    REG_DWORD    0x4

## Related

- [[procedures/windows-remote-desktop-services-shadowing-persistence]]
- [[commands/allow-remote-connections]]
