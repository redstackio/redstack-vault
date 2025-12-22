---
id: cmd-014
data: 'sed -n ''1065,1070p'' lib/vtls/vtls.c'
tags:
  - extract
  - code-review
type: command
output: Code snippet around line 1066
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.037Z'
verified: false
validated: true
submitted: true
---
# sed-extract-vtls-lines

## Command

```bash
sed -n '1065,1070p' lib/vtls/vtls.c
```

## Description

Extracts lines 1065-1070 from vtls.c.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Suppress default | Yes |
| `'1065,1070p'` | Range | Yes |

## Examples

### Basic Usage

```bash
sed -n '1065,1070p' lib/vtls/vtls.c
```

## Expected Output

Code snippet.

## Related

- [[procedures/Static-Analysis-of-Unsafe-strcpy-Calls-in-cURL]]
