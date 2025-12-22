---
id: f20cd0c2-c621-49cc-86c9-653df3833a6b
name: mssql-sp-addsrvrolemember-grant-sysadmin
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:34.072981+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - privilege-escalation
  - sql-injection-payload
validated: true
---

# mssql-sp-addsrvrolemember-grant-sysadmin

## Code

```sql
EXEC master.dbo.sp_addsrvrolemember 'user', 'sysadmin';
```

## Description

This SQL code invokes the sp_addsrvrolemember system stored procedure in the master database to add a specified login ('user') as a member of the sysadmin fixed server role, granting full administrative privileges over the MSSQL instance. It is typically injected via a SQL injection vulnerability to escalate privileges without direct authentication.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'user' | The login name to add to the role | 'attacker_user' |
| 'sysadmin' | The target fixed server role | 'sysadmin' |

## Usage

Embed this code in a SQL injection payload, e.g., in a stacked query: '; EXEC master.dbo.sp_addsrvrolemember 'attacker_user', 'sysadmin'; --. Deliver via tools like sqlmap or manual HTTP requests. Prerequisite: The login must exist (create via prior injection if needed). After execution, connect with the new credentials to exploit DBA access, such as enabling xp_cmdshell for OS command execution.

## Detection

- Monitor MSSQL error logs and audit traces for sp_addsrvrolemember executions, especially from non-admin sessions.
- Alert on role membership changes: Query sys.server_role_members for anomalies.
- Web application logs showing unusual SQL patterns or failed sanitization.
- Network traffic analysis for injection attempts on port 1433 or proxied via web apps.

## Related

- [[procedures/MSSQL-Injection-to-Grant-DBA-Access]]
- [[tools/sqlmap]]
