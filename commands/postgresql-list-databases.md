---
id: 755975e1-082b-42b7-8bd1-b72474f9bf46
name: postgresql-list-databases
type: command
executor: sql
data: SELECT datname FROM pg_database;
output: null
created_at: '2023-04-06T03:56:35.661283+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Database
tags:
  - postgresql
  - enumeration
verified: true
validated: true
---

# postgresql-list-databases

## Command

```sql
SELECT datname FROM pg_database;
```

## Description

This SQL command queries the PostgreSQL system catalog to retrieve a list of all database names on the server. It is used during reconnaissance to identify available databases for further exploration, typically executed in a psql session or via SQL injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| datname | The column name for database names (fixed in query) | No (built-in) |
| pg_database | The system table containing database metadata (fixed) | No (built-in) |

No user-supplied parameters; the query is static but can be adapted (e.g., add WHERE clauses for filtering).

## Examples

### Basic Usage

In psql:
```sql
postgres=# SELECT datname FROM pg_database;
```

### Filtered Usage (Advanced)

To exclude system databases:
```sql
SELECT datname FROM pg_database WHERE datistemplate = false AND datname != 'postgres';
```

## Expected Output

A tabular list of database names:
```
  datname  
-----------
 postgres
 template1
 template0
 myapp_db
(4 rows)
```

Look for non-system entries like 'myapp_db' as indicators of user data.

## Related

- [[procedures/PostgreSQL-Database-Enumeration]]
- [[techniques/System-Information-Discovery|T1082]]
