---
id: caa174ad-57e2-4167-82b3-98240e3fc5c4
name: MySQL-Time-Based-Blind-Injection-Payloads
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.721926+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - MySQL
tags:
  - sqli
  - blind-injection
  - time-based
validated: true
---

# MySQL-Time-Based-Blind-Injection-Payloads

## Code

```sql
?id=1 AND IF(ASCII(SUBSTRING((SELECT USER()),1,1)))>=100,1, BENCHMARK(2000000,MD5(NOW()))) --
?id=1 AND IF(ASCII(SUBSTRING((SELECT USER()), 1, 1)))>=100, 1, SLEEP(3)) --
?id=1 OR IF(MID(@@version,1,1)='5',sleep(1),1)='2
```

## Description

These SQL payloads demonstrate time-based blind injection using MySQL's IF conditional with delay functions. The first two test if the first character of the current database user has ASCII >=100, triggering BENCHMARK (CPU delay) or SLEEP (sleep delay) on false. The third checks the MySQL version starting with '5' using SLEEP(1). They are designed for injection into URL parameters like ?id= to infer data via response time differences.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| USER() | MySQL function returning current user | root@localhost |
| @@version | MySQL system variable for version | 5.7.44 |
| SUBSTRING(...,1,1) | Extracts first character | r (from root) |
| ASCII(...) | Returns ASCII value | 114 (for 'r') |

No user-defined variables; adapt the condition (e.g., >=100) for binary search.

## Usage

Inject into vulnerable web parameters via tools like curl or Burp Suite. For example, append to ?id= in a GET request. Measure response times: short (~0.5s) for true (no delay), long (2-3s) for false. Use in red team engagements to exfil data from blind endpoints or CTFs. Chain with information_schema queries for broader extraction.

## Detection

- Web logs showing anomalous query times or functions like SLEEP/BENCHMARK.
- WAF rules matching IF, ASCII, SUBSTRING patterns in parameters.
- Database audit logs for repeated conditional queries from single IP.
- Response time monitoring alerting on >2s delays.

## Related

- [[procedures/MySQL-Time-Based-Blind-Injection-Using-Conditionals]]
- [[tools/sqlmap]]
