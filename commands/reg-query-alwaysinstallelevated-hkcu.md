---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: reg-query-alwaysinstallelevated-hkcu
type: command
executor: cmd
data: >-
  reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v
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

# reg-query-alwaysinstallelevated-hkcu

## Command

```cmd
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

## Description

Queries the AlwaysInstallElevated registry value in the current user's hive (HKCU) to check if it's enabled for privilege escalation via MSI installs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer | Registry path | Yes |
| /v AlwaysInstallElevated | Specifies the value name to query | Yes |

## Examples

### Basic Usage

```cmd
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

## Expected Output

```
HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1 (1)
```

If the value is 1, the setting is enabled; if 0 or missing, it's disabled.

## Related

- [[procedures/Windows-AlwaysInstallElevated-Privilege-Escalation]]
