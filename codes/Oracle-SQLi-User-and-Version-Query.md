---
type: code
language: sql
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Oracle Database
tags:
  - sqli
  - payload
  - oracle
  - discovery
validated: true
---

# Oracle-SQLi-User-and-Version-Query

## Code

```sql
SELECT user FROM dual UNION SELECT * FROM v$version
```

## Description

This SQL payload is designed for UNION-based SQL injection in Oracle databases. It retrieves the current database user from the 'dual' table and all columns from the 'v$version' system view, which contains detailed version information including the Oracle release, edition, and components. When injected into a vulnerable query, it appends this data to the legitimate results, allowing enumeration without direct query access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload; adjust column count with NULLs if needed for matching original query (e.g., SELECT NULL, user FROM dual) | N/A |

## Usage

Inject this payload into a vulnerable parameter after closing the original query with a quote and comment (e.g., ' UNION [payload]--). Use in tools like sqlmap (--technique=U) or manual requests via curl/Burp. Ideal for initial reconnaissance to identify the database user context and version for CVE lookup. Ensure the original query returns the same number of columns; test with ORDER BY to determine count.

## Detection

- Database logs showing UNION queries or access to v$version by non-admin users.
- WAF alerts for keywords like 'UNION', 'v$version', or 'dual' in input.
- Application error logs with ORA-01789 (column mismatch) during testing.
- Network traffic analysis for anomalous SQL patterns in HTTP parameters.

## Related

- [[procedures/Oracle-SQL-Injection-User-and-Version-Retrieval]]
- [[tools/sqlmap]]
