---
id: 1e6a9d87-a49d-4c03-8378-64111da326a0
name: MySQL Select InnoDB Version
type: command
executor: sql
data: SELECT @@innodb_version
output: null
created_at: '2023-04-06T03:56:36.832649+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - mysql
  - discovery
verified: true
validated: true
---

# MySQL Select InnoDB Version

## Command

```sql
SELECT @@innodb_version;
```

## Description

This command retrieves the version of the InnoDB storage engine in a MySQL database, useful for compatibility checks or identifying the MySQL variant during reconnaissance in SQLi attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @@innodb_version | System variable for InnoDB version | Yes |

## Examples

### Basic Usage

```sql
SELECT @@innodb_version;
```

### In Injection Context

```sql
' UNION SELECT @@innodb_version--
```

## Expected Output

+------------------+
| @@innodb_version |
+------------------+
| 5.6.31           |
+------------------+

## Related

- [[procedures/SQL Injection WAF Bypass using MySQL Specific Commands]]
- [[MySQL Select MySQL Version]]
