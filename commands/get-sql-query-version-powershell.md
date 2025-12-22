---
type: command
executor: powershell
data: Get-Query "SELECT @@VERSION"
output: null
platforms:
  - Windows
tags:
  - mssql
  - query
  - version
verified: true
validated: true
---

# get-sql-query-version-powershell

## Command

```powershell
Get-Query "SELECT @@VERSION"
```

## Description

This PowerShell cmdlet executes a custom SQL query against a specified or piped SQL instance. Here, it runs 'SELECT @@VERSION' to retrieve the server's version, edition, and build information. Ideal for post-enumeration discovery in MSSQL environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| QueryString | The SQL query to execute (e.g., "SELECT @@VERSION") | Yes |
| -Instance | Target instance name (if not piped) | No |

## Examples

### Basic Usage

```powershell
Get-Query "SELECT @@VERSION"
```

### With Specific Instance

```powershell
Get-Query -Instance 'SERVER\INSTANCE' "SELECT @@VERSION"
```

## Expected Output

Query results as a DataTable or object:

@@VERSION
-----------------
Microsoft SQL Server 2019 (RTM) - 15.0.2000.5 (X64)   
	Mar 26 2022 10:22:50   
	Copyright (C) 2019 Microsoft Corporation
	Developer Edition (64-bit) on Windows 10 Pro 10.0 <X64> (Build 19042: )

## Related

- [[procedures/Query-MSSQL-Server-Version]]
- [[commands/get-sqlinstance-domain-powershell]]
