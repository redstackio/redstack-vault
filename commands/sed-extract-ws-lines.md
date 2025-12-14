---
id: cmd-013
data: 'sed -n ''1260,1265p'' lib/ws.c'
tags:
  - extract
  - code-review
type: command
output: Code snippet around line 1261
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.041Z'
verified: false
validated: true
submitted: true
---
# sed-extract-ws-lines

## Command

```bash
sed -n '1260,1265p' lib/ws.c
```

## Description

Extracts lines 1260-1265 from ws.c for vulnerability review.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Suppress default | Yes |
| `'1260,1265p'` | Print range | Yes |

## Examples

### Basic Usage

```bash
sed -n '1260,1265p' lib/ws.c
```

## Expected Output

Code lines printed.

## Related

- [[procedures/Static-Analysis-of-Unsafe-strcpy-Calls-in-cURL]]
