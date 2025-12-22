---
id: c6de6cc6-9f68-4e6c-a0df-2c8c787eafc3
name: mssql-query-user-roles
type: command
executor: sqlcmd
data: 'SELECT * FROM sys.fn_my_permissions(NULL, ''DATABASE'');'
output: null
created_at: '2023-04-06T03:56:20.739226+00:00'
updated_at: '2023-04-10T20:36:37.829759+00:00'
platforms:
  - Windows
tags:
  - mssql
  - discovery
  - roles
verified: true
validated: true
---

# mssql-query-user-roles

## Command

```sqlcmd
sqlcmd -S $_SERVER -U $_USERNAME -P $_PASSWORD -d $_DATABASE -Q "SELECT * FROM sys.fn_my_permissions(NULL, 'DATABASE');"
```

## Description

This command retrieves the current user's permissions at the database level in MSSQL, helping to enumerate roles and access rights for privilege assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVER | MSSQL server hostname or IP | Yes |
| $_USERNAME | SQL login username | Yes |
| $_PASSWORD | SQL login password | Yes |
| $_DATABASE | Target database name (e.g., master) | Yes |
| -S | Server connection flag | Built-in |
| -U | Username flag | Built-in |
| -P | Password flag | Built-in |
| -d | Database flag | Built-in |
| -Q | Query execution flag | Built-in |

## Examples

### Basic Usage

```sqlcmd
sqlcmd -S localhost -U sa -P P@ssw0rd -d master -Q "SELECT * FROM sys.fn_my_permissions(NULL, 'DATABASE');"
```

### Advanced Usage

Query with output to file for analysis:

```sqlcmd
sqlcmd -S remote-server -U user -P pass -d dbname -Q "SELECT * FROM sys.fn_my_permissions(NULL, 'DATABASE');" -o roles.txt
```

## Expected Output

```
entity_name permission_name  permission_state
NULL         CREATE TABLE    GRANT
NULL         SELECT          GRANT
NULL         INSERT          GRANT

(3 rows affected)
```

The output lists permissions like 'CREATE TABLE' or 'CONTROL' with their state. Empty results indicate limited access (e.g., public role only).

## Related

- [[procedures/Enumerate-Current-User-Role-in-MSSQL]]
