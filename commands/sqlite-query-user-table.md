---
id: cmd-sqlite-user-query
data: sqlite3 ~/Downloads/grafana.db "select * from user;"
tags:
  - query
  - database
  - user-enum
type: command
output: 1|admin|admin@example.com|$2a$10$...|1|...
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.744Z'
verified: false
validated: true
submitted: true
---
# sqlite-query-user-table

## Command

```bash
sqlite3 ~/Downloads/grafana.db "select * from user;"
```

## Description

Queries the downloaded Grafana SQLite database to retrieve all records from the user table, exposing user details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Database file | Path to grafana.db | Yes |
| SQL query | SELECT statement for user table | Yes |

## Examples

### Basic Usage

```bash
sqlite3 grafana.db "select * from user;"
```

### Advanced Usage

Query specific columns:

```bash
sqlite3 grafana.db "select login, email from user;"
```

## Expected Output

Table rows with user data, e.g., id, login, email, password hash, and active status.

## Related

- [[Related Procedure: Download-and-Query-Grafana-SQLite-Database]]
