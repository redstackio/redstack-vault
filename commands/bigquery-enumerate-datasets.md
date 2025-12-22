---
type: command
executor: sql
data: SELECT dataset_id FROM `$_PROJECT_ID.INFORMATION_SCHEMA.SCHEMATA`;
output: null
platforms:
  - GCP
tags:
  - discovery
  - bigquery
verified: true
validated: true
---

# bigquery-enumerate-datasets

## Command

```sql
SELECT dataset_id FROM `$_PROJECT_ID.INFORMATION_SCHEMA.SCHEMATA`;
```

## Description

This SQL command lists all dataset IDs in the specified BigQuery project by querying the INFORMATION_SCHEMA. Essential for mapping data structures in an SQLi attack to identify targets for further exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PROJECT_ID | The Google Cloud project ID (e.g., 'my-project-123') | Yes |

## Examples

### Basic Usage

```sql
SELECT dataset_id FROM `my-project-123.INFORMATION_SCHEMA.SCHEMATA`;
```

### With Region Specification (if needed)

```sql
SELECT dataset_id FROM `region-us.my-project-123.INFORMATION_SCHEMA.SCHEMATA`;
```

## Expected Output

```
+------------+
| dataset_id |
+------------+
| analytics  |
| customers  |
| logs       |
+------------+
```

A list of dataset names in the project.

## Related

- [[procedures/SQL-Injection-in-Google-BigQuery-for-Data-Exfiltration]]
