---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote-Services|T1021 - Remote Services]]'
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Linked Database]]'
  - '[[tags/MSSQL Server]]'
  - '[[tags/Database Discovery]]'
commands:
  - '[[commands/get-sqlquery-top-5-rows-linked-server]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Extract-Top-5-Columns-from-Linked-Database

## Summary

This procedure extracts the top 5 columns from a selected table in a linked database using MSSQL Server's linked server functionality. It executes a SQL query via PowerShell to retrieve the first 5 rows, which reveals column names and sample data, aiding in database structure reconnaissance for further attacks or data exfiltration.

## Description

In scenarios where an attacker has access to an MSSQL Server instance with configured linked servers, this procedure allows querying remote databases to discover schema details without direct access. By using the OPENQUERY function, the procedure fetches the top 5 rows from a target table in the linked database, parsing the output to identify key columns such as IDs, names, or sensitive fields. This is particularly useful in lateral movement phases to map interconnected databases in enterprise environments. The approach assumes the linked server is already set up and the attacker has query permissions on the target table. Expected outcomes include a list of column names and sample values, providing insights into data types and potential high-value targets.

## Requirements

1. Administrative or query access to an MSSQL Server instance with a configured linked server.
2. PowerShell execution privileges on the target system, including the necessary SQL module (e.g., SqlServer or dbatools) for Get-SQLQuery.
3. Knowledge of the linked server name, remote database name, and target table name from prior reconnaissance.
4. Network connectivity between the MSSQL instance and the linked remote database.

## Defense

- Restrict linked server configurations to only essential, trusted remote endpoints and require explicit permissions for OPENQUERY usage.
- Monitor SQL Server logs for anomalous queries involving OPENQUERY or TOP clauses on linked servers, using tools like SQL Server Audit or Extended Events.
- Implement least-privilege access controls on database roles to limit SELECT permissions on sensitive tables.
- Segment database networks to prevent lateral queries between instances.

## Objectives

1. Retrieve column names and sample data from a remote table via a linked server.
2. Identify database structure for targeted data collection or further exploitation.
3. Validate linked server access for lateral movement opportunities.

## Instructions

### Step 1: Identify Linked Server and Target Details

**Context**: Before executing the query, confirm the linked server name, remote database, and table from prior enumeration (e.g., via sp_linkedservers or database documentation). This ensures the placeholders are correctly substituted to avoid errors.

Gather the following:
- Linked server name (e.g., LINKED_DB_SERVER)
- Remote database name (e.g., RemoteDB)
- Target table name (e.g., Users)

### Step 2: Execute Query to Retrieve Top 5 Rows

**Context**: Use the Get-SQLQuery command to run a SQL query that leverages OPENQUERY to fetch the top 5 rows from the remote table. This returns column headers and data, allowing extraction of the top columns by inspecting the output structure.

**Command** ([[commands/get-sqlquery-top-5-rows-linked-server]]):
```powershell
Get-SQLQuery -Instance "DBSERVERNAME\DBInstance" -Query "select * from openquery(\"$DatabaseLinkName\",'select TOP 5 * from $DatabaseNameFromPreviousCommand.dbo.$TableNameFromPreviousCommand')" -Verbose
```

> This command connects to the specified MSSQL instance and executes the query. The OPENQUERY function passes the TOP 5 SELECT directly to the linked server, bypassing some local processing. Substitute placeholders: DBSERVERNAME\DBInstance with your local SQL server (e.g., SQL01\SQLEXPRESS), $DatabaseLinkName with the linked server name, $DatabaseNameFromPreviousCommand with the remote DB name, and $TableNameFromPreviousCommand with the table name. The -Verbose flag provides detailed execution logs. Expected output includes a table with 5 rows, where the first row headers reveal column names like ID, Username, Email, etc.

### Step 3: Parse Output for Column Extraction

**Context**: Review the command output to manually or scripturally extract column names. In PowerShell, pipe the results to Format-Table or Export-Csv for clarity.

For example, after running the command:
```powershell
$result = Get-SQLQuery ... | Format-Table -AutoSize
$result | Out-String
```

> Inspect the column headers in the output. Success is indicated by receiving 5 rows of data without errors like 'Login failed' or 'Invalid object name'. If fewer rows return, the table may have limited data; adjust TOP clause if needed.
