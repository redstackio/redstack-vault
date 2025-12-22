---
type: command
executor: sql
data: LIMIT $_LIMIT_COUNT
output: null
created_at: '2023-04-06T03:56:32.353435+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - GCP
tags:
  - sqli
  - pagination
verified: true
validated: true
---

# bigquery-limit-results

## Command

```sql
LIMIT $_LIMIT_COUNT
```

## Description

This SQL clause restricts the number of rows returned by a query, essential for testing injections without overwhelming the application or triggering rate limits in BigQuery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LIMIT_COUNT | Maximum number of rows to return (e.g., 1, 10) | Yes |

## Examples

### Basic Usage

```sql
SELECT * FROM table LIMIT 1
```

### Advanced Usage

```sql
SELECT * FROM table ORDER BY id DESC LIMIT 5
```

## Expected Output

Limited result set, e.g., first row only:

| id | name |
|----|------|
| 1  | John |

## Related

- [[procedures/BigQuery-Union-Based-SQL-Injection]]
