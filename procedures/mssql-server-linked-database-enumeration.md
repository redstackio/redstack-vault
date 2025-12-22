---
id: e6cfec99-f094-4ed4-a7bb-32f6bcf0395b
name: mssql-server-linked-database-enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.014835+00:00'
updated_at: '2023-04-10T20:36:39.276730+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
  - '[[techniques/Query Registry|T1012 - Query Registry]]'
sub_techniques: []
tags:
  - '[[tags/Find Trusted Link]]'
  - '[[tags/Linked Database]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/mssql-select-from-sysservers]]'
platforms:
  - Windows
  - SQL Server
tools: []
validated: true
---

# mssql-server-linked-database-enumeration

## Summary

This procedure enumerates linked servers in a Microsoft SQL Server instance by querying the system table sysservers. It allows attackers with database access to discover trusted connections to remote servers, enabling pivoting to other systems and potential access to sensitive data across the network.

## Description

In a Microsoft SQL Server environment, linked servers allow one SQL instance to connect to another remote database server, often with trusted authentication. Attackers can exploit this to expand their reach beyond the initial compromised instance. This procedure targets the master database's sysservers table, which stores configuration details for all linked servers, including names, providers, and connection strings. By extracting this information, an attacker identifies pivot points for lateral movement, such as querying remote databases for credentials or data exfiltration. The target environment is typically a Windows-based SQL Server (versions 2008+), requiring valid login credentials with SELECT permissions on system views. Success reveals linked server details, which can lead to further exploitation like executing queries on remote instances.

## Requirements

1. Valid credentials or session access to the target MSSQL Server instance (e.g., via SQL authentication or Windows integrated).
2. SELECT permissions on system tables/views in the master database.
3. A SQL client tool like sqlcmd, PowerShell with SqlServer module, or Impacket's mssqlclient for query execution.
4. Network connectivity to the SQL Server port (default TCP 1433).

## Defense

Defensive measures and detection strategies:

- Implement network segmentation to isolate SQL Servers and limit lateral connections between instances.
- Enforce least privilege access: Revoke unnecessary SELECT permissions on system tables for non-admin users.
- Enable SQL Server auditing for queries against sysservers and linked server activities; monitor logs for anomalous SELECT statements.
- Use database firewalls or proxies to restrict outbound connections from SQL instances.
- Regularly review and remove unused linked servers via sp_dropserver.

## Objectives

1. Identify all linked servers configured in the target MSSQL instance.
2. Extract configuration details to assess trust relationships and potential pivot targets.
3. Enable further network discovery or data access via discovered links.

## Instructions

### Step 1: Establish Connection to MSSQL Instance

**Context**: Before querying system tables, connect to the target SQL Server using a SQL client. This ensures you have an active session with sufficient permissions. Use tools like sqlcmd for command-line access or integrate with existing sessions in tools like Metasploit's mssql modules.

**Command** (N/A - connection setup):

Assume connection via sqlcmd:

```bash
sqlcmd -S target_server -U username -P password
```

> This step verifies access. If connected successfully, you should see the sqlcmd prompt (1>).

### Step 2: Query Linked Servers from Sysservers

**Context**: Execute a query against the master database's sysservers table to retrieve all linked server configurations. This reveals server names, data sources, providers, and security contexts, helping identify trusted links for pivoting.

**Command** ([[commands/mssql-select-from-sysservers]]):

```sql
select * from master..sysservers
```

> The SELECT * retrieves all columns from sysservers, including srvid (server ID), name (linked server name), network_name (connection string), status (login type, e.g., trusted), and isremote (remote login enabled). Run this in your SQL session. If permissions are insufficient, you'll get an error; otherwise, it lists all entries.

### Step 3: Analyze and Validate Output

**Context**: Review the query results to identify actionable linked servers. Look for entries with status indicating trusted logins (e.g., 48 for RPC enabled) or remote data sources pointing to internal network segments. Test connectivity to a discovered linked server using a follow-up query like EXEC sp_testlinkedserver 'servername' to confirm viability without full exploitation.

**Command** (N/A - analysis):

In SQL session:

```sql
EXEC sp_testlinkedserver 'linked_server_name';
```

> Expected: Confirmation of successful connection or error details. Document server names and statuses for use in subsequent procedures like remote query execution.
