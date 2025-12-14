---
id: cmd-015
data: 'sed -n ''1539,1544p'' lib/vtls/wolfssl.c'
tags:
  - extract
  - code-review
type: command
output: Code snippet around line 1540
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.033Z'
verified: false
validated: true
submitted: true
---
# sed-extract-wolfssl-lines

## Command

```bash
sed -n '1539,1544p' lib/vtls/wolfssl.c
```

## Description

Extracts lines 1539-1544 from wolfssl.c.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Suppress | Yes |
| `'1539,1544p'` | Range | Yes |

## Examples

### Basic Usage

```bash
sed -n '1539,1544p' lib/vtls/wolfssl.c
```

## Expected Output

Code lines.

## Related

- [[procedures/Static-Analysis-of-Unsafe-strcpy-Calls-in-cURL]]
