---
id: c50fc8a4-99b2-4cf7-b176-917f37de784b
name: sql-unicode-len-select-statement
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:33.401902+00:00'
updated_at: '2023-04-10T20:22:25.420433+00:00'
platforms:
  - SQL Server
tags:
  - unicode-bypass
  - sql-injection
  - hql
validated: true
---

# sql-unicode-len-select-statement

## Code

```sql
SELECT LEN([U+00A0](select[U+00A0](1))
```

## Description

This SQL snippet uses Unicode non-breaking spaces (U+00A0) to inject a subquery into a LEN function, bypassing whitespace trimming filters in HQL applications for injection testing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [U+00A0] | Unicode non-breaking space to evade trimming | Inserted as shown |
| select(1) | Malformed subquery for length calculation | Returns value 1 |

## Usage

Inject this payload into vulnerable HQL input fields, such as search parameters, to test if Unicode allows execution of nested SQL. Use in tools like Burp Suite to modify requests.

## Detection

- Monitor database logs for queries containing non-ASCII characters like U+00A0.
- WAF rules flagging unusual Unicode in SQL patterns.
- Anomaly detection in query lengths or subquery nesting.

## Related

- [[procedures/Hibernate-Query-Language-Injection-Using-Unicode]]
