---
type: code
language: sql
verified: true
tags:
  - sqli
  - comment-bypass
  - bigquery
platforms:
  - GCP
validated: true
---

# BigQuery-SQL-Injection-Comment-Example

## Code

```sql
select 1#from here it is not working
select 1/*between those it is not working*/
```

## Description

This SQL snippet illustrates the use of line comments (#) and block comments (/* */) in BigQuery queries to demonstrate how they can be leveraged in SQL injection attacks. By injecting these comments into a vulnerable parameter, an attacker can terminate the original query prematurely and append malicious SQL, bypassing filters that do not parse within comments. This is useful for evading web application filters or WAF rules that block direct keywords like 'UNION' or 'SELECT' without considering comment contexts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static example payload; customize by replacing '1' with injection logic (e.g., '1 # UNION SELECT username FROM users'). | N/A |

## Usage

Inject this payload into a vulnerable input field or API parameter in an application that constructs BigQuery queries. For instance, in a search endpoint: 'q=1 # UNION SELECT * FROM secrets --'. Use tools like Burp Suite to intercept and modify requests. This code serves as a building block for more complex injections, such as data exfiltration via UNION queries.

## Detection

- Monitor BigQuery query logs for unusual comment usage or truncated queries.
- Application logs showing SQL errors with comment artifacts.
- WAF alerts on payloads containing # or /* */ near SQL keywords.
- Anomalous data access patterns in Cloud Audit Logs.

## Related

- [[procedures/BigQuery-SQL-Injection-Using-Comment-Syntax]]
