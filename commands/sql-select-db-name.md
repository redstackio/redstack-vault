---
type: command
executor: sql
data: select db_name()
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - SQL Server
tags:
  - database-discovery
  - mssql
verified: true
validated: true
---

# sql-select-db-name

## Command

```sql
select db_name()
```

## Description

This SQL command uses the built-in DB_NAME() function to return the name of the database currently active in the session. It is a quick way to confirm the database context during database reconnaissance or troubleshooting access issues in SQL Server environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | The function requires no parameters; it operates on the current session context. | No |

## Examples

### Basic Usage

```sql
select db_name()
```

Execute this in any SQL query interface connected to the target instance.

### Advanced Usage

Combine with conditional logic for scripted enumeration:

```sql
if db_name() = 'master' print 'Default database detected'; else print 'Custom database: ' + db_name();
```

## Expected Output

A single-row result set with one column named 'db_name' (or unlabeled), containing the database name string. Example:

```
db_name
--------
MyAppDB
```

If no database is active or access is denied, it may return NULL or an error like 'Cannot open database "default" requested by the login.'

## Related

- [[procedures/Retrieve-Current-Database-Name-in-SQL-Server]]
