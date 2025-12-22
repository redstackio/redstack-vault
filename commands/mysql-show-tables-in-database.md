---
id: 2f3c1b5d-934a-4926-bf20-b43313ea0854
name: MySQL Show Tables in Database
type: command
executor: sql
data: SHOW TABLES IN dvwa
output: null
created_at: '2023-04-06T03:56:36.832530+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - mysql
  - enumeration
verified: true
validated: true
---

# MySQL Show Tables in Database

## Command

```sql
SHOW TABLES IN dvwa;
```

## Description

This command lists all tables in a specified MySQL database, ideal for quick schema enumeration in SQLi WAF bypass techniques.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| dvwa | Database name (replace with target DB) | Yes |

## Examples

### Basic Usage

```sql
SHOW TABLES IN dvwa;
```

### In Injection Context

```sql
' UNION SELECT table_name FROM (SHOW TABLES IN dvwa) AS t--
```

## Expected Output

+----------------+
| Tables_in_dvwa |
+----------------+
| guestbook      |
| users          |
+----------------+

## Related

- [[procedures/SQL Injection WAF Bypass using MySQL Specific Commands]]
- [[MySQL Select InnoDB Table Stats]]
