---
id: b1894b1e-e024-480a-86b0-3e5f0ae148c7
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.988809+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Effective-Permissions-from-the-Database]]'
  - '[[tags/Manual-SQL-Server-Queries]]'
  - '[[tags/MSSQL-Server]]'
commands:
  - '[[commands/sqlcmd-execute-query]]'
tools:
  - '[[tools/sqlcmd]]'
platforms:
  - Windows
  - MSSQL Server
validated: true
---

# Query-MSSQL-Effective-Database-Permissions

## Summary

This procedure uses a SQL query to enumerate the effective permissions of users on a Microsoft SQL Server database, allowing an attacker with valid credentials to assess access levels, identify high-privilege accounts, and plan privilege escalation or data exfiltration.

## Description

In a penetration testing or red team scenario, discovering effective permissions within an MSSQL Server database is a key discovery technique. By executing the fn_my_permissions function, the procedure retrieves a comprehensive list of permissions granted to users or roles on database objects. This can reveal overly permissive configurations, such as users with SELECT, INSERT, UPDATE, or EXECUTE rights on sensitive tables. The query targets the database scope but can be adapted for other objects like tables or schemas. Prerequisites include authenticated access to the SQL Server instance, typically via a low-privilege account. Success enables mapping of the attacker's current access and identifying paths to broader compromise, such as dumping credentials or querying linked servers.

## Requirements

1. Valid SQL Server credentials with at least read access to system views (e.g., db_datareader role or equivalent).
2. Network access to the SQL Server instance (default port 1433/TCP).
3. Installed sqlcmd utility or equivalent SQL client on the attacker's machine.
4. Knowledge of the target database name and server hostname/IP.

## Defense

- Implement principle of least privilege by granting minimal permissions to database users and regularly auditing roles with tools like SQL Server Audit or extended events.
- Enable logging of failed and successful queries via SQL Server Profiler or Query Store to detect anomalous permission checks.
- Use database activity monitoring (DAM) solutions to alert on queries accessing system functions like fn_my_permissions.
- Rotate credentials frequently and enforce multi-factor authentication for database access where possible.

## Objectives

1. Enumerate permissions for all users (or a specific user) on the target database to understand access boundaries.
2. Identify misconfigurations, such as excessive grants, to support privilege escalation planning.
3. Gather intelligence on database structure and sensitive data accessibility for subsequent exfiltration or lateral movement.

## Instructions

### Step 1: Connect to the SQL Server Instance

**Context**: Establish a connection to the target MSSQL Server using sqlcmd to authenticate and prepare for query execution. This step verifies credentials and sets the context to the desired database.

Use the [[commands/sqlcmd-execute-query]] command to connect, specifying the server, database, and credentials.

```bash
sqlcmd -S $_SERVER -d $_DATABASE -U $_USERNAME -P $_PASSWORD
```

> If connection succeeds, you will enter the sqlcmd interactive mode (1> prompt). If using -Q for non-interactive, the query runs immediately. Common errors include login failures (indicating invalid creds) or connection timeouts (network/firewall issues).

### Step 2: Execute the Permissions Query

**Context**: Run the SQL query to list effective permissions. Using NULL for the principal retrieves permissions for the current user or all applicable; specify a username for targeted enumeration. This leverages the built-in fn_my_permissions function to avoid direct access to sensitive system tables.

Reference the [[codes/MSSQL-Effective-Permissions-Database-Query]] code and execute it via sqlcmd.

**Command** ([[commands/sqlcmd-execute-query]]):

```bash
sqlcmd -S $_SERVER -d $_DATABASE -U $_USERNAME -P $_PASSWORD -Q "SELECT * FROM fn_my_permissions(NULL, 'DATABASE');"
```

> The query returns columns like entity_name (e.g., the database), subentity_name, permission_name (e.g., SELECT, ALTER), and state_desc (e.g., GRANT). For NULL principal, it shows current user permissions; adjust to a specific user if VIEW DEFINITION rights allow. Expected output is a table listing permissions; no rows indicate minimal access.

### Step 3: Analyze and Verify Output

**Context**: Review the results to map permissions and validate findings. Look for high-impact permissions like CONTROL or UNSAFE ASSEMBLY, which could enable code execution or full control.

Export results for analysis if needed:

**Command** ([[commands/sqlcmd-execute-query]]):

```bash
sqlcmd -S $_SERVER -d $_DATABASE -U $_USERNAME -P $_PASSWORD -Q "SELECT * FROM fn_my_permissions(NULL, 'DATABASE');" -o permissions_output.txt -s "," -w 200
```

> The -o flag saves to file, -s sets comma separator for CSV, -w adjusts width. Success is confirmed by non-empty output showing permission details. Cross-reference with database schema (e.g., via sp_helpdb) to prioritize targets.
