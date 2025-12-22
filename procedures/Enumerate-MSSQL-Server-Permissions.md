---
type: procedure
description: >-
  Query the MSSQL Server to enumerate effective permissions for the current
  user, identifying potential access levels and attack vectors.
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.959915+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Permission-Groups-Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Effective-Permissions-from-the-Server]]'
  - '[[tags/Manual-SQL-Server-Queries]]'
  - '[[tags/MSSQL-Server]]'
commands:
  - '[[commands/Retrieve-MSSQL-Server-Permissions]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enumerate-MSSQL-Server-Permissions

## Summary

This procedure queries an MSSQL Server instance to enumerate the effective permissions granted to the current user at the server level. It helps identify what actions the user can perform, such as creating databases, managing logins, or executing administrative tasks, which is useful for assessing privilege levels during penetration testing or security audits.

## Description

Enumerating server permissions on an MSSQL instance reveals the explicit and inherited permissions for the connected user, including roles like sysadmin or dbcreator. This technique is typically used after gaining initial database access to map out escalation paths or lateral movement opportunities. The query leverages the built-in `fn_my_permissions` function, which returns permission names, states (e.g., GRANT, DENY), and types. In an attack scenario, this information can highlight misconfigurations, such as overly permissive roles, enabling further exploitation like credential dumping or process injection if elevated privileges are confirmed.

## Requirements

1. Authenticated access to the MSSQL server via SQL Server Management Studio (SSMS), sqlcmd, or a similar client.
2. Valid login credentials with at least public or server-level access.
3. Basic knowledge of SQL syntax and MSSQL system functions.
4. Network connectivity to the MSSQL port (default TCP 1433).

## Defense

- Restrict database access to least privilege principles, using role-based access control (RBAC) and auditing login permissions regularly.
- Enable SQL Server Audit to log permission queries and failed access attempts.
- Implement network segmentation and firewalls to limit exposure of MSSQL instances.
- Monitor for anomalous queries via SQL Profiler or Extended Events, alerting on uses of functions like `fn_my_permissions`.

## Objectives

1. Identify the current user's effective server-level permissions to assess potential attack vectors.
2. Determine if the user has elevated roles (e.g., sysadmin) that enable privilege escalation.
3. Document permission states to inform mitigation strategies and risk assessment.

## Instructions

### Step 1: Connect to the MSSQL Instance

**Context**: Establish a connection to the target MSSQL server using a SQL client to execute server-level queries. This step ensures you have the necessary authenticated session.

Use SSMS or sqlcmd to connect with your credentials. For example, via sqlcmd:

```bash
sqlcmd -S target_server -U username -P password
```

> Once connected, you are ready to query permissions. Verify connection success by running a simple query like `SELECT @@VERSION;` which should return the server version without errors.

### Step 2: Execute the Permissions Enumeration Query

**Context**: Run the query to retrieve effective permissions for the current user on the server. This reveals grants, denies, and role memberships that determine your access scope.

**Command** ([[commands/Retrieve-MSSQL-Server-Permissions]]):

```sql
select * from fn_my_permissions(null, 'server');
```

> The `fn_my_permissions` function with `null` as the principal and `'server'` as the securable class lists all server-level permissions. Columns include `entity_name` (permission name), `subentity_name`, `permission_state` (e.g., GRANT), and `permission_state_value`. If the user has sysadmin role, expect broad permissions like CREATE ANY DATABASE or ALTER ANY LOGIN.

### Step 3: Analyze the Results

**Context**: Review the output to identify high-value permissions and decide on next actions, such as attempting privilege escalation if administrative rights are present.

Parse the results manually or export to a file for analysis:

```sql
select * from fn_my_permissions(null, 'server') INTO OUTFILE 'permissions.txt';
```

> Look for permissions like `CONTROL SERVER` (full admin) or `CREATE LOGIN` (user management). If no high privileges, consider enumerating database-specific permissions next with `fn_my_permissions('database', 'DATABASE')`.

## Expected Output

Successful execution produces a result set like:

| entity_name | subentity_name | permission_state | permission_state_value |
|-------------|----------------|------------------|-----------------------|
| CREATE ANY DATABASE | NULL | GRANT | 1 |
| ALTER ANY LOGIN | NULL | GRANT | 1 |
| CONTROL SERVER | NULL | DENY | 0 |

This indicates the user can create databases and alter logins but is denied full server control. Empty results suggest minimal access (e.g., public role only).
