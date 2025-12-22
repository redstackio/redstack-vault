---
id: da63583f-2adb-4837-a67c-50789f182ccf
name: Enumerate-MSSQL-Database-Users
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.878093+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/All Database Users for a Database]]'
  - '[[tags/Manual SQL Server Queries]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/sqlcmd-run-database-users-query]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/sqlcmd]]'
validated: true
---

# Enumerate-MSSQL-Database-Users

## Summary

This procedure enumerates all database users (excluding roles) for a specific database in a Microsoft SQL Server (MSSQL) instance. It uses a targeted SQL query against the sys.database_principals system view to retrieve user details such as names, types, and authentication methods, helping identify potential targets for privilege escalation, lateral movement, or further exploitation in a compromised environment.

## Description

In an MSSQL Server environment, database principals include users, roles, and other entities that can access database resources. This procedure focuses on non-role principals (primarily users) within a specific database, providing visibility into user accounts that could be leveraged for attacks like credential dumping or unauthorized access. The technique relies on executing a manual SQL query, which requires authenticated access to the database. It is particularly useful during post-exploitation phases where an attacker has initial database credentials and seeks to map out user privileges for deeper compromise. The query filters out database roles to focus on actionable user accounts, revealing details like SQL authentication vs. Windows authentication. This aligns with discovery activities in offensive security operations, enabling attackers to prioritize high-value targets.

## Requirements

1. Valid authentication credentials (SQL or Windows) for the MSSQL Server instance and the target database.
2. Network access to the MSSQL Server (default port 1433/TCP, or custom port).
3. A SQL client tool like sqlcmd installed on the attacker's machine for query execution.
4. Permissions to execute SELECT queries on system views (typically granted to db_datareader or equivalent roles).

## Defense

- Implement the principle of least privilege, ensuring database users have only the necessary permissions for their functions and revoking unnecessary access to system views like sys.database_principals.
- Regularly review and audit MSSQL Server logs (e.g., via SQL Server Audit or Extended Events) to detect suspicious queries, such as SELECTs on system tables from unexpected sources or failed login attempts.
- Use network segmentation and firewalls to restrict access to MSSQL instances, allowing connections only from authorized IP ranges and requiring VPN or bastion hosts for remote access.
- Enable query logging and monitoring tools like SQL Server Profiler or third-party SIEM integrations to alert on enumeration patterns.

## Objectives

1. Retrieve a list of all non-role database principals (users) in the target database.
2. Identify user types and authentication methods to assess exploitation potential.
3. Map database users for use in subsequent attacks like privilege escalation or lateral movement.

## Instructions

### Step 1: Connect to the MSSQL Instance and Execute the Enumeration Query

**Context**: Establish a connection to the target MSSQL database using sqlcmd, then run a SQL query to enumerate database users excluding roles. This step assumes you have the server details and credentials; if using Windows authentication, omit -U and -P flags.

**Command** ([[commands/sqlcmd-run-database-users-query]]):

```bash
sqlcmd -S $_SERVER -d $_DATABASE -U $_USERNAME -P $_PASSWORD -Q "SELECT * FROM sys.database_principals WHERE type_desc != 'DATABASE_ROLE';"
```

> This command connects to the specified MSSQL server and database, authenticates with the provided credentials, and executes the query inline using the -Q flag for quiet execution (outputs results directly). The query targets sys.database_principals, a system view containing all database-level principals, and filters out roles to focus on users and other entities. Run this from a machine with sqlcmd installed. If the query succeeds, it will display user details; errors may indicate insufficient permissions or connection issues.

**Expected Output**: A result set table showing columns like name, principal_id, type, type_desc, default_schema_name, create_date, modify_date, owning_principal_id, sid, is_fixed_role, authentication_type_desc. For example:

```
name                    principal_id  type  type_desc         default_schema_name  create_date           modify_date           owning_principal_id  sid                              is_fixed_role  authentication_type_desc
---------------------- ------------- ----- ------------------ -------------------- -------------------- -------------------- -------------------- --------------------------------- ------------- ----------------------------
dbo                    1             S     SQL_USER          dbo                  2023-01-01 00:00:00   2023-01-01 00:00:00   NULL                 0x01                               0             INSTANCE
user1                  5             S     SQL_USER          dbo                  2023-02-01 00:00:00   2023-02-01 00:00:00   1                    0xAABB...                          0             DATABASE
```

### Step 2: Analyze the Output for Exploitation Opportunities

**Context**: Review the query results to identify interesting users, such as those with elevated privileges (e.g., db_owner) or unusual authentication types. Cross-reference with server-level principals if needed for broader discovery.

**Instructions**: Pipe the command output to a file for analysis (e.g., add > users.txt to the sqlcmd command) or use grep/awk to filter by type_desc='SQL_USER'. Look for users with sid indicating domain accounts, which could enable lateral movement.

> If no users appear beyond 'dbo', the database may have minimal custom users—proceed to server-level enumeration. Verify success by checking for multiple rows excluding roles.

**Expected Output**: Filtered list of users, e.g., via manual inspection or scripted parsing, highlighting potential targets like service accounts.
