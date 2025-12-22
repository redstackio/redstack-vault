---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - database-discovery
  - mssql
  - sql-query
  - reconnaissance
commands:
  - '[[commands/sql-select-db-name]]'
platforms:
  - SQL Server
tools: []
validated: true
---

# Retrieve-Current-Database-Name-in-SQL-Server

## Summary

This procedure retrieves the name of the current database in a Microsoft SQL Server instance using a built-in SQL function. It is a fundamental reconnaissance step after gaining access to a database server, helping attackers map the environment, identify active databases, and plan subsequent actions like data enumeration or privilege escalation.

## Description

Once an attacker has obtained access to a SQL Server instance—through valid credentials, SQL injection, or lateral movement—they often need to quickly understand the database context to avoid errors in further operations. The DB_NAME() function returns the name of the database currently in use by the session, such as 'master', 'tempdb', or a user-created database. This information is crucial for targeted queries, schema exploration, or confirming the scope of access. The procedure assumes interactive access via a SQL client and focuses on manual execution for reliability in restricted environments.

## Requirements

1. Valid authentication credentials or session access to the SQL Server instance (e.g., via SQL login or Windows authentication).
2. A SQL execution interface, such as sqlcmd, Azure Data Studio, SQL Server Management Studio (SSMS), or a programmatic client like Impacket's mssqlclient.py.
3. Network connectivity to the SQL Server port (default TCP 1433).
4. Sufficient permissions to execute SELECT statements (typically granted to most database users).

## Defense

Defensive measures and detection strategies:

- Enforce least privilege access: Limit database users to only necessary databases and revoke public schema access where possible.
- Enable SQL Server Audit or Extended Events to log all SELECT queries, particularly those involving system functions like DB_NAME().
- Implement query filtering at the application layer or use database firewalls (e.g., SQL Firewall) to block suspicious reconnaissance queries.
- Monitor for anomalous login patterns or query volumes from unexpected sources using tools like Microsoft Defender for SQL or SIEM integration.

## Objectives

1. Identify the current database context to guide further database-specific enumeration.
2. Confirm successful access to the SQL Server instance without triggering errors from incorrect database assumptions.
3. Gather environmental intelligence for chaining into more advanced discovery techniques, such as listing all databases or tables.

## Instructions

### Step 1: Connect to the SQL Server Instance

**Context**: Establish a connection to the target SQL Server to ensure query execution capability. This step verifies access before running the discovery query.

If using sqlcmd (command-line tool), connect with:

```bash
sqlcmd -S target_server -U username -P password
```

> Successful connection is indicated by the '1>' prompt. If using a GUI like SSMS, open a new query window after logging in. Failure here (e.g., login denied) means prerequisites are unmet—escalate privileges or obtain credentials first.

### Step 2: Execute the Current Database Name Query

**Context**: Run the SQL query to retrieve the database name. This provides immediate feedback on the session's database context, which is essential for subsequent operations like querying user tables or system views.

**Command** ([[commands/sql-select-db-name]]):

```sql
select db_name()
```

> The DB_NAME() function queries the current session's database without requiring additional parameters. It targets the sys.databases system view implicitly. Expected output is a single-column result set with the database name (e.g., 'AdventureWorks'). If the output is 'master', it indicates default access—consider switching databases with 'USE [dbname]' if needed. Verify by re-running the query after any USE statement to confirm context change.
