---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567896
data: nginx -V 2>&1 | grep debug
tags:
  - version-check
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:32.684Z'
verified: false
validated: true
submitted: true
---
# nginx-version-check

## Command

```bash
nginx -V 2>&1 | grep debug
```

## Description

Checks the nginx build configuration for debug options to determine if it's vulnerable to exploits like CVE-2014-0133, which requires absence of --with-debug.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-V` | Verbose build info | Yes |
| `2>&1` | Redirect stderr to stdout | Yes |
| `grep debug` | Filter for debug flags | Yes |

## Examples

### Basic Usage

```bash
nginx -V 2>&1 | grep debug
```

### Advanced Usage

```bash
nginx -V 2>&1 | grep -E "debug|spdy"
```

## Expected Output

No output if --with-debug is absent, confirming potential vulnerability; otherwise, lists debug-related compile options.

## Related

- [[Related Procedure: Verify-SPDY-Module-Configuration-for-CVE-2014-0133]]
