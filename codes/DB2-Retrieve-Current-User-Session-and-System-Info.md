---
id: b14c2403-e030-45be-95c2-5c09369fed56
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:32.597587+00:00'
updated_at: '2023-04-10T20:21:57.621230+00:00'
tags:
  - DB2
  - SQL Injection
  - User Enumeration
platforms:
  - Databases
  - DB2
validated: true
---

# DB2-Retrieve-Current-User-Session-and-System-Info

## Code

```sql
select user from sysibm.sysdummy1
select session_user from sysibm.sysdummy1
select system_user from sysibm.sysdummy1
```

## Description

This SQL code snippet executes three queries against the DB2 system dummy table to retrieve key user context information: the current database user, the session authorization ID, and the underlying system user. It is designed for injection into vulnerable applications to perform discovery without requiring additional privileges or data manipulation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This code has no variables; it uses built-in DB2 functions and tables. | N/A |

## Usage

Inject this code via SQL injection in a vulnerable DB2-connected application, such as appending it to a SELECT statement using UNION or error-based techniques. For example, in a search parameter: ' UNION SELECT user FROM sysibm.sysdummy1 --. Execute in the context of an active database session to enumerate the user under which the application operates. Useful in red team engagements for mapping database privileges before escalation.

## Detection

- Monitor database query logs for SELECT statements targeting SYSIBM.SYSDUMMY1, which is unusual for legitimate application queries.
- Implement anomaly detection in SQL traffic for concatenated or union-based injections.
- Enable DB2 audit facilities to log user and session queries, alerting on access to system metadata tables.

## Related

- [[procedures/DB2-Current-User-Information-Retrieval-via-SQL-Injection]]
