---
type: command
executor: sql
data: GROUP BY $_COLUMN_NAME
output: null
created_at: '2023-04-06T03:56:32.353564+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - GCP
tags:
  - sqli
  - aggregation
verified: true
validated: true
---

# bigquery-group-by-column

## Command

```sql
GROUP BY $_COLUMN_NAME
```

## Description

This SQL clause groups query results by the specified column, useful in union injections to avoid errors from duplicate rows or to shape output in BigQuery queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COLUMN_NAME | Name of the column to group by | Yes |

## Examples

### Basic Usage

```sql
SELECT COUNT(*) FROM table GROUP BY username
```

### Advanced Usage

```sql
SELECT username, COUNT(*) FROM table GROUP BY username HAVING COUNT(*) > 1
```

## Expected Output

Aggregated rows grouped by the column, e.g.:

| username | count |
|----------|-------|
| user1    | 5     |

## Related

- [[procedures/BigQuery-Union-Based-SQL-Injection]]
