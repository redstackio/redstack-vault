---
type: code
language: SQL
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - sql-injection
  - db2
  - case-statement
  - blind-injection
platforms:
  - Databases
  - DB2
validated: true
---

# db2-case-statement-boolean-test

## Code

```sql
select CASE WHEN (1=1) THEN 'AAAAAAAAAA' ELSE 'BBBBBBBBBB' END from sysibm.sysdummy1
```

## Description

This SQL code snippet demonstrates a basic boolean-based blind injection payload using DB2's CASE statement. It tests a condition (here, always true: 1=1) and returns a distinguishable string ('AAAAAAAAAA' for true, 'BBBBBBBBBB' for false) from the dummy table sysibm.sysdummy1. In injection scenarios, replace the condition with database queries to infer data based on application responses.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (1=1) | Boolean condition to test; replace with data extraction logic like (substring(table.column,1,1)='a') | (SELECT COUNT(*) FROM users > 0) |
| 'AAAAAAAAAA' | String returned on true condition (choose long/distinct for easy detection in responses) | 'true-indicator' |
| 'BBBBBBBBBB' | String returned on false condition | 'false-indicator' |
| sysibm.sysdummy1 | Dummy table for non-disruptive testing; replace if targeting real tables | sysibm.sysdummy1 |

## Usage

Inject this payload into a vulnerable DB2-connected application parameter (e.g., via POST data or URL). Observe if the response contains the true/false strings or alters behavior (e.g., page load time). Use in procedures like [[procedures/DB2-Injection-Using-CASE-Statement]] for step-by-step data exfiltration. Automate with tools like sqlmap by providing custom payloads.

## Detection

- Database logs showing unusual CASE statements with dummy tables or conditional logic on user input.
- Application logs with high volumes of similar queries or response anomalies (e.g., varying string lengths).
- WAF alerts for SQL keywords like CASE, WHEN, THEN in payloads.
- Monitor for iterative queries probing single characters or ASCII values.
