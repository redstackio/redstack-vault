---
type: procedure
description: >-
  Extracts entries from a selected column in a linked SQL Server database to
  gather sensitive information like credentials.
verified: true
submitted: false
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation-of-Remote-Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Remote-Services|T1021 - Remote Services]]'
sub_techniques:
  - >-
    [[sub-techniques/SMB/Windows-Admin-Shares|T1021.002 - SMB/Windows Admin
    Shares]]
tags:
  - '[[tags/Gather Entries from a Selected Linked Column]]'
  - '[[tags/Linked Database]]'
  - '[[tags/MSSQL Server]]'
commands: []
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Extract-Data-from-Linked-SQL-Server-Database

## Summary

This procedure demonstrates how to extract sensitive data, such as usernames and passwords, from a specific column in a linked SQL Server database using OPENQUERY to bypass network segmentation and access remote data stores.

## Description

Linked Database Column Extraction involves querying a linked server configuration in Microsoft SQL Server to retrieve entries from a targeted column in a remote database. This technique is useful in scenarios where an attacker has gained initial access to a SQL Server instance and seeks to discover or exfiltrate credential information or other sensitive data stored in linked databases. By leveraging the OPENQUERY function, the attacker can execute pass-through queries to the remote server, potentially evading direct network access restrictions. This method maps to lateral movement and discovery tactics, allowing escalation through obtained credentials. It requires administrative or query execution privileges on the local SQL instance and assumes a pre-configured linked server pointing to the target remote database.

## Requirements

1. Access to a SQL Server instance with a configured linked server to the target remote database.
2. PowerShell execution privileges on the host running the SQL Server or a machine with SQL Server management tools.
3. Knowledge of the remote database name, table name, column name, and a specific column value from prior enumeration (e.g., from a previous discovery step).
4. Installation of the SQL Server PowerShell module (e.g., SqlServer or DBATools) to support the Get-SQLQuery cmdlet.

## Defense

- Implement least-privilege access controls on SQL Server instances, restricting query execution on linked servers to authorized users only.
- Use database firewalls and network segmentation to isolate SQL Servers, disabling unnecessary linked server configurations.
- Enable SQL Server auditing for query execution, linked server usage, and anomalous data access patterns; monitor logs for OPENQUERY invocations targeting sensitive columns.
- Regularly review and remove unused linked servers, and apply principle of least privilege to linked server credentials.

## Objectives

1. Retrieve sensitive entries (e.g., credentials) from a specified column in a linked remote database.
2. Facilitate unauthorized data access across segmented networks via SQL linked servers.
3. Enable privilege escalation by using extracted data for further system compromise.

## Instructions

### Step 1: Verify Linked Server Configuration

**Context**: Confirm the existence and accessibility of the linked server to ensure the query can be executed without errors. This step prevents failures due to misconfiguration.

Use SQL Server Management Studio (SSMS) or a similar tool to query the sys.servers system view.

**Command**:
```sql
SELECT * FROM sys.servers WHERE name = '<DatabaseLinkName>';
```

> This lists details of the linked server, including provider and data source. If the linked server is not listed or disabled, configuration is required beforehand.

**Expected Output**: A row showing the linked server name, status as '0' (enabled), and connection details.

### Step 2: Prepare Query Parameters from Prior Enumeration

**Context**: Gather the necessary database, table, column, and value details from previous discovery steps (e.g., enumerating databases or tables via [[techniques/SQL-Query-Discovery]]). This ensures the query targets the correct sensitive data.

Manually note or script the retrieval of these values, such as identifying a column like 'username' in a 'credentials' table where a known value matches a filter.

**Expected Output**: Variables set with: DatabaseName (e.g., 'TargetDB'), TableName (e.g., 'Users'), ColumnName (e.g., 'Username'), ColumnValue (e.g., 'admin').

### Step 3: Execute Query on Linked Server Using PowerShell

**Context**: Use the prepared parameters to construct and run an OPENQUERY against the linked server, extracting all rows where the specified column matches the value. This step accomplishes the data extraction.

**Code** ([[codes/PowerShell-Query-Linked-SQL-Server]]):

```ps1
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "select * from openquery(`"<DatabaseLinkName>`"'select * from <DatabaseNameFromPreviousCommand>.dbo.<TableNameFromPreviousCommand> where <ColumnNameFromPreviousCommand>=<ColumnValueFromPreviousCommand>')" -Verbose
```

> This PowerShell invocation uses the Get-SQLQuery cmdlet to execute the pass-through query via OPENQUERY. The linked server handles the remote execution, returning results as a table. Replace placeholders with actual values from Step 2. The -Verbose flag provides detailed output for troubleshooting.

**Expected Output**: A DataTable object containing rows from the remote table matching the filter, e.g., columns like Username, PasswordHash displayed in console or exported to CSV.

**Success Indicators**:
- No authentication or connection errors in verbose output.
- Returned dataset includes sensitive column entries (e.g., credential pairs).
