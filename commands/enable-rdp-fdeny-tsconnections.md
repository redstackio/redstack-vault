---
id: c136c221-68c1-4879-bc88-61f149c35d9d
name: enable-rdp-fdeny-tsconnections
type: command
executor: cmd
data: >-
  reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v
  fDenyTSConnections /t REG_DWORD /d 0 /f
output: null
created_at: '2023-04-06T03:56:31.036684+00:00'
updated_at: '2023-04-10T20:37:56.779209+00:00'
platforms:
  - Windows
tags:
  - rdp
  - registry
verified: true
validated: true
---

# enable-rdp-fdeny-tsconnections

## Command

```cmd
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

## Description

Enables the RDP service by modifying the Windows registry to deny TS connections set to 0. Run as administrator on the target machine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /v fDenyTSConnections | Registry value name | Yes |
| /t REG_DWORD | Data type | Yes |
| /d 0 | Value to enable RDP (0 = enabled) | Yes |
| /f | Force without prompt | Yes |

## Examples

### Basic Usage

```cmd
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

### Remote Usage

```cmd
psexec \\$_TARGET reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

## Expected Output

```
The operation completed successfully.
```

## Related

- [[procedures/windows-rdp-credential-usage]]
