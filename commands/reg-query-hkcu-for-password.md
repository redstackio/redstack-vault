---
type: command
executor: cmd
data: REG QUERY HKCU /F "password" /t REG_SZ /S /K
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

# reg-query-hkcu-for-password

## Command

```cmd
REG QUERY HKCU /F "password" /t REG_SZ /S /K
```

## Description

Identical to the primary HKCU search; used for redundancy in comprehensive scans.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /F "password" | Filter string | Yes |
| /t REG_SZ | Value type | Yes |
| /S | Subkey recursion | Yes |
| /K | Key matching | Yes |

## Examples

### Basic Usage

```cmd
REG QUERY HKCU /F "password" /t REG_SZ /S /K
```

## Expected Output

Similar to primary HKCU query.

## Related

- [[procedures/windows-password-and-credential-query-via-registry]]
