---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: reg-query-alwaysinstallelevated-hklm
type: command
executor: cmd
data: >-
  reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v
  AlwaysInstallElevated
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - registry
  - privesc
verified: true
validated: true
---

# reg-query-alwaysinstallelevated-hklm

## Command

```cmd
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

## Description

Queries the machine-wide AlwaysInstallElevated registry value in HKLM to determine if elevated MSI installs are permitted system-wide.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer | Registry path | Yes |
| /v AlwaysInstallElevated | Specifies the value name to query | Yes |

## Examples

### Basic Usage

```cmd
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

## Expected Output

```
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1 (1)
```

A value of 1 indicates vulnerability; requires admin to change if 0.

## Related

- [[procedures/Windows-AlwaysInstallElevated-Privilege-Escalation]]
