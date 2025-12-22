---
type: command
executor: sql
data: >-
  SELECT column_name FROM
  `$_PROJECT_ID.$_DATASET_NAME.INFORMATION_SCHEMA.COLUMNS` WHERE table_name =
  '$_TABLE_NAME'
output: null
created_at: '2023-04-06T03:56:32.353180+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - GCP
tags:
  - sqli
  - schema-extraction
verified: true
validated: true
---

# bigquery-extract-column-names

## Command

```sql
SELECT column_name FROM `$_PROJECT_ID.$_DATASET_NAME.INFORMATION_SCHEMA.COLUMNS` WHERE table_name = '$_TABLE_NAME'
```

## Description

This SQL command queries BigQuery's INFORMATION_SCHEMA to list column names for a specific table, aiding in crafting union-based injections by revealing the schema structure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PROJECT_ID | Google Cloud project ID containing the dataset | Yes |
| $_DATASET_NAME | Name of the BigQuery dataset | Yes |
| $_TABLE_NAME | Name of the target table | Yes |

## Examples

### Basic Usage

```sql
SELECT column_name FROM `myproject.mydataset.INFORMATION_SCHEMA.COLUMNS` WHERE table_name = 'usertable'
```

### Advanced Usage

```sql
SELECT column_name, data_type FROM `myproject.mydataset.INFORMATION_SCHEMA.COLUMNS` WHERE table_name = 'usertable' ORDER BY ordinal_position
```

## Expected Output

A result set listing column names, e.g.:

| column_name |
|-------------|
| id          |
| username    |
| email       |

## Related

- [[procedures/BigQuery-Union-Based-SQL-Injection]]
