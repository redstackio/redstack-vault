---
id: 2f865ca6-656d-4bae-8804-9cedc1dccdff
name: Enumerate-MSSQL-Server-Logins
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.847194+00:00'
updated_at: '2023-04-10T20:36:42.853427+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/MSSQL-Server]]'
  - '[[tags/Logins-Enumeration]]'
  - '[[tags/Database-Discovery]]'
  - '[[tags/Manual-SQL-Queries]]'
commands:
  - '[[commands/query-mssql-sys-server-principals]]'
platforms:
  - Windows
  - Linux
  - Database
tools: []
validated: true
---

# Enumerate-MSSQL-Server-Logins

## Summary

This procedure enumerates all server logins on a Microsoft SQL Server (MSSQL) instance by querying the sys.server_principals system view. It excludes server roles to focus on user and login accounts, providing details such as names, types, and authentication methods. This is useful in red team engagements for identifying potential accounts to target for privilege escalation or lateral movement, or in defensive auditing to review access controls.

## Description

In a security assessment, discovering active logins on an MSSQL server reveals the attack surface for account compromise. The sys.server_principals view contains metadata on server-level principals, including SQL logins, Windows logins, and certificates. By filtering out server roles (type_desc != 'SERVER_ROLE'), the query isolates actionable accounts. This technique applies in scenarios where initial access to the database has been gained via weak credentials or misconfigurations. Success depends on the executing user's permissions, typically requiring VIEW DEFINITION or higher. The output helps map user privileges and authentication types (SQL vs. Windows), aiding in targeted follow-up actions like password spraying or SID enumeration.

## Requirements

1. Authenticated session to the MSSQL server (e.g., via SQL Server Management Studio (SSMS), sqlcmd, or a connected application).
2. Permissions to query system views (at minimum, public role access; ideally db_owner or sysadmin for full details).
3. Access to a SQL query executor (e.g., SSMS, sqlcmd tool, or integrated in a scripting language like Python with pyodbc).
4. Network connectivity to the MSSQL instance (default port 1433).

## Defense

Defensive measures and detection strategies:

- Restrict query permissions on system views to sysadmin only, using DENY VIEW DEFINITION on sensitive principals.
- Enable SQL Server Audit for SELECT operations on sys.server_principals to log unauthorized enumerations.
- Implement least privilege: Use Windows Authentication over SQL logins and regularly rotate credentials.
- Monitor for anomalous queries via Extended Events or SQL Trace, alerting on sys.server_principals access from non-admin accounts.

## Objectives

1. Retrieve a list of all non-role server principals (logins) on the MSSQL instance.
2. Identify authentication types (SQL vs. Windows) and principal IDs for further enumeration.
3. Assess potential security risks, such as weak or default logins, to inform escalation paths.

## Instructions

### Step 1: Connect to the MSSQL Instance and Execute the Enumeration Query

**Context**: Establish a connection to the target MSSQL server and run the query to list server logins. This step assumes you have valid credentials; if not, obtain them via prior reconnaissance. The query filters out server roles to display only user-relevant principals, providing name, SID, type, and authentication details.

**Command** ([[commands/query-mssql-sys-server-principals]]):

Use a SQL executor like sqlcmd or SSMS to run the following query. For sqlcmd, replace placeholders with your server details.

```sql
SELECT * FROM sys.server_principals WHERE type_desc != 'SERVER_ROLE';
```

**Code** ([[codes/mssql-enumerate-server-principals-query]]):

The core SQL code is embedded above for direct execution.

> This command retrieves columns like name, principal_id, type_desc (e.g., SQL_LOGIN, WINDOWS_LOGIN), is_disabled, and create_date. If the query succeeds without errors, it indicates sufficient permissions. Review the output for disabled accounts (is_disabled = 1) or recent creations that might indicate recent changes.

### Step 2: Analyze and Verify Results

**Context**: Parse the output to identify high-value targets, such as service accounts or admins. Cross-reference with sys.server_role_members for role assignments if permissions allow.

No specific command here; manually inspect the result set or export to a file for analysis (e.g., in SSMS, right-click results > Save Results As).

> Expected: A table with rows for each login, excluding roles like dbcreator or sysadmin. If no rows return, either no logins exist (unlikely) or permissions are insufficient—escalate privileges first.
