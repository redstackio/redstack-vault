---
id: 80f66788-169b-462f-8a4e-60a110283c9e
name: Enumerate-MSSQL-Database-Roles-and-User-Members
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.929026+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - mssql
  - database-enumeration
  - roles
  - discovery
commands:
  - '[[commands/mssql-query-database-role-members]]'
platforms:
  - Windows
  - SQL Server
tools: []
validated: true
---

# Enumerate-MSSQL-Database-Roles-and-User-Members

## Summary

This procedure enables enumeration of all database roles and their user members on a Microsoft SQL Server (MSSQL) instance. It helps identify privilege structures, such as high-privilege roles like db_owner or sysadmin, which can reveal opportunities for privilege escalation or lateral movement within the database environment.

## Description

In an attack scenario, enumerating database roles and members provides insight into the access control model of the MSSQL Server. Attackers with valid credentials can query system views to list roles (e.g., db_datareader, db_ddladmin) and their assigned users or principals. This is particularly useful post-initial access to a database user account, allowing mapping of permissions for further exploitation. The procedure relies on SQL queries against sys.database_role_members and sys.database_principals views, executable via tools like SQL Server Management Studio (SSMS), sqlcmd, or PowerShell's Invoke-Sqlcmd. It assumes the attacker has at least read access to these system views, typically granted to any authenticated user.

## Requirements

1. Valid credentials for an MSSQL Server account with query execution privileges (e.g., db_datareader or higher).
2. Network access to the MSSQL Server instance (default port 1433/TCP).
3. A client tool capable of executing SQL queries, such as SSMS, sqlcmd, or PowerShell.

## Defense

Defensive measures and detection strategies:

- Enforce least privilege by granting only necessary permissions to MSSQL Server users and regularly auditing role assignments.
- Monitor MSSQL Server logs (e.g., via SQL Server Audit or Extended Events) for suspicious activity, such as queries accessing sys.database_role_members from unexpected accounts or during off-hours.
- Implement network segmentation to limit the exposure of the MSSQL Server to the internet or untrusted networks, and use firewalls to restrict access to port 1433.
- Enable query logging and integrate with SIEM systems to alert on enumeration patterns.

## Objectives

1. Enumerate all database roles on the MSSQL Server instance.
2. Identify all user members assigned to each database role.
3. Map role memberships to detect potential privilege escalation paths.

## Instructions

### Step 1: Connect to the MSSQL Instance

**Context**: Establish a connection to the target MSSQL Server using your chosen client tool to prepare for query execution. This step verifies access and sets the context for the database (e.g., master or a specific user database).

**Instructions**: Launch SSMS or use sqlcmd/PowerShell to connect with your credentials. Specify the server instance (e.g., servername\instance) and authenticate. If targeting a specific database, use 'USE [DatabaseName];' after connecting.

> Ensure no errors like 'Login failed' occur, indicating successful authentication.

### Step 2: Execute the Role Enumeration Query

**Context**: Run the SQL query to retrieve database roles and their members. This uses system views to join role and member principal data, displaying roles with members or 'No members' for empty ones. The query filters for role principals (type 'R') and orders results alphabetically.

**Command** ([[commands/mssql-query-database-role-members]]):

**Code** ([[codes/mssql-enumerate-database-roles-query]]):

```sql
SELECT DB1.name AS DatabaseRoleName,
isnull (DB2.name, 'No members') AS DatabaseUserName
FROM sys.database_role_members AS DRM
RIGHT OUTER JOIN sys.database_principals AS DB1
ON DRM.role_principal_id = DB1.principal_id
LEFT OUTER JOIN sys.database_principals AS DB2
ON DRM.member_principal_id = DB2.principal_id
WHERE DB1.type = 'R'
ORDER BY DB1.name;
```

> This query returns a result set with columns for DatabaseRoleName and DatabaseUserName. Analyze the output for roles like 'db_owner' or 'sysadmin' and their members, which indicate high-privilege users. If no members appear for a role, it may still be exploitable if you can add yourself. Modify the query with WHERE clauses (e.g., WHERE DB1.name = 'db_owner') for targeted enumeration. Expected output includes rows like:
>
> DatabaseRoleName | DatabaseUserName
> ---------------- | ----------------
> db_owner         | admin_user
> public           | No members
>
> Success is indicated by a complete list without permission errors.
