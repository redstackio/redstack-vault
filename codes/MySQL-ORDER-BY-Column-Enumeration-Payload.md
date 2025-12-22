---
id: 32084d86-0e3c-45cf-99c9-b8a77af3cf26
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.233670+00:00'
updated_at: '2023-04-10T20:22:49.057957+00:00'
tags:
  - mysql-injection
  - column-enumeration
  - order-by
platforms:
  - Web
  - MySQL
validated: true
---

# MySQL-ORDER-BY-Column-Enumeration-Payload

## Code

```sql
1' ORDER BY 1--+    #True
1' ORDER BY 2--+    #True
1' ORDER BY 3--+    #True
1' ORDER BY 4--+    #False - Query is only using 3 columns
                    #-1' UNION SELECT 1,2,3--+    True
```

## Description

This SQL payload uses the ORDER BY clause to probe the number of columns in a vulnerable MySQL query during a SQL injection attack. By incrementing the column number (e.g., 1, 2, 3), it sorts results until an error reveals the actual column count. The trailing UNION SELECT confirms the count for further exploitation, such as injecting custom values.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N (in ORDER BY N) | Column position to test (increment sequentially) | 1, 2, 3, 4 |

## Usage

Inject this into a vulnerable parameter in a web application (e.g., via browser URL or POST data). Start with low N and increase until an SQL error occurs. Once the column count is known (e.g., 3), use the UNION SELECT variant to test data injection, replacing numbers with NULL or strings to infer types. This is a key step in blind SQLi reconnaissance.

## Detection

- WAF rules triggering on ORDER BY with numeric arguments or comment sequences like --+.
- Database logs showing queries with dynamic ORDER BY clauses or UNION statements.
- Application response anomalies, such as error pages or delayed responses during probing.

## Related

- [[procedures/MySQL-Union-Based-Column-Enumeration]]
