---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: reg-add-alwaysinstallelevated-hkcu
type: command
executor: cmd
data: >-
  reg add HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v
  AlwaysInstallElevated /t REG_DWORD /d 1 /f
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

# reg-add-alwaysinstallelevated-hkcu

## Command

```cmd
reg add HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated /t REG_DWORD /d 1 /f
```

## Description

Adds or sets the AlwaysInstallElevated value to 1 in the HKCU hive, enabling non-admin users to install MSI packages with elevated privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer | Registry path | Yes |
| /v AlwaysInstallElevated | Value name | Yes |
| /t REG_DWORD | Data type | Yes |
| /d 1 | Data value (1 to enable) | Yes |
| /f | Force without prompt | Yes |

## Examples

### Basic Usage

```cmd
reg add HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated /t REG_DWORD /d 1 /f
```

## Expected Output

```
The operation completed successfully.
```

Confirms the key is set; re-query to verify.

## Related

- [[procedures/Windows-AlwaysInstallElevated-Privilege-Escalation]]
