---
id: 823b11b5-35b4-47b6-8512-81e4adf9f56f
name: postgresql-select-columns-from-information-schema
type: command
executor: sql
data: >-
  SELECT column_name FROM information_schema.columns WHERE
  table_name='data_table'
output: null
created_at: '2023-04-06T03:56:35.720094+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - sql-injection
  - postgresql
verified: true
validated: true
---

# postgresql-select-columns-from-information-schema

## Command

```sql
SELECT column_name FROM information_schema.columns WHERE table_name='data_table'
```

## Description

This SQL command queries the PostgreSQL information_schema view to retrieve the names of all columns in a specified table. It is typically used in SQL injection attacks to enumerate database schema details, helping attackers identify exploitable fields.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| table_name | The name of the target table to enumerate columns for (e.g., 'users') | Yes |

## Examples

### Basic Usage

```sql
SELECT column_name FROM information_schema.columns WHERE table_name='users'
```

### With Additional Filters (e.g., Schema)

```sql
SELECT column_name FROM information_schema.columns WHERE table_name='users' AND table_schema='public'
```

## Expected Output

A list of column names for the specified table, returned as rows in the result set. For example:

column_name
------------
id
username
email
password

If no columns are found or access is denied, an empty result set or error (e.g., permission denied) is returned.

## Related

- [[procedures/PostgreSQL-Column-Enumeration-via-SQL-Injection]]
