---
id: 84b41754-3336-4a32-b056-0f460a246a34
name: list-clr-stored-procedures
type: command
executor: powershell
data: Get-SQLStoredProcedureCLR -Instance <instance> -Verbose
output: null
created_at: '2023-04-06T03:56:20.364587+00:00'
updated_at: '2023-04-10T20:36:39.601743+00:00'
platforms:
  - Windows
tags:
  - clr
  - mssql
  - discovery
verified: true
validated: true
---

# list-clr-stored-procedures

## Command

```powershell
Get-SQLStoredProcedureCLR -Instance <instance> -Verbose
```

## Description

This command queries the MSSQL instance to list all stored procedures implemented via CLR assemblies, helping identify loaded malicious or custom procedures for verification or cleanup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Instance | Target SQL Server instance (e.g., localhost) | Yes |
| -Verbose | Enable detailed query output | No |

## Examples

### Basic Usage

```powershell
Get-SQLStoredProcedureCLR -Instance localhost -Verbose
```

### Advanced Usage

```powershell
Get-SQLStoredProcedureCLR -Instance "SERVER\INSTANCE" -Verbose
```

## Expected Output

Returns a table of CLR procedures:

```
Name: runcmd
Assembly: runcmd
CreateDate: 2023-04-06
IsCLR: True
...
```

Empty list if no CLR procedures exist; verbose shows the underlying SQL query (SELECT * FROM sys.procedures WHERE is_ms_shipped = 0 AND type = 'P' AND ...).

## Related

- [[procedures/mssql-clr-assembly-command-execution]]
- [[commands/create-clr-dll-and-sql-files]]
