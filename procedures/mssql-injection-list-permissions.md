---
id: 4d390b1c-23b7-4844-8350-8fd5658434e0
name: mssql-injection-list-permissions
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.167537+00:00'
updated_at: '2023-04-10T20:22:47.315515+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - mssql-injection
  - list-permissions
  - database-discovery
commands:
  - '[[commands/mssql-check-server-permissions]]'
  - '[[commands/mssql-check-database-permissions]]'
  - '[[commands/mssql-view-permissions-for-object]]'
  - '[[commands/mssql-check-sysadmin-role-membership]]'
platforms:
  - Windows
  - MSSQL
tools: []
validated: true
---

# mssql-injection-list-permissions

## Summary

This procedure exploits SQL injection vulnerabilities in Microsoft SQL Server (MSSQL) to enumerate server-level, database-level, and object-specific permissions for the current user, as well as check membership in server roles like sysadmin. It helps attackers assess their access rights and identify escalation opportunities in a compromised database environment.

## Description

In a SQL injection attack on an MSSQL database, an attacker injects malicious SQL code through unsanitized input fields, such as web application forms or APIs, to execute arbitrary queries. This procedure focuses on using built-in MSSQL functions like fn_my_permissions and is_srvrolemember to discover permissions without needing additional tools beyond a SQL execution interface. It is typically used after initial access via SQLi to map the database landscape, understand privilege levels, and plan further actions like data exfiltration or privilege escalation. The target environment is an MSSQL server exposed through a vulnerable web application, often on Windows platforms. Expected outcomes include detailed permission reports that reveal if the user has rights to SELECT, INSERT, EXECUTE, or administrative roles, enabling targeted follow-on exploitation.

## Requirements

1. Valid SQL injection point in a web application connected to an MSSQL database (e.g., via UNION-based or error-based injection).
2. Ability to execute arbitrary SQL queries, such as through sqlcmd, a web-based SQL client, or an injection payload delivered via tools like Burp Suite or sqlmap.
3. Basic knowledge of MSSQL syntax and injection techniques to craft payloads that bypass basic filters.
4. Network access to the target application and database port (default TCP 1433).

## Defense

- Implement parameterized queries and prepared statements in application code to prevent SQL injection.
- Apply the principle of least privilege by granting minimal permissions to database users associated with web applications.
- Enable SQL Server auditing and logging for query execution, monitoring for anomalous permission checks or function calls like fn_my_permissions.
- Use web application firewalls (WAFs) to detect and block injection patterns, and regularly scan for vulnerabilities with tools like sqlmap or Nessus.

## Objectives

1. Enumerate effective permissions at server, database, and object levels to understand current access scope.
2. Verify membership in privileged server roles to identify potential escalation paths.
3. Gather intelligence on database structure for targeted exploitation, such as accessing sensitive views or escalating to sysadmin.

## Instructions

### Step 1: Check Server-Level Permissions

**Context**: This step uses the fn_my_permissions function to list all effective permissions the current user has on the entire server, helping identify broad administrative rights like CREATE DATABASE or ALTER ANY LOGIN.

**Command** ([[commands/mssql-check-server-permissions]]):
```sql
SELECT * FROM fn_my_permissions(NULL, 'SERVER');
```

> This query returns a result set with columns including permission_name (e.g., CONTROL SERVER), permission_state (GRANT/DENY), and class_desc (SERVER). It executes quickly and provides an overview of server-wide access. If the output shows high-privilege grants, consider escalating immediately.

### Step 2: Check Database-Level Permissions

**Context**: Query database-specific permissions to see rights like SELECT ANY TABLE or ALTER on schemas, which indicate potential for data manipulation within the current database.

**Command** ([[commands/mssql-check-database-permissions]]):
```sql
SELECT * FROM fn_my_permissions(NULL, 'DATABASE');
```

> The output includes permission_name (e.g., SELECT), subentity_name (if applicable), and class_desc (DATABASE). Look for grants on key objects; denied permissions may highlight restrictions to work around.

### Step 3: View Permissions for a Specific Object

**Context**: For targeted enumeration, check permissions on a specific database object like a view (e.g., Sales.vIndividualCustomer) to assess read/write access to sensitive data structures.

**Command** ([[commands/mssql-view-permissions-for-object]]):
```sql
SELECT * FROM fn_my_permissions('Sales.vIndividualCustomer', 'OBJECT') ORDER BY subentity_name, permission_name;
```

> Results show permissions like SELECT or UPDATE on the specified object, ordered for easy review. Adapt the object name based on prior enumeration (e.g., from INFORMATION_SCHEMA views). Success confirms granular access to business-critical data.

### Step 4: Check Sysadmin Role Membership

**Context**: Determine if the current user is a member of the sysadmin server role, which grants full control over the SQL Server instance, enabling unrestricted actions like xp_cmdshell execution.

**Command** ([[commands/mssql-check-sysadmin-role-membership]]):
```sql
-- possible roles: sysadmin, serveradmin, dbcreator, setupadmin, bulkadmin, securityadmin, diskadmin, public, processadmin
SELECT is_srvrolemember('sysadmin');
```

> The query returns 1 if the user is a member (success for attacker) or 0 otherwise. Repeat for other roles like 'securityadmin' by changing the argument to map privilege levels comprehensively.
