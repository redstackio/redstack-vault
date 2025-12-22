---
type: command
executor: cmd
data: reg query HKCU /f password /t REG_SZ /s
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - registry
verified: true
validated: true
---

# reg-query-hkcu-for-password-variant

## Command

```cmd
reg query HKCU /f password /t REG_SZ /s
```

## Description

Variant search for HKCU passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /f password | Filter | Yes |
| /t REG_SZ | Type | Yes |
| /s | Recursion | Yes |

## Examples

### Basic Usage

```cmd
reg query HKCU /f password /t REG_SZ /s
```

## Expected Output

Similar to primary variant.

## Related

- [[procedures/windows-password-and-credential-query-via-registry]]
