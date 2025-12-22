---
id: deb11c1f-30d3-4514-afa8-23234bff0aa4
name: PostgreSQL-Version-Query-SQL
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.420468+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - Linux
tags:
  - sqli
  - postgresql
  - database-enumeration
validated: true
---

# PostgreSQL-Version-Query-SQL

## Code

```sql
SELECT version()
```

## Description

This SQL code snippet queries the PostgreSQL database to return the full version information of the server, including the release number, architecture, compiler details, and bit width. It is a simple, built-in function call that requires no parameters and is commonly used in reconnaissance during SQL injection attacks to fingerprint the database backend.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The `version()` function takes no variables or arguments | N/A |

## Usage

Inject this code into a vulnerable SQL endpoint, such as a web application's query parameter, to extract version details. For example, in a blind SQL injection scenario, wrap it in conditional statements to infer results. It can be delivered via tools like sqlmap (--dbms=postgresql) or manual HTTP requests with Burp Suite. This is often the first step in database enumeration to identify exploitable versions.

## Detection

- Monitor application logs for queries invoking system functions like `version()`.
- Web application firewalls (WAFs) can flag injections containing `SELECT version`.
- Database audit logs should alert on non-standard queries from application users.
- Anomaly detection in response times or error messages revealing PostgreSQL internals.

## Related

- [[procedures/PostgreSQL-Version-Retrieval-via-SQL-Injection]]
- [[techniques/Exploit Public-Facing Application|T1190]]
