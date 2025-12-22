---
id: 65c2a704-d6d9-4c6c-bee9-5efa0f32faa8
name: get-mssql-tables-from-database
type: command
executor: powershell
data: Get-SQLInstanceDomain | Get-SQLTable -DatabaseName <DatabaseName> -NoDefaults
output: null
created_at: '2023-04-06T03:56:19.912246+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - database-discovery
verified: true
validated: true
---

# get-mssql-tables-from-database

## Command

```powershell
Get-SQLInstanceDomain | Get-SQLTable -DatabaseName <DatabaseName> -NoDefaults
```

## Description

This PowerShell command uses the dbatools module to discover SQL Server instances in the domain and retrieve a list of user tables from a specified database, excluding default system tables. It is used during database reconnaissance to map schema structures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<DatabaseName>` | The name of the target database (e.g., 'MyDB') | Yes |
| `-NoDefaults` | Excludes default/system tables, focusing on custom ones | No |

## Examples

### Basic Usage

```powershell
Get-SQLInstanceDomain | Get-SQLTable -DatabaseName 'AdventureWorks' -NoDefaults
```

### Advanced Usage

```powershell
$instance = Get-SQLInstanceDomain -Server 'sqlserver.domain.com'; $instance | Get-SQLTable -DatabaseName 'ProductionDB'
```

## Expected Output

```
SchemaName TableName  TableType
----------- --------- ----------
 dbo        Users     Base Table
 dbo        Orders    Base Table
 dbo        Products  Base Table
```

This output shows schema, table names, and types for successful enumeration. Errors may occur if credentials lack permissions or the database does not exist.

## Related

- [[procedures/mssql-identify-sensitive-information-get-tables-and-column-details]]
- [[commands/get-mssql-column-details-from-table]]
