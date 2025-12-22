---
id: 5ae58021-2876-4977-a80b-888009173c60
name: mssql-user-information-queries
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:33.515164+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Database
  - MSSQL
tags:
  - sql-injection
  - discovery
validated: true
---

# mssql-user-information-queries

## Code

```sql
SELECT CURRENT_USER
SELECT user_name();
SELECT system_user;
SELECT user;
```

## Description

This SQL code snippet contains a series of queries to enumerate user information in an MSSQL database, including current session user, database username, system login, and user variable. It is designed for injection into vulnerable applications to perform account discovery without direct DB access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; static queries | N/A |

## Usage

Inject this multi-statement block via SQL injection points supporting semicolons (e.g., `'; [code here] --`). Use in reconnaissance phases to map database privileges. For blind injections, wrap each in conditional statements (e.g., IF (SELECT CURRENT_USER)='sa' THEN WAITFOR DELAY '00:00:05'). Related to procedures like [[procedures/Retrieve-MSSQL-User-Information-via-SQL-Injection]].

## Detection

- Database logs showing SELECT on system functions like user_name() or system_user from untrusted IPs.
- WAF alerts for multi-statement SQL or keywords like CURRENT_USER in payloads.
- Anomalous query patterns targeting sysusers or equivalent views.

## Related

- [[procedures/Retrieve-MSSQL-User-Information-via-SQL-Injection]]
