---
id: 8d11716c-23e0-4715-805b-6fb4852c4503
name: mssql-impersonation-credential-check-script
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:21.034010+00:00'
updated_at: '2023-04-10T20:36:37.210308+00:00'
platforms:
  - Windows
tags:
  - impersonation
  - discovery
  - mssql
validated: true
---

# mssql-impersonation-credential-check-script

## Code

```sql
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
EXECUTE AS LOGIN = 'adminuser'
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
SELECT ORIGINAL_LOGIN()
```

## Description

This SQL script performs a complete impersonation check in MSSQL Server: it queries the current system user and sysadmin role status, impersonates a target login ('adminuser'), re-queries the context and role under the new identity, and finally retrieves the original login. It is used for privilege discovery and verification during post-exploitation without altering the database.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'adminuser' | Target login to impersonate (hardcoded; replace as needed) | 'domain\\adminuser' |

## Usage

Execute the entire script in SSMS or sqlcmd against a SQL Server instance where you have IMPERSONATE rights. Use before attempting escalation to map privileges. Follow with `REVERT;` to end impersonation. This script can be delivered via SQL injection or direct console access in red team engagements.

## Detection

- SQL Server logs for EXECUTE AS events (audit 'IMPERSONATION' actions).
- Queries to SYSTEM_USER, IS_SRVROLEMEMBER, or ORIGINAL_LOGIN in transaction logs.
- Anomalous role checks or impersonations from low-priv logins via Extended Events.

## Related

- [[procedures/mssql-impersonation-credential-check]]
- [[tools/sqlcmd]] (for execution)
