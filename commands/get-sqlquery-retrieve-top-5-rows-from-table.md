---
type: command
executor: powershell
data: >-
  Get-SQLQuery -Instance "$_INSTANCE" -Query 'SELECT TOP 5 * FROM
  $_DATABASE.dbo.$_TABLENAME'
tags:
  - mssql
  - query
  - discovery
platforms:
  - Windows
verified: true
validated: true
---

# get-sqlquery-retrieve-top-5-rows-from-table

## Command

```powershell
Get-SQLQuery -Instance "$_INSTANCE" -Query 'SELECT TOP 5 * FROM $_DATABASE.dbo.$_TABLENAME'
```

## Description

This command uses the Get-SQLQuery cmdlet (typically from dbatools or sqlps PowerShell modules) to execute a SQL query that retrieves the top 5 rows from a specified table in an MSSQL database. It is useful for quick reconnaissance of table contents during database enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Instance `$_INSTANCE` | The SQL Server instance name (e.g., 'SERVERNAME\\INSTANCE') | Yes |
| -Query | The SQL query string to execute | Yes |
| $_DATABASE | Database name in the query (e.g., 'MyDB') | Yes (in query) |
| $_TABLENAME | Table name in the query (e.g., 'Users') | Yes (in query) |

## Examples

### Basic Usage

```powershell
Get-SQLQuery -Instance "localhost\SQLEXPRESS" -Query 'SELECT TOP 5 * FROM AdventureWorks.dbo.Employees'
```

### Advanced Usage

```powershell
Get-SQLQuery -Instance "remote-server\MSSQL2019" -Query 'SELECT TOP 5 * FROM SecurityDB.dbo.Credentials' | Format-Table
```

## Expected Output

A tabular result set showing the top 5 rows:

```

ID    Name       Email                PasswordHash
--    ----       -----                ------------
1     John Doe   john@example.com     5f4dcc3b5aa765d61d8327deb882cf99
2     Jane Smith jane@example.com     e10adc3949ba59abbe56e057f20f883e
3     Bob User   bob@example.com      ...
4     Alice Key  alice@example.com    ...
5     Eve Pass   eve@example.com      ...

```

If successful, displays row data; errors indicate permission issues or invalid targets.

## Related

- [[procedures/Gather-Top-5-Entries-from-MSSQL-Table]]
