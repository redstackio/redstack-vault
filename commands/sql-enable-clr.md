---
type: command
executor: sql
data: 'sp_configure ''clr enabled'', 1 RECONFIGURE GO'
output: null
created_at: '2023-04-06T03:56:20.431310+00:00'
updated_at: '2023-04-10T20:36:42.151890+00:00'
platforms:
  - SQL Server
tags:
  - configuration
  - clr
verified: true
validated: true
---

# sql-enable-clr

## Command

```sql
sp_configure 'clr enabled', 1;
RECONFIGURE;
GO
```

## Description

Activates Common Language Runtime (CLR) integration in SQL Server, allowing .NET assemblies to be loaded and executed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'clr enabled' | The configuration option name | Yes |
| 1 | Value to enable (1 = on, 0 = off) | Yes |

## Examples

### Basic Usage

```sql
sp_configure 'clr enabled', 1;
RECONFIGURE;
GO
```

### Disable

```sql
sp_configure 'clr enabled', 0;
RECONFIGURE;
GO
```

## Expected Output

Configuration option 'clr enabled' changed from 0 to 1. Run the RECONFIGURE statement to install.

## Related

- [[procedures/Creating-and-Importing-CLR-Assembly-for-OS-Command-Execution-in-MSSQL]]
