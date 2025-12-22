---
id: f6e83705-b8ba-4f4c-a4dd-5b9aa58ba685
name: Enumerate-Tables-in-Linked-MSSQL-Database
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.171055+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/System Owner/User Discovery|T1033 - System Owner/User
    Discovery]]
  - >-
    [[techniques/Data from Information Repositories|T1213 - Data from
    Information Repositories]]
sub_techniques: []
tags:
  - linked-database
  - mssql-server
  - table-enumeration
  - database-discovery
commands:
  - '[[commands/get-sqlquery-execute-openquery]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enumerate-Tables-in-Linked-MSSQL-Database

## Summary

This procedure allows an attacker with access to a Microsoft SQL Server (MSSQL) instance to enumerate all table names from a linked remote database server. By executing a targeted SQL query through the linked server configuration, the attacker can identify database structures for further reconnaissance, data collection, or lateral movement without direct access to the remote database.

## Description

In scenarios where an attacker has compromised an MSSQL server with configured linked servers (allowing queries to remote databases), this procedure leverages the OPENQUERY function to execute a SELECT statement on the remote database's system tables. Specifically, it queries the sys.tables view to retrieve table names. This technique is useful during post-exploitation phases to map out interconnected database environments, discover sensitive data locations, or prepare for data exfiltration. The procedure assumes the attacker has sufficient permissions on the source MSSQL instance to query linked servers and that the linked server is properly configured with credentials or impersonation. It maps to MITRE ATT&CK under Discovery for understanding the environment and Collection for gathering database schema information, enabling targeted follow-on actions like querying specific tables for credentials or user data.

## Requirements

1. Valid credentials or access to an MSSQL Server instance with linked server configuration pointing to the target remote database.
2. PowerShell environment with the SqlServer module installed (or equivalent SQL execution capabilities).
3. Knowledge of the linked server name, remote database name, and source MSSQL instance details.
4. Network connectivity between the source and linked servers (typically over port 1433 for MSSQL).

## Defense

- Restrict linked server configurations to only necessary remote endpoints and use least-privilege credentials for linked server logins.
- Monitor SQL Server logs and audit trails for anomalous OPENQUERY executions or queries against sys.tables on linked servers.
- Implement database activity monitoring (DAM) tools to detect unusual schema enumeration patterns.
- Enforce network segmentation to limit lateral querying between database instances and disable unnecessary linked servers.

## Objectives

1. Retrieve a complete list of table names from the target linked database to map its structure.
2. Identify potential high-value tables (e.g., those containing user data, credentials, or configuration) for subsequent exploitation.
3. Validate linked server access and permissions without alerting defenders through direct remote connections.

## Instructions

### Step 1: Prepare Linked Server Query

**Context**: Identify the source MSSQL instance, linked server name, and target database name. Ensure the linked server is configured and accessible. This step sets up the variables needed for the query, confirming prerequisites before execution.

Replace placeholders with actual values: `<DBSERVERNAME\DBInstance>` for the source server (e.g., `server01\SQLEXPRESS`), `<DatabaseLinkName>` for the linked server (e.g., `RemoteDBLink`), and `<DatabaseNameFromPreviousCommand>` for the remote database (e.g., `ProductionDB`). Verify linked server status using a simple test query if needed.

**Expected Output**: No output at this stage; confirmation that placeholders are correctly substituted.

### Step 2: Execute Query to Enumerate Tables

**Context**: Use the Get-SQLQuery command to run the OPENQUERY against the linked server. This retrieves table names from sys.tables, providing a schema overview. The -Verbose flag provides execution details for troubleshooting.

**Command** ([[commands/get-sqlquery-execute-openquery]]):

```powershell
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "select * from openquery('<DatabaseLinkName>','select name from <DatabaseNameFromPreviousCommand>.sys.tables')" -Verbose
```

> This command connects to the specified MSSQL instance and executes the nested query via OPENQUERY, which passes the inner SELECT directly to the linked server. The outer SELECT * captures all results. Success is indicated by a returned table with column 'name' listing table names. If the linked server requires specific authentication, ensure the query context uses the appropriate login. Handle errors like 'linked server not found' by verifying server configuration.

**Expected Output**: A table or result set displaying table names, such as:

| name          |
|---------------|
| Users         |
| Credentials   |
| AuditLogs     |

If no tables are returned, check permissions or linked server setup.

### Step 3: Analyze and Validate Results

**Context**: Review the output to identify relevant tables. Cross-reference with known database schemas or use the results to inform next steps, such as querying specific tables.

Export results to a file for further analysis if needed: `results | Export-Csv -Path table_list.csv -NoTypeInformation`. Look for tables like 'sysusers', 'employees', or custom ones indicating sensitive data.

**Expected Output**: Processed list of table names, potentially filtered or annotated for relevance.

**Success Indicators**:
- Query executes without authentication or connectivity errors.
- At least one table name is returned, confirming linked server access.
- No alerts triggered in SQL logs during execution.
