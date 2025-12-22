---
id: 824e7b94-692c-44b5-a29e-0abf5b4f0852
name: reg-query-laps-enabled
type: command
executor: cmd
data: reg query "HKLM\Software\Policies\Microsoft Services\AdmPwd" /v AdmPwdEnabled
output: null
created_at: '2023-01-12T19:12:06.787503+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - registry
verified: true
validated: true
---

# reg-query-laps-enabled

## Command

```cmd
reg query "HKLM\Software\Policies\Microsoft Services\AdmPwd" /v AdmPwdEnabled
```

## Description

This command queries the Windows registry for the LAPS (Local Administrator Password Solution) policy enablement value. It checks if the AdmPwdEnabled DWORD is set to 1, indicating LAPS is active on the local machine. Use this during discovery to detect LAPS deployment without domain queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKLM\Software\Policies\Microsoft Services\AdmPwd | Registry key path for LAPS policy | Yes (built-in) |
| /v AdmPwdEnabled | Specifies the value name to query | Yes (built-in) |

## Examples

### Basic Usage

```cmd
reg query "HKLM\Software\Policies\Microsoft Services\AdmPwd" /v AdmPwdEnabled
```

### Advanced Usage

To export the result: 
```cmd
reg query "HKLM\Software\Policies\Microsoft Services\AdmPwd" /v AdmPwdEnabled > laps_reg.txt
```

## Expected Output

If LAPS is enabled:
```
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft Services\AdmPwd
    AdmPwdEnabled    REG_DWORD    0x1
```

If not found or disabled:
```
ERROR: The system was unable to find the specified registry key or value.
```

## Related

- [[procedures/Enumerate-LAPS-Artifacts-on-Local-Machine]]
