---
id: a2fbbd65-ee84-4009-869b-a3e409a58863
name: Domain-SQL-Server-Discovery-Script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:19.794705+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - discovery
  - sql-server
  - powershell
validated: true
---

# Domain-SQL-Server-Discovery-Script

## Code

```powershell
Get-SQLInstanceDomain -Verbose
# Get Server Info for Found Instances
Get-SQLInstanceDomain | Get-SQLServerInfo -Verbose
# Get Database Names
Get-SQLInstanceDomain | Get-SQLDatabase -NoDefaults
```

## Description

This PowerShell script performs comprehensive discovery of SQL Server instances in a Windows domain. It first enumerates instances, then retrieves server details, and finally lists user databases. It relies on the SqlServer module and is useful for reconnaissance in AD environments to map database assets.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The script uses current domain context; no user-defined variables | N/A |

## Usage

Execute this script on a domain-joined Windows machine after importing the SqlServer module (Import-Module SqlServer). Run in an elevated PowerShell session with domain credentials. Output can be redirected to files for analysis, e.g., `./script.ps1 > discovery.txt`. Integrate into larger attack chains for lateral movement targeting databases.

## Detection

- Monitor PowerShell execution logs for SqlServer module imports and commands like Get-SQLInstanceDomain.
- Network traffic to UDP 1434 (SQL Browser) or TCP 1433 from non-SQL clients.
- Event logs for AD queries related to SQL SPNs or service enumerations.

## Related

- [[procedures/Domain-SQL-Server-Discovery]]
- [[tools/Powershell]]
