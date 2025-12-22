---
id: 1bb0caaa-9811-424f-a2a8-00cffdd11e1a
name: mssql-select-current-user
type: command
executor: sqlcmd
data: SELECT USER_NAME();
output: null
created_at: '2023-04-06T03:56:35.447997+00:00'
updated_at: '2023-04-10T20:23:19.545936+00:00'
platforms:
  - Windows
tags:
  - mssql
  - discovery
verified: true
validated: true
---

# mssql-select-current-user

## Command

```sqlcmd
sqlcmd -S $_SERVER -U $_USERNAME -P $_PASSWORD -Q "SELECT USER_NAME();"
```

## Description

This command queries the current user's name in the MSSQL database session, useful for confirming access and user context during discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVER | MSSQL server hostname or IP (e.g., localhost or 192.168.1.100) | Yes |
| $_USERNAME | SQL login username | Yes |
| $_PASSWORD | SQL login password | Yes |
| -S | Specifies the server to connect to | Built-in |
| -U | Specifies the username | Built-in |
| -P | Specifies the password | Built-in |
| -Q | Executes the query and exits | Built-in |

## Examples

### Basic Usage

```sqlcmd
sqlcmd -S localhost -U sa -P P@ssw0rd -Q "SELECT USER_NAME();"
```

### Advanced Usage

Connect to a remote instance with trusted authentication:

```sqlcmd
sqlcmd -S remote-server -E -Q "SELECT USER_NAME();"
```

## Expected Output

```
--------
sa

(1 rows affected)
```

The output shows the current username (e.g., 'sa' for system administrator). If no rows or an error occurs, check credentials or permissions.

## Related

- [[procedures/Enumerate-Current-User-Role-in-MSSQL]]
