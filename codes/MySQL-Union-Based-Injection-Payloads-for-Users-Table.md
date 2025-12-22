---
id: 907f03be-5797-45ac-bf38-99ef9758d1cb
name: MySQL-Union-Based-Injection-Payloads-for-Users-Table
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.329226+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - sql-injection
  - union-based
  - mysql
  - payload
validated: true
---

# MySQL-Union-Based-Injection-Payloads-for-Users-Table

## Code

```sql
1' AND (SELECT * FROM Users) = 1--+  #Operand should contain 3 column(s)
# This error means query uses 3 column
#-1' UNION SELECT 1,2,3--+    True
```

## Description

This SQL code snippet contains payloads for MySQL union-based injection targeting a Users table. The first payload uses an error-based subquery to enumerate the number of columns by causing a mismatch error. The second is a basic UNION SELECT to confirm the column count and begin data extraction, returning placeholder values (1,2,3) that can be replaced with actual column names like username or password.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Users | Name of the target table containing user data | Users |
| 1,2,3 | Placeholder values matching column count; replace with NULL or column names for extraction | 1,username,password |

## Usage

Inject these payloads into a vulnerable web parameter (e.g., via GET/POST in a form or URL). Use the error-based payload first to determine column count from the MySQL error message, then adapt the UNION SELECT with the correct number of columns to pull data from Users. Commonly used in procedures like [[procedures/MySQL-Union-Based-Injection-to-Extract-Users-Table-Data]] during web penetration testing to exfiltrate credentials.

## Detection

- Database logs showing subqueries or UNION statements from untrusted inputs.
- Application errors revealing column counts or table names (e.g., "Operand should contain X column(s)").
- WAF alerts for keywords like UNION, SELECT, or table names in requests.
- Anomalous response times or content lengths indicating successful injections.

## Related

- [[procedures/MySQL-Union-Based-Injection-to-Extract-Users-Table-Data]]
