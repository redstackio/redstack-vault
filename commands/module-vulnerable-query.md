---
data: connection.query("SELECT * FROM "+ table +" WHERE "+name_id+"='"+ id+"'")
tags:
  - sqli
  - vulnerable
type: command
output: Query results based on input; vulnerable to injection
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.051Z'
id: 0cb95b47-352c-4047-9556-55f170cf86fa
verified: false
validated: true
submitted: true
---
# module-vulnerable-query

## Command

```javascript
connection.query("SELECT * FROM "+ table +" WHERE "+name_id+"='"+ id+"'")
```

## Description

Core vulnerable query construction in query-mysql's fetchById, using concatenation of user inputs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| table | User-provided table | Yes |
| name_id | Column name | Yes |
| id | User input (injectable) | Yes |

## Examples

### With Injection

```javascript
connection.query("SELECT * FROM users WHERE username='noob' or 1=1-- ");
```

## Expected Output

Executes altered query, returns all rows.

## Related

- [[Related Procedure|procedures/Exploit-SQL-Injection-with-Malicious-Input]]
