---
id: 51ce57c7-1fae-4d5c-8a7d-0bccc1290910
name: Query-SQL-Server-Current-User-and-Sysadmin-Status
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.722023+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - manual-sql-queries
  - mssql-server
  - query-current-user-sysadmin
commands:
  - '[[commands/sql-server-get-current-user-and-role]]'
platforms:
  - Windows
  - SQL Server
tools: []
validated: true
---

# Query-SQL-Server-Current-User-and-Sysadmin-Status

## Summary

This procedure retrieves information about the current SQL Server user, including the login name and whether the user has sysadmin privileges. It is useful in penetration testing or red team engagements to assess the level of access granted to a compromised database account, enabling attackers to determine potential escalation paths or data access capabilities.

## Description

In a security assessment of Microsoft SQL Server environments, understanding the current user's identity and privileges is a foundational discovery step. This procedure executes SQL queries to fetch the SQL Server login name via SUSER_SNAME(), the Windows or domain login via SYSTEM_USER, and checks sysadmin membership using IS_SRVROLEMEMBER('sysadmin'). These queries require basic SELECT permissions and are typically run after initial access to the database instance, such as through a compromised application or direct connection. Success provides critical intelligence for planning further actions like privilege escalation if sysadmin access is confirmed, or lateral movement if limited privileges are identified. The target environment is a SQL Server instance (e.g., on Windows servers), and outcomes help map the attack surface within the database.

## Requirements

1. Valid connection to the SQL Server instance (e.g., via sqlcmd, SSMS, or integrated application access).
2. SELECT permissions on system views or sufficient user context to execute the queries.
3. Tools like sqlcmd or a SQL client for query execution.

## Defense

- Restrict database access to least privilege principles, avoiding broad SELECT grants on system catalogs.
- Enable SQL Server auditing for query execution on sensitive system functions like SUSER_SNAME and IS_SRVROLEMEMBER.
- Monitor for anomalous queries from non-administrative accounts and implement query whitelisting where possible.

## Objectives

1. Identify the current SQL Server login and associated Windows user.
2. Determine if the current user holds sysadmin role membership for privilege assessment.
3. Gather intelligence to inform subsequent discovery or escalation steps.

## Instructions

### Step 1: Connect to SQL Server Instance

**Context**: Establish a connection to the target SQL Server using a client tool to execute queries. This assumes initial access via credentials or exploited vulnerability.

Use a SQL client like sqlcmd to connect:

```bash
sqlcmd -S target_server -U username -P password
```

> This opens an interactive session. If connected successfully, proceed to query execution. Expected output: A prompt like '1>' indicating readiness for SQL input.

### Step 2: Execute Queries for User Information

**Context**: Run the SQL statements to retrieve user details and sysadmin status. This step accomplishes the core discovery by querying system functions.

**Command** ([[commands/sql-server-get-current-user-and-role]]):

```sql
select suser_sname();
select system_user;
select is_srvrolemember('sysadmin');
```

> The first query returns the SQL Server login name (e.g., 'domain\user'). The second returns the operating system login (e.g., 'DOMAIN\User'). The third returns 1 if sysadmin (full privileges) or 0 otherwise. Execute each in sequence within the SQL session. If sysadmin is 1, the account has elevated access for further exploitation.
