---
id: 6904d1e3-e678-48dd-b4ba-a0a35c0d08da
name: bash-assign-empty-variable
type: command
executor: bash
data: google=""
output: null
created_at: '2023-04-06T03:56:37.506287+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - bash
  - variable
  - obfuscation
verified: true
validated: true
---

# bash-assign-empty-variable

## Command

```bash
google=""
```

## Description

This command assigns an empty string to a bash variable named 'google'. It is used to prepare for URL obfuscation in SSRF attacks by allowing embedded variables to expand without adding content, effectively hiding domain parts from string filters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `google` | Variable name (customizable, e.g., change to any name) | Yes |
| `""` | Empty string value | Yes |

## Examples

### Basic Usage

```bash
google=""
```

### Advanced Usage

```bash
filter_bypass=""
```

(Use a different variable name if 'google' conflicts.)

## Expected Output

No output is produced; the variable is silently set. Verify with `echo $google`, which should return an empty line.

## Related

- [[procedures/Bypass-SSRF-Filters-Using-Bash-Variables-and-Curl-Verbose]]
- [[commands/curl-verbose-with-variable-url]]
