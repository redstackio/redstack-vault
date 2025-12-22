---
type: code
language: sql
verified: true
tags:
  - mssql
  - sql-injection
  - payload
  - discovery
platforms:
  - Windows
  - MSSQL
validated: true
---

# mssql-hostname-enumeration-sql-payload

## Code

```sql
SELECT HOST_NAME()
SELECT @@hostname;
```

## Description

This SQL code snippet contains two equivalent queries to retrieve the hostname of the MSSQL server instance. It can be used as a stacked query payload in SQL injection attacks to enumerate system information without direct database access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; direct execution in MSSQL context | N/A |

## Usage

Inject this as a stacked payload in a vulnerable application, e.g., `'; <original query>; SELECT HOST_NAME(); SELECT @@hostname; --`. Useful in error-based, UNION-based, or blind SQLi to extract hostname for reconnaissance. Execute via tools like sqlmap with `--technique=S` for stacked queries.

## Detection

- Database query logs showing execution of HOST_NAME() or @@hostname from untrusted inputs.
- WAF alerts on UNION SELECT or stacked queries.
- Anomalous response times in blind injection attempts.

## Related

- [[procedures/mssql-hostname-enumeration-via-sqli]]
- [[commands/mssql-select-host-name]]
