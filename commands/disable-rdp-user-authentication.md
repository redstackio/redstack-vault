---
id: 43a61bee-3a68-48bf-ba69-4cbf33b839ff
name: disable-rdp-user-authentication
type: command
executor: cmd
data: >-
  reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal
  Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f
output: null
created_at: '2023-04-06T03:56:31.036745+00:00'
updated_at: '2023-04-10T20:37:56.779209+00:00'
platforms:
  - Windows
tags:
  - rdp
  - registry
  - nla
verified: true
validated: true
---

# disable-rdp-user-authentication

## Command

```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f
```

## Description

Disables user authentication (NLA) for the RDP-Tcp session to prevent CredSSP errors during connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /v UserAuthentication | Registry value for NLA | Yes |
| /t REG_DWORD | Data type | Yes |
| /d 0 | Value to disable (0 = disabled) | Yes |
| /f | Force without prompt | Yes |

## Examples

### Basic Usage

```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f
```

## Expected Output

```
The operation completed successfully.
```

## Related

- [[procedures/windows-rdp-credential-usage]]
