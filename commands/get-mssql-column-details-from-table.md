---
id: 184a1136-3a70-4140-80de-3588f2ab1cb2
name: get-mssql-column-details-from-table
type: command
executor: powershell
data: >-
  Get-SQLInstanceDomain | Get-SQLColumn -DatabaseName <DatabaseName> -TableName
  <TableName>
output: null
created_at: '2023-04-06T03:56:19.912303+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - database-discovery
  - sensitive-data
verified: true
validated: true
---

# get-mssql-column-details-from-table

## Command

```powershell
Get-SQLInstanceDomain | Get-SQLColumn -DatabaseName <DatabaseName> -TableName <TableName>
```

## Description

This PowerShell command from the dbatools module enumerates detailed column information for a specific table in an MSSQL database, including data types and properties, to identify potential sensitive data storage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<DatabaseName>` | The name of the target database | Yes |
| `<TableName>` | The name of the target table (e.g., 'Users') | Yes |

## Examples

### Basic Usage

```powershell
Get-SQLInstanceDomain | Get-SQLColumn -DatabaseName 'AdventureWorks' -TableName 'Users'
```

### Advanced Usage

```powershell
Get-SQLInstanceDomain | Get-SQLColumn -DatabaseName 'ProductionDB' -TableName 'Credentials' | Select-Object Name, DataType, MaxLength, IsNullable
```

## Expected Output

```
Name         DataType Length IsNullable
----         -------- ------ ----------
ID           int      4      False
Username     varchar  50     True
PasswordHash varchar  255    False
Email        varchar  100    True
```

This sample shows column names, types, lengths, and nullability. Use this to spot sensitive columns like password fields.

## Related

- [[procedures/mssql-identify-sensitive-information-get-tables-and-column-details]]
- [[commands/get-mssql-tables-from-database]]
