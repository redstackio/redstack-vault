---
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:37.054006+00:00'
updated_at: '2023-04-10T20:24:30.505330+00:00'
tags:
  - boolean-enumeration
  - sqlite-injection
  - table-length
platforms:
  - Databases
  - SQLite
validated: true
---

# SQLite-Table-Name-Length-Boolean-Query

## Code

```sql
and (SELECT length(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%' limit 1 offset 0)=table_name_length_number
```

## Description

This SQL snippet is a boolean condition payload used in SQL injection attacks against SQLite databases to determine the length of the first user-created table name. It queries the sqlite_master metadata table, filters for non-system tables, and compares the length to a test value. When injected into a vulnerable parameter, it causes the application to respond differently based on whether the length matches, enabling blind enumeration.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| table_name_length_number | Integer value to test against the actual table name length (try 1-30 sequentially) | 8 |

## Usage

Inject this payload into a confirmed boolean SQL injection point, such as a numeric ID parameter in a URL or form (e.g., ?id=1' [payload] --). Observe the application's response: a normal page indicates true (length match), while an error or altered page indicates false. Used as the first step in table enumeration during database schema discovery in web application penetration testing or red team engagements.

## Detection

- Web application logs showing repeated queries to sqlite_master with length functions and varying integer comparisons.
- Intrusion detection systems (IDS) alerting on SQL injection patterns involving system table access or boolean conditions.
- Application monitoring for unusual response time variations or error rates from injection attempts.
- Database audit logs capturing unauthorized metadata queries.

## Related

- [[procedures/SQLite-Boolean-Table-Enumeration]]
