---
id: f64d5b34-5a72-4544-bf53-bb0a19fedec8
name: db2-query-tables-by-column-name
type: command
executor: sql
data: select tbname from sysibm.syscolumns where name='username'
output: null
created_at: '2023-04-06T03:56:32.836523+00:00'
updated_at: '2023-04-10T20:22:04.830021+00:00'
platforms:
  - Databases
  - DB2
tags:
  - SQL-Injection
  - Database-Enumeration
verified: true
validated: true
---

# db2-query-tables-by-column-name

## Command

```sql
select tbname from sysibm.syscolumns where name='username'
```

## Description

This SQL command queries the DB2 system catalog to retrieve the names of all tables (tbname) that contain a column named 'username'. It is typically used in SQL injection attacks to enumerate database schema during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| name='username' | The column name to search for (case-sensitive; adapt as needed, e.g., 'password') | Yes |

## Examples

### Basic Usage

```sql
select tbname from sysibm.syscolumns where name='username'
```

### Advanced Usage

To search for multiple columns or add schema filter:

```sql
select tbname, colno from sysibm.syscolumns where name IN ('username', 'email')
```

## Expected Output

A list of table names containing the specified column, such as:

TBName
------
USERS
ADMIN_USERS

If no tables match, an empty result set is returned.

## Related

- [[procedures/DB2-SQL-Injection-to-Find-Tables-by-Column-Name]]
