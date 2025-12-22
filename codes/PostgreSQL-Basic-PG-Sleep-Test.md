---
id: new-uuid-for-basic-sleep
type: code
language: SQL
verified: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - postgresql
  - sql-injection
  - time-based
  - blind-sqli
platforms:
  - Database
validated: true
---

# PostgreSQL-Basic-PG-Sleep-Test

## Code

```sql
SELECT pg_sleep(5);
```

## Description

This SQL code snippet tests for time-based blind SQL injection by forcing a 5-second delay using PostgreSQL's pg_sleep function. It is injected into vulnerable parameters to confirm if the database executes arbitrary SQL and delays responses predictably, without producing visible output or errors.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; fixed 5-second sleep for clear delay detection. Adjust sleep duration if network latency is high (e.g., pg_sleep(10)). | N/A |

## Usage

Inject into a vulnerable input like a search query or ID parameter: e.g., id=1' OR (SELECT pg_sleep(5))--. Use in web requests via Burp Suite or curl. Measure total response time; a delay of ~5 seconds indicates successful injection. This is the first step in validating blind SQLi before data extraction.

## Detection

- Database logs showing pg_sleep executions or queries exceeding 5 seconds.
- Application logs for anomalous long response times from specific endpoints.
- WAF alerts for SQL keywords like 'pg_sleep' in payloads.
- Network monitoring for repeated requests to the same vulnerable parameter with timing variations.

## Related

- [[procedures/PostgreSQL-Time-Based-Blind-SQL-Injection-for-Table-Dump]]
