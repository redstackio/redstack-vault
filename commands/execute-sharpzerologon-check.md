---
id: 144421f0-d231-4ebb-ab25-4898ede2051e
name: execute-sharpzerologon-check
type: command
executor: bash
data: execute-assembly SharpZeroLogon.exe $_DC_FQDN
output: null
created_at: '2023-04-06T03:56:02.673382+00:00'
updated_at: '2023-04-10T20:36:01.289773+00:00'
platforms:
  - Windows
tags:
  - sharpzerologon
  - check
verified: true
validated: true
---

# execute-sharpzerologon-check

## Command

```bash
execute-assembly SharpZeroLogon.exe $_DC_FQDN
```

## Description

Executes the SharpZeroLogon assembly to check for ZeroLogon vulnerability from a compromised Windows host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DC_FQDN | Fully qualified domain name of DC | Yes |

## Examples

### Basic Usage

```bash
execute-assembly SharpZeroLogon.exe win-dc01.vulncorp.local
```

## Expected Output

```
[+] Target is vulnerable to ZeroLogon.
```

## Related

- [[procedures/ZeroLogon-Exploitation-and-Post-Exploitation]]
- [[tools/SharpZeroLogon]]
