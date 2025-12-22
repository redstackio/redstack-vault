---
id: 7ee352f6-8021-4120-8cb6-44deebd4dc0c
name: sql-basic-len-subquery
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:33.401997+00:00'
updated_at: '2023-04-10T20:22:25.420433+00:00'
platforms:
  - SQL Server
tags:
  - sql-injection
  - hql
validated: true
---

# sql-basic-len-subquery

## Code

```sql
SELECT LEN((SELECT(1)))
```

## Description

A basic SQL code snippet that measures the length of a subquery result, serving as an initial test for HQL injection vulnerabilities to confirm SQL execution capability.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (SELECT(1)) | Subquery returning constant 1 | N/A |

## Usage

Embed this in application inputs to probe for injection. If it returns 1 without errors, the point is vulnerable to further payloads.

## Detection

- Query logs showing unexpected subqueries in LEN functions.
- Input validation alerts for nested SELECT statements.

## Related

- [[procedures/Hibernate-Query-Language-Injection-Using-Unicode]]
