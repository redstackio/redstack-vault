---
type: code
language: ps1
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - mssql
  - enumeration
  - discovery
  - linked-server
validated: true
---

# PowerShell-Query-Linked-Databases-via-OpenQuery

## Code

```ps1
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "select * from openquery('<DatabaseLinkName>','select name from sys.databases')" -Verbose
```

## Description

This PowerShell code snippet uses the Get-SQLQuery cmdlet (from the SqlServer module) to execute a distributed query against a linked server in MSSQL. It leverages OPENQUERY to remotely select database names from sys.databases on the linked instance, enabling enumeration of remote databases without direct access. Useful in reconnaissance to map database topologies during red team engagements.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <DBSERVERNAME\DBInstance> | The target MSSQL server instance name in 'server\instance' format | "sqlserver01\SQLEXPRESS" |
| <DatabaseLinkName> | The name of the configured linked server in the current database | "LINKED_REMOTE_DB" |

## Usage

Execute this code in a PowerShell session after importing the SqlServer module. It requires authenticated access to the initial MSSQL instance with linked server permissions. Typically used in post-compromise scenarios to discover interconnected databases; output can be piped to files for further analysis (e.g., `$result | Export-Csv -Path databases.csv`). Integrate into procedures like database enumeration for lateral movement planning.

## Detection

- Monitor PowerShell logs for SqlServer module imports and Get-SQLQuery executions.
- Audit MSSQL error logs for OPENQUERY attempts, especially from non-admin users.
- Network traffic analysis for unusual TCP/1433 connections between database servers.
- SIEM alerts on queries accessing sys.databases via linked servers.

## Related

- [[procedures/Enumerate-Linked-Databases-in-MSSQL]]
