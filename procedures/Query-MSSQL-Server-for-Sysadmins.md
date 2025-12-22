---
id: 9e9a34a5-3c43-4986-803f-f8c4122a2291
name: Query-MSSQL-Server-for-Sysadmins
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.904812+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/List All Sysadmins]]'
  - '[[tags/Manual SQL Server Queries]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/Retrieve-Server-Principals-with-Sysadmin-Role]]'
platforms:
  - Windows
tools: []
validated: true
---

# Query-MSSQL-Server-for-Sysadmins

## Summary

This procedure queries a Microsoft SQL Server (MSSQL) instance to identify all server principals with sysadmin privileges, revealing high-value accounts that could be targeted for credential theft or privilege escalation in a network compromise scenario.

## Description

In a penetration test or red team engagement, discovering privileged accounts on a database server like MSSQL is crucial for mapping the attack surface. The sysadmin role grants full control over the SQL Server instance, including the ability to execute commands, access data, and potentially pivot to other systems. This procedure uses a direct SQL query against the sys.server_principals system view to enumerate these principals, filtering for membership in the sysadmin server role. It is applicable in environments where an attacker has obtained valid credentials or executed initial access to the database, such as via SQL injection or compromised service accounts. The output provides names, types (e.g., SQL login, Windows user), and disabled status, enabling prioritization of active privileged accounts for further exploitation.

## Requirements

1. Valid credentials (username and password) for an MSSQL account with sufficient permissions to query system views (at least VIEW DEFINITION or higher).
2. Network access to the MSSQL Server instance (default port 1433/TCP).
3. A SQL client tool like sqlcmd, Azure Data Studio, or SQL Server Management Studio (SSMS) to execute queries.
4. The target must be running Microsoft SQL Server (versions 2005+ support this query syntax).

## Defense

- Limit sysadmin role membership to the minimum necessary accounts and regularly audit role assignments using tools like SQL Server Audit or extended events.
- Implement least privilege principles by using Windows Authentication and group-based roles instead of direct SQL logins.
- Enable logging of failed and successful logins, query executions on system views, and alert on anomalous database activity (e.g., via SQL Server Audit or SIEM integration).
- Use database firewalls or network segmentation to restrict access to MSSQL instances.

## Objectives

1. Enumerate all server principals with sysadmin privileges on the MSSQL instance.
2. Identify active, high-value targets for subsequent attacks like password cracking or lateral movement.
3. Validate the query results to confirm no false positives in role membership.

## Instructions

### Step 1: Connect to the MSSQL Instance

**Context**: Establish a connection to the target MSSQL Server using a SQL client to ensure access and prepare for query execution. This step verifies prerequisites and sets the session context.

Use a tool like sqlcmd to connect:

```bash
sqlcmd -S target_server -U username -P password
```

> This command initiates an interactive session. If using SSMS, open a new query window and connect via the UI. Expected output: A prompt like '1>' indicating successful connection. If connection fails, check credentials, firewall rules, and server availability.

### Step 2: Execute the Sysadmin Enumeration Query

**Context**: Run the SQL query to retrieve the list of sysadmin principals. This leverages the IS_SRVROLEMEMBER function to check role membership dynamically.

**Command** ([[commands/Retrieve-Server-Principals-with-Sysadmin-Role]]):

```sql
SELECT name, type_desc, is_disabled FROM sys.server_principals WHERE IS_SRVROLEMEMBER('sysadmin', name) = 1;
```

**Code** ([[codes/SQL-Query-List-Sysadmin-Principals]]):

```sql
SELECT name,type_desc,is_disabled FROM sys.server_principals WHERE IS_SRVROLEMEMBER ('sysadmin',name) = 1
```

> The query targets the sys.server_principals view, which catalogs server-level logins and roles. IS_SRVROLEMEMBER returns 1 for members of the sysadmin fixed server role. Columns include name (principal identifier), type_desc (e.g., 'SQL_LOGIN', 'WINDOWS_LOGIN'), and is_disabled (0 for enabled, 1 for disabled). Execute in the connected session (e.g., paste into sqlcmd and end with GO). Expected output: A result set listing principals, such as:

| name          | type_desc    | is_disabled |
|---------------|--------------|-------------|
| sa            | SQL_LOGIN    | 0           |
| DOMAIN\Admin | WINDOWS_LOGIN | 0           |

If no results, the current user may lack permissions or no sysadmins exist (unlikely).

### Step 3: Interpret and Export Results

**Context**: Analyze the output for actionable intelligence and save for reporting or further use, such as targeting specific accounts.

In sqlcmd, redirect output to a file:

```bash
:output sysadmins.txt
GO
:output
```

> Review for enabled principals (is_disabled = 0) and note Windows vs. SQL logins for escalation paths. Cross-reference with domain knowledge if available. Success is confirmed by a non-empty result set with relevant privileged accounts. If results include unexpected entries, it may indicate over-privileged configurations.
