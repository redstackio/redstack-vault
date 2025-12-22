---
id: e81873e0-1ba3-4076-abb5-dbe95e8342f9
name: SQLite-Version-Query
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.940725+00:00'
updated_at: '2023-04-10T20:24:31.614633+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - sqlite
  - injection
  - discovery
validated: true
---

# SQLite-Version-Query

## Code

```sql
select sqlite_version();
```

## Description

This SQL code snippet queries the SQLite database to retrieve the version of the SQLite engine. It is a simple, built-in function that returns the compile-time version string, useful as an injection payload for discovering the database version during reconnaissance in SQL injection attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; this is a static query. | N/A |

## Usage

Inject this query into a vulnerable SQL input point in an application, such as a web form or API endpoint. For example, in a UNION-based injection: `UNION SELECT sqlite_version()`. Execute via manual crafting, sqlmap, or direct database access. Use it early in the attack to inform version-specific exploitation, like targeting known CVEs in older SQLite versions.

## Detection

- Monitor application logs for queries containing 'sqlite_version()'. 
- Web application firewalls can signature-match this exact string in payloads.
- Database access logs showing unexpected metadata queries from untrusted sources.
- Anomalous error responses leaking version information.

## Related

- [[procedures/SQLite-Version-Discovery-via-Injection]]
- [[codes/SQLite-Version-Query]]
