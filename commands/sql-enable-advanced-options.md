---
type: command
executor: sql
data: 'sp_configure ''show advanced options'', 1; RECONFIGURE GO'
output: null
created_at: '2023-04-06T03:56:20.431194+00:00'
updated_at: '2023-04-10T20:36:42.151890+00:00'
platforms:
  - SQL Server
tags:
  - configuration
  - clr
verified: true
validated: true
---

# sql-enable-advanced-options

## Command

```sql
sp_configure 'show advanced options', 1;
RECONFIGURE;
GO
```

## Description

Enables the display of advanced server configuration options in SQL Server, necessary to access and modify CLR settings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'show advanced options' | The configuration option name | Yes |
| 1 | Value to enable (1 = on, 0 = off) | Yes |

## Examples

### Basic Usage

```sql
sp_configure 'show advanced options', 1;
RECONFIGURE;
GO
```

### Disable

```sql
sp_configure 'show advanced options', 0;
RECONFIGURE;
GO
```

## Expected Output

Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install.

## Related

- [[procedures/Creating-and-Importing-CLR-Assembly-for-OS-Command-Execution-in-MSSQL]]
