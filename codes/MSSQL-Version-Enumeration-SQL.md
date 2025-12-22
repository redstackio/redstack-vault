---
id: 35e0a205-688d-474d-80a5-261a70511475
name: MSSQL-Version-Enumeration-SQL
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:33.552555+00:00'
updated_at: '2023-04-10T20:22:39.770690+00:00'
platforms:
  - Windows
  - Linux
tags:
  - mssql
  - sql
  - enumeration
validated: true
---

# MSSQL-Version-Enumeration-SQL

## Code

```sql
SELECT @@version
```

## Description

This SQL code snippet retrieves the version details of a Microsoft SQL Server instance, including version number, build, edition, and OS information. It is a fundamental reconnaissance query used to fingerprint the database for potential exploits.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; this is a static query. Execution context (e.g., connection string) is handled by the client tool. | N/A |

## Usage

Execute this query in an MSSQL client like sqlcmd, Azure Data Studio, or via SQL injection in a vulnerable web application. For example, in a union-based SQLi: append ' UNION SELECT @@version -- to a query. Useful in initial database enumeration during pentests or after gaining low-priv access.

## Detection

- Database query logs showing SELECT @@version or similar system variable queries.
- Web application logs with injection payloads containing @@version.
- Intrusion detection systems (IDS) rules for SQLi patterns targeting version info.
- Monitor for unusual SELECT queries from untrusted sources.

## Related

- [[procedures/Enumerate-MSSQL-Version]]
- [[commands/mssql-select-version]]
