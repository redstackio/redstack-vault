---
type: command
executor: powershell
data: Get-SQLInstanceDomain
output: null
platforms:
  - Windows
tags:
  - mssql
  - discovery
verified: true
validated: true
---

# get-sqlinstance-domain-powershell

## Command

```powershell
Get-SQLInstanceDomain
```

## Description

This PowerShell cmdlet enumerates all SQL Server instances running in the current domain by querying network resources or Active Directory. Use it during discovery phases to identify targets for further interrogation like version checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; uses current domain context | No |

## Examples

### Basic Usage

```powershell
Get-SQLInstanceDomain
```

### Piped Usage

```powershell
Get-SQLInstanceDomain | Where-Object { $_.InstanceName -eq 'MSSQLSERVER' }
```

## Expected Output

A table listing instances:

ServerName    InstanceName  IsClustered  Version
-----------    ------------  -----------  -------
DC01           MSSQLSERVER   False        15.0.2000.5
SQLSRV02       REPORTING     False        14.0.1000.169

## Related

- [[procedures/Query-MSSQL-Server-Version]]
- [[commands/get-sql-query-version-powershell]]
