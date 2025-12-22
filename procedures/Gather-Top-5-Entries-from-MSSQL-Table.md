---
type: procedure
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - mssql
  - database-discovery
  - sensitive-information
commands:
  - '[[commands/get-sqlquery-retrieve-top-5-rows-from-table]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Gather-Top-5-Entries-from-MSSQL-Table

## Summary

This procedure enables an attacker with access to an MSSQL database to extract the top 5 entries from a specific table, potentially revealing sensitive information such as user data, credentials, or configuration details that can aid in further reconnaissance or targeting.

## Description

In a compromised environment, attackers often query databases to discover valuable assets. This procedure uses PowerShell's Get-SQLQuery cmdlet (from modules like PowerSQL or dbatools) to execute a simple SELECT TOP 5 query against a targeted table in an MSSQL instance. It assumes the attacker has valid credentials for database access. The technique focuses on quick data enumeration without alerting defenders, mapping to MITRE ATT&CK's Discovery tactic where system information is gathered from repositories like databases. Success depends on the table containing relevant data, such as employee records or API keys, which can inform subsequent attacks like credential dumping or lateral movement.

## Requirements

1. Valid credentials with SELECT permissions on the target database and table.
2. PowerShell environment with SQL Server module installed (e.g., dbatools or sqlps).
3. Network access to the MSSQL server instance.
4. Knowledge of the database name, table name, and server instance details.

## Defense

- Implement principle of least privilege: Limit database accounts to read-only where possible and revoke unnecessary SELECT permissions.
- Enable SQL Server auditing and logging for query monitoring; use tools like SQL Server Audit or Extended Events to detect anomalous SELECT statements.
- Deploy database activity monitoring (DAM) solutions to alert on queries targeting sensitive tables.
- Use encryption for sensitive data at rest and enforce row-level security (RLS) to restrict data visibility.

## Objectives

1. Retrieve the top 5 rows from a specified MSSQL table to identify sensitive information.
2. Assess the table's contents for potential targets or vulnerabilities without full data exfiltration.
3. Validate database access and query capabilities for further exploitation.

## Instructions

### Step 1: Prepare the Query Parameters

**Context**: Identify the MSSQL instance, database, and table to target. Replace placeholders with actual values to construct the SQL query. This ensures the command targets the correct location and limits output to avoid excessive data transfer.

Ensure the PowerShell module for SQL interactions (e.g., Import-Module dbatools) is loaded.

### Step 2: Execute the Query to Retrieve Top 5 Rows

**Context**: Run the Get-SQLQuery command to fetch the top 5 entries. This step performs the core data gathering, using TOP 5 to quickly sample the table without triggering size-based alerts.

**Command** ([[commands/get-sqlquery-retrieve-top-5-rows-from-table]]):
```powershell
Get-SQLQuery -Instance "$_INSTANCE" -Query 'SELECT TOP 5 * FROM $_DATABASE.dbo.$_TABLENAME'
```

> This command connects to the specified MSSQL instance and executes the SQL query. The -Instance parameter points to the server (e.g., 'SERVERNAME\SQLEXPRESS'), and the -Query parameter uses SELECT TOP 5 * to retrieve all columns from the first 5 rows of the table. Expected output is a table-like result set displaying the rows; if the table is empty or access is denied, an error will occur. Review the output for sensitive fields like usernames, emails, or hashes.

### Step 3: Verify and Analyze Output

**Context**: Inspect the returned data for actionable intelligence. This step confirms success and documents findings for use in attack chains.

Save the output to a file if needed: `| Export-Csv -Path output.csv -NoTypeInformation`. Check for patterns or values that indicate high-value data, such as unencrypted passwords or API tokens.
