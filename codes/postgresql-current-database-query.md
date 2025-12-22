---
type: code
language: sql
verified: true
tags:
  - postgresql
  - discovery
  - sqli
platforms:
  - PostgreSQL
validated: true
---

# postgresql-current-database-query

## Code

```sql
SELECT current_database()
```

## Description

This SQL code snippet executes the `current_database()` function to retrieve the name of the active PostgreSQL database. It is a simple, built-in query useful for enumeration in SQL injection scenarios or legitimate database administration, providing insight into the database instance without needing elevated privileges.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; the query is static and executes immediately upon injection or direct run. | N/A |

## Usage

Inject this query into a vulnerable parameter (e.g., via Burp Suite repeater or sqlmap) or run it in a psql session after gaining database access. In red team operations, use it early in discovery to identify the target database for targeted table enumeration or data extraction. For evasion, wrap in comments or encode if the application filters inputs.

## Detection

- Monitor PostgreSQL logs for `current_database()` executions from unexpected sources or IPs.
- Web application logs showing anomalous SQL patterns in parameters (e.g., union selects).
- Intrusion detection systems (IDS) signatures for SQLi payloads containing database functions.

## Related

- [[procedures/PostgreSQL-Database-Name-Enumeration]]
- [[techniques/System Information Discovery|T1082 - System Information Discovery]]
