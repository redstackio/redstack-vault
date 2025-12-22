---
id: a78909fa-25ca-455a-84d1-8a4340f8e6c2
name: PostgreSQL-PG-Sleep-Database-Name-Test
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.853734+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - PostgreSQL
tags:
  - sql-injection
  - blind-injection
  - time-based
  - pg_sleep
validated: true
---

# PostgreSQL-PG-Sleep-Database-Name-Test

## Code

```sql
select case when substring(datname,1,1)='1' then pg_sleep(5) else pg_sleep(0) end from pg_database limit 1
```

## Description

This SQL code snippet performs a time-based blind injection test on PostgreSQL by conditionally delaying the query response using pg_sleep. It checks if the first character of the first database name (from pg_database) is '1'; if true, it sleeps for 5 seconds, otherwise 0 seconds. This allows attackers to infer database metadata through timing without producing visible output, forming the basis for extracting full names or other data via repeated tests on characters and positions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| datname | Database name column from pg_database | postgres |
| 1,1 | Position and length for substring (start at 1, length 1) | 1,1 |
| '1' | Test character (replace with 'a'-'z', digits, etc.) | 'p' |
| 5 | Sleep duration for true condition (in seconds) | 5 |
| 0 | Sleep duration for false condition | 0 |
| limit 1 | Restrict to first row | 1 |

## Usage

Embed this code into an injectable parameter of a web application (e.g., via URL or POST data) connected to PostgreSQL. Use tools like curl to send the request and measure response time. For extraction, iterate over possible characters (a-z, 0-9) for each position in the string. Example: To test if database name starts with 'p', replace '1' with 'p'. A 5-second delay confirms the condition. Chain with system tables like pg_tables for broader dumps. Deliver via vulnerable apps like login forms or search endpoints.

## Detection

- Monitor PostgreSQL logs for pg_sleep calls or queries exceeding normal execution time (e.g., >2s).
- WAF rules to block SQL keywords like 'pg_sleep', 'substring', 'case when' in inputs.
- Application-level timing anomalies: Alert on requests with response times >3s from the same IP.
- Database auditing: Track access to system catalogs like pg_database.

## Related

- [[procedures/PostgreSQL-Time-Based-Blind-Injection-for-Database-Dump]]
- [[commands/curl-postgresql-sqli-payload]]
