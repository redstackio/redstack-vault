---
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:20Z'
updated_at: '2023-04-10T20:36:31Z'
platforms:
  - Windows
tags:
  - mssql
  - powershell
  - discovery
validated: true
---

# mssql-linked-server-crawler-script

## Code

```ps1
Get-SQLServerLinkCrawl -Instance "<DBSERVERNAME\DBInstance>" -Verbose
select * from openquery("<instance>", 'select * from openquery("<instance2>", ''select * from master..sysservers'')')
```

## Description

This PowerShell script snippet initiates a linked server crawl using Get-SQLServerLinkCrawl and follows up with a SQL OPENQUERY to probe remote linked servers for further sysservers details. It is used to map MSSQL database interconnections for discovery and lateral movement.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <DBSERVERNAME\DBInstance> | Target SQL Server instance path | sqlserver01\default |
| <instance> | Linked server name for first OPENQUERY | LINKEDSQL02 |
| <instance2> | Target remote instance for nested query | sqlserver03 |

## Usage

Load this script in a PowerShell session with SQL modules imported. Run the first line to crawl the initial instance, then use the output to populate the SQL query variables for deeper probing. Integrate into procedures for automated MSSQL discovery during red team engagements.

## Detection

- PowerShell execution logs showing Get-SQLServerLinkCrawl or OPENQUERY to sysservers.
- SQL audit trails for queries against master..sysservers from unexpected users.
- Network traffic to MSSQL ports (1433) with patterns indicating recursive queries.

## Related

- [[procedures/MSSQL-Linked-Database-Crawler]]
- [[procedures/MSSQL-Linked-Database-Crawler]]
