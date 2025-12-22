---
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.833825+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - sqli
  - payload
  - time-based
  - postgresql
validated: true
---

# PostgreSQL-pg-sleep-Delay-Payload

## Code

```sql
select 1 from pg_sleep(5)
;(select 1 from pg_sleep(5))
||(select 1 from pg_sleep(5))
```

## Description

This SQL code snippet contains variations of payloads using PostgreSQL's pg_sleep function to introduce a 5-second delay during query execution. It can be injected into vulnerable parameters to confirm time-based blind SQL injection, perform data inference via conditional delays, or cause denial-of-service by overwhelming the database with slow queries. The three forms (simple select, semicolon-separated, and concatenated) account for different filtering or parsing behaviors in web applications.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | The sleep duration is hardcoded to 5 seconds; modify pg_sleep(N) for different delays | pg_sleep(10) for 10-second delay |

## Usage

Inject these payloads into user-controlled inputs (e.g., URL parameters, POST data) in a web app connected to PostgreSQL. For confirmation: Append to a query like '1; [payload]--'. For extraction: Wrap in conditions like 'AND (IF(condition, pg_sleep(5), 0))--'. Use tools like curl or Burp Suite to send and time requests. This is typically part of blind SQLi procedures where no data is directly outputted.

## Detection

- Database logs showing pg_sleep executions or queries exceeding normal timeouts.
- Application-level monitoring for response times >3 seconds on routine requests.
- WAF rules matching 'pg_sleep' or unusual SQL concatenation/semicolons.
- Network traffic analysis for repeated delayed HTTP responses from the same IP.

## Related

- [[procedures/PostgreSQL-Time-Based-Blind-SQL-Injection]]
- [[commands/curl-inject-postgresql-sleep-payload]]
