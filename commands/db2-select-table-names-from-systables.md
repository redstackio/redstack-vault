---
id: caed4488-25eb-418a-93a6-20d2f19f749f
name: db2-select-table-names-from-systables
type: command
executor: sql
data: select name from sysibm.systables
output: null
created_at: '2023-04-06T03:56:32.805835+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Database
  - DB2
tags:
  - SQL-Injection
  - Database-Enumeration
verified: true
validated: true
---

# db2-select-table-names-from-systables

## Command

```sql
select name from sysibm.systables
```

## Description

This SQL command queries the SYSIBM.SYSTABLES system catalog view in IBM DB2 to retrieve the names of all tables in the entire database. It provides broader enumeration compared to schema-specific views and is useful for comprehensive discovery via injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| name | The column specifying the table name (no user input; system-defined) | No (outputs all) |
| sysibm.systables | The system view for database-wide table metadata | Yes |

## Examples

### Basic Usage

```sql
select name from sysibm.systables;
```

### Filtered Usage

```sql
select name from sysibm.systables where type = 'T';
```

## Expected Output

A comprehensive list of table names, for example:

NAME
----
SYSIBM.SYSTABLES
USERS
ORDERS
ADMIN_CONFIG

Filter out system tables for attacker-relevant data.

## Related

- [[procedures/List-Tables-via-DB2-SQL-Injection]]
- [[commands/db2-select-table-names-from-tables]]
