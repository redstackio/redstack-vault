---
type: code
language: ps1
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - sql-query
  - linked-server
  - data-extraction
validated: true
---

# PowerShell-Query-Linked-SQL-Server

## Code

```ps1
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "select * from openquery(`"<DatabaseLinkName>`"'select * from <DatabaseNameFromPreviousCommand>.dbo.<TableNameFromPreviousCommand> where <ColumnNameFromPreviousCommand>=<ColumnValueFromPreviousCommand>')" -Verbose
```

## Description

This PowerShell code snippet executes a pass-through SQL query using OPENQUERY on a linked server to extract data from a specific table column in a remote database. It is designed for scenarios where direct access to the remote database is restricted, allowing lateral data access via an existing SQL Server linked server configuration. The query filters results based on a column value, targeting sensitive information like credentials.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <DBSERVERNAME\DBInstance> | The SQL Server instance name (server\instance) hosting the linked server | 'sqlserver01\SQLEXPRESS' |
| <DatabaseLinkName> | The name of the configured linked server | 'RemoteDBLink' |
| <DatabaseNameFromPreviousCommand> | Name of the remote database to query | 'TargetDatabase' |
| <TableNameFromPreviousCommand> | Name of the table containing the target column | 'CredentialsTable' |
| <ColumnNameFromPreviousCommand> | Name of the column to filter and extract from | 'Username' |
| <ColumnValueFromPreviousCommand> | Specific value to match in the column for filtering | 'admin' |

## Usage

Substitute the placeholders with values obtained from prior enumeration steps (e.g., database discovery). Run this in a PowerShell session with the SqlServer module loaded. It is typically used within a procedure like [[procedures/Extract-Data-from-Linked-SQL-Server-Database]] after gaining query access to the local SQL instance. Export results to a file for further analysis: pipe to Export-Csv.

## Detection

- Monitor SQL Server error logs and audit traces for OPENQUERY executions referencing linked servers.
- PowerShell script block logging will capture the Get-SQLQuery invocation and query string.
- Network traffic analysis for unusual SQL connections from the linked server IP.
- Anomalous data volume queries or access to sensitive tables via extended events.
