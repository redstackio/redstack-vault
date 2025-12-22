---
id: a7acbf3f-b379-42b4-8967-7ff9e7c1cbc9
name: db2-select-table-names-from-tables
type: command
executor: sql
data: select table_name from sysibm.tables
output: null
created_at: '2023-04-06T03:56:32.805744+00:00'
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

# db2-select-table-names-from-tables

## Command

```sql
select table_name from sysibm.tables
```

## Description

This SQL command queries the SYSIBM.TABLES system catalog view in IBM DB2 to retrieve the names of all tables in the current schema. It is commonly injected via SQL injection vulnerabilities to enumerate database structure during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| table_name | The column specifying the table name (no user input; system-defined) | No (outputs all) |
| sysibm.tables | The system view for table metadata | Yes |

## Examples

### Basic Usage

```sql
select table_name from sysibm.tables;
```

### Filtered Usage

```sql
select table_name from sysibm.tables where type = 'T';
```

## Expected Output

A list of table names, for example:

TABLE_NAME
----------
USERS
ORDERS
PRODUCTS

If no tables exist in the schema, an empty result set is returned.

## Related

- [[procedures/List-Tables-via-DB2-SQL-Injection]]
- [[commands/db2-select-table-names-from-systables]]
