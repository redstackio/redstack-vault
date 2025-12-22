---
id: 2f7cad72-2762-4191-9c98-b70c3c058757
name: Enumerate-MSSQL-Databases
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.823541+00:00'
updated_at: '2023-04-10T20:36:33.171505+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/List all databases]]'
  - '[[tags/Manual SQL Server Queries]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/mssql-select-database-names]]'
platforms:
  - MSSQL
tools: []
validated: true
---

# Enumerate-MSSQL-Databases

## Summary

The Enumerate-MSSQL-Databases procedure discovers all available databases on a Microsoft SQL Server instance by executing a targeted SQL query against the system catalog. This technique allows attackers to map the database landscape, identifying potential targets for data extraction, such as user databases containing sensitive information like customer records or financial data, while system databases like master and tempdb provide insight into the server's configuration.

## Description

In an attack scenario, this procedure is typically used during the discovery phase after gaining initial access to the MSSQL server via valid credentials, SQL injection, or a compromised host with network connectivity. The query targets the sysdatabases view in the master database, which lists all database names without requiring elevated privileges beyond basic SELECT access. This is a low-risk, high-value reconnaissance step that informs subsequent actions like database-specific enumeration or exploitation. The procedure assumes connectivity via a SQL client such as sqlcmd, Azure Data Studio, or integrated tools like Impacket's mssqlclient.py. Expected outcomes include a complete list of databases, enabling prioritization of high-value targets. Detection can be mitigated by running queries during off-hours or blending with legitimate administrative traffic.

## Requirements

1. Valid credentials (username/password) or exploited access to the MSSQL server instance.
2. Network connectivity to the MSSQL port (default TCP 1433) from the attacker's machine or compromised host.
3. A SQL client tool capable of executing ad-hoc queries, such as sqlcmd, PowerShell with SqlServer module, or Python with pyodbc.
4. Basic SELECT permissions on the master database (often granted to public roles).

## Defense

Defensive measures and detection strategies:

- Apply principle of least privilege: Restrict SELECT access to sysdatabases for non-administrative accounts and use database roles to limit visibility.
- Enable SQL Server Audit to log all queries against system views, alerting on anomalous SELECT statements from master..sysdatabases.
- Implement network segmentation and firewall rules to restrict inbound connections to MSSQL ports from untrusted sources.
- Monitor for unusual query patterns using tools like SQL Server Extended Events or third-party SIEM integration to detect reconnaissance queries.

## Objectives

1. Retrieve a complete list of database names on the target MSSQL instance.
2. Identify user-created databases for potential sensitive data targeting.
3. Validate successful query execution without triggering immediate alerts.
4. Gather intelligence for follow-on enumeration or exploitation activities.

## Instructions

### Step 1: Connect to the MSSQL Instance

**Context**: Establish a connection to the target MSSQL server using your chosen SQL client. This step ensures you have the necessary access before executing discovery queries. Use trusted credentials or an exploited session to authenticate.

**Command** (Connect via sqlcmd example):
```bash
sqlcmd -S $_SERVER -U $_USERNAME -P $_PASSWORD
```

> This connects to the server specified by $_SERVER (e.g., hostname or IP:port). Once connected, you can proceed to query execution. Expected output: A successful connection prompt (1>).

### Step 2: Execute Database Enumeration Query

**Context**: Run the SQL query to list all databases. This targets the system catalog to retrieve names without needing db_owner privileges. The query is lightweight and unlikely to log as suspicious if administrative access is mimicked.

**Command** ([[commands/mssql-select-database-names]]):
```sql
select name from master..sysdatabases;
```

> This query selects the 'name' column from the sysdatabases compatibility view in the master database. It returns a result set with database names. If the instance has many databases, results may paginate; use 'GO' to execute. Decision point: If access is denied, escalate privileges or pivot to another access vector; otherwise, proceed to analyze the output for targets like 'AdventureWorks' or custom user DBs.

### Step 3: Verify and Document Results

**Context**: Review the output to confirm success and note any databases of interest. This step includes exporting results for further analysis if needed.

**Command** (Optional export in sqlcmd):
```sql
select name from master..sysdatabases; GO
```

> After execution, the results will display inline. To save: Use 'OUTPUT TO file.txt' in some clients or redirect sqlcmd output (e.g., sqlcmd ... > dbs.txt). Expected output: A table-like list of database names. Success criteria: No errors like 'Login failed' or 'Permission denied'; presence of expected system DBs (master, model, msdb, tempdb).
