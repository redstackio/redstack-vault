---
id: 6588446e-9684-4735-8656-02cdece3e571
name: check-lsass-ppl-status
type: command
executor: powershell
data: reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa /v RunAsPPL
output: null
created_at: '2023-04-06T03:56:26.592325+00:00'
updated_at: '2023-04-10T20:37:03.734493+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - registry
verified: true
validated: true
---

# check-lsass-ppl-status

## Command

```powershell
reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa /v RunAsPPL
```

## Description

This command queries the Windows registry to determine if the LSASS process is running under Protected Process Light (PPL) protection. Use it during defense evasion reconnaissance to assess if additional bypass steps are needed for credential access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa | Registry path for LSA configuration | Yes (built-in) |
| /v RunAsPPL | Specifies the value name to query | Yes (built-in) |

## Examples

### Basic Usage

```powershell
reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa /v RunAsPPL
```

### With Output Redirection

```powershell
reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa /v RunAsPPL > ppl_status.txt
```

## Expected Output

Successful query on a PPL-enabled system:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa
    RunAsPPL    REG_DWORD    0x1
```

If disabled or absent:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa
    RunAsPPL    REG_DWORD    0x0
```

Error if key inaccessible: 'ERROR: Access is denied.'

## Related

- [[procedures/Terminate-Microsoft-Defender-to-Bypass-PPL]]
