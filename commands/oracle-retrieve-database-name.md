---
type: command
executor: sql
data: SELECT name FROM V$DATABASE;
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

# oracle-retrieve-database-name

## Command

```sql
SELECT name FROM V$DATABASE;
```

## Description

This SQL command retrieves the local database name (DB_NAME) from the V$DATABASE dynamic performance view, providing core identification of the Oracle database instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Parameterless query; requires SELECT on V$DATABASE. | N/A |

## Examples

### Basic Usage

```sql
SELECT name FROM V$DATABASE;
```

### Blind Injection Usage

Use boolean-based blind SQLi to infer the name character by character, e.g., via conditional queries.

## Expected Output

A single row with the database name, e.g.:

NAME
----
ORCL

## Related

- [[procedures/Oracle-SQL-Database-Name-Enumeration]]
- [[commands/oracle-retrieve-global-database-name]]
