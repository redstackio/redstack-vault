---
type: command
executor: cmd
data: >-
  reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server"
  /v fDenyTSConnections /t REG_DWORD /d 0 /f
output: null
platforms:
  - Windows
tags:
  - persistence
  - lateral-movement
verified: true
validated: true
---

# allow-remote-connections

## Command

```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

## Description

This command enables Remote Desktop connections by setting the registry to allow incoming Terminal Server connections. Essential for remote shadowing or RDP access in attack chains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server | Registry path for Terminal Server controls | Yes |
| /v fDenyTSConnections | Specifies the value name to modify | Yes |
| /t REG_DWORD | Sets the value type to DWORD | Yes |
| /d 0 | Sets the value to 0 (allow connections) | Yes |
| /f | Forces the operation without prompting | Yes |

## Examples

### Basic Usage

```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

### Verification

```cmd
reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections
```

## Expected Output

The operation completed successfully.

If queried, output shows:

fDenyTSConnections    REG_DWORD    0x0

## Related

- [[procedures/windows-remote-desktop-services-shadowing-persistence]]
- [[commands/configure-terminal-services-shadowing]]
