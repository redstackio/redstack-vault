---
id: 5454177f-57f4-4f6e-a0c8-cedbeb32572a
name: Enumerate-Current-User-Role-in-MSSQL
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.744692+00:00'
updated_at: '2023-04-10T20:36:37.791496+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/MSSQL]]'
  - '[[tags/Role Enumeration]]'
  - '[[tags/Manual SQL Queries]]'
  - '[[tags/Discovery]]'
commands:
  - '[[commands/mssql-select-current-user]]'
  - '[[commands/mssql-query-user-roles]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enumerate-Current-User-Role-in-MSSQL

## Summary

This procedure enumerates the current user's role and associated permissions in a Microsoft SQL Server (MSSQL) database, allowing attackers to assess their level of access and privileges for planning further actions such as privilege escalation or data exfiltration.

## Description

In an MSSQL environment, attackers with initial database access can query system views and functions to discover the current user's identity and roles. This discovery technique is part of the reconnaissance phase, helping to map privileges like db_owner, db_datareader, or custom roles. It targets system catalog views such as sys.database_principals and sys.fn_my_permissions. This is typically used after gaining SQL login credentials via initial access vectors like weak authentication or SQL injection. The procedure assumes connection via tools like sqlcmd or integrated clients, and outputs role membership that informs subsequent attack paths.

## Requirements

1. Valid MSSQL login credentials with at least public role access to the target database.
2. Network connectivity to the MSSQL instance (default port 1433).
3. A SQL client such as sqlcmd (included in SQL Server tools) or integrated tools like SSMS.
4. Basic knowledge of T-SQL syntax for querying system views.

## Defense

- Enforce principle of least privilege by granting minimal roles to service accounts and users.
- Enable SQL Server auditing for login successes and query activities on system views.
- Use database firewalls or network segmentation to restrict access to MSSQL instances.
- Monitor for anomalous queries accessing sys.database_role_members or fn_my_permissions.

## Objectives

1. Identify the current user's name and database context.
2. Enumerate assigned roles and permissions to gauge access level.
3. Determine potential for escalation based on role privileges like db_owner.

## Instructions

### Step 1: Connect to the MSSQL Instance and Query Current User

**Context**: Establish a connection and retrieve the current user's identity to confirm access and start role assessment. This step verifies the session context.

**Command** ([[commands/mssql-select-current-user]]):
```sql
SELECT USER_NAME();
```

> This T-SQL command returns the name of the current user in the database context. Execute it via sqlcmd or a SQL client after logging in. If successful, it displays the username, indicating the session is active and the user context is established.

### Step 2: Query User Roles and Permissions

**Context**: Once the user is identified, query system functions to list roles and permissions, revealing privileges like SELECT, INSERT, or administrative rights.

**Command** ([[commands/mssql-query-user-roles]]):
```sql
SELECT * FROM sys.fn_my_permissions(NULL, 'DATABASE');
```

> This command lists all permissions for the current user at the database level. It outputs a table with permission names and states (e.g., GRANT, DENY). Review for high-privilege entries like 'CONTROL' or 'ALTER ANY ROLE' to assess escalation potential. If needed, join with sys.database_role_members for role details: SELECT r.name FROM sys.database_role_members rm JOIN sys.database_principals r ON rm.role_principal_id = r.principal_id WHERE rm.member_principal_id = USER_ID();
