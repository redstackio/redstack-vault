---
id: cmd-012
data: grep -n "strcpy(" lib/ws.c lib/vtls/vtls.c lib/vtls/wolfssl.c
tags:
  - search
  - static-analysis
type: command
output: 'lib/ws.c:1261: strcpy(keyval, randstr); etc.'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.045Z'
verified: false
validated: true
submitted: true
---
# grep-search-strcpy

## Command

```bash
grep -n "strcpy(" lib/ws.c lib/vtls/vtls.c lib/vtls/wolfssl.c
```

## Description

Searches for strcpy calls in cURL files with line numbers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Line numbers | Yes |
| `strcpy(` | Pattern | Yes |
| `lib/ws.c ...` | Files | Yes |

## Examples

### Basic Usage

```bash
grep -n "strcpy(" lib/*.c
```

## Expected Output

File:line: matching line.

## Related

- [[procedures/Static-Analysis-of-Unsafe-strcpy-Calls-in-cURL]]
