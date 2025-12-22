---
id: 5365c9f4-3d81-4f67-8a82-67c9493fdcc5
name: PowerShell-Enumerate-Linked-SQL-Servers
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:20.068881+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sql-enumeration
  - discovery
  - powershell
validated: true
---

# PowerShell-Enumerate-Linked-SQL-Servers

## Code

```ps1
Get-SQLInstanceDomain | Get-SQLServerLink -Verbose
select * from master..sysservers
```

## Description

This PowerShell code snippet combines domain SQL instance discovery with linked server enumeration and a direct SQL query to sysservers. It is designed for use in red team operations to crawl linked databases and map MSSQL infrastructure in an AD domain, identifying potential lateral movement targets.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The code uses built-in cmdlets; no user variables required, but ensure SQL modules are loaded | N/A |

## Usage

Load this in a PowerShell session with SQL Server modules (e.g., Import-Module SQLPS). Run against an accessible SQL instance to output linked servers. Pipe results to Export-Csv for logging, or integrate into a larger script for automated crawling: foreach link, connect and re-run the query.

## Detection

- PowerShell execution logs showing Get-SQLInstanceDomain or Get-SQLServerLink cmdlets.
- SQL audit logs for queries to master..sysservers from unexpected accounts.
- Anomalous connections between SQL instances indicating link traversal.

## Related

- [[procedures/Enumerate-Linked-MSSQL-Servers-via-Database-Crawling]]
