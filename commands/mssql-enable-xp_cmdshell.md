---
type: command
executor: sql
data: |-
  EXEC sp_configure 'show advanced options', 1;
  GO
  RECONFIGURE;
  GO
  EXEC sp_configure 'xp_cmdshell', 1;
  GO
  RECONFIGURE;
  GO
tags:
  - mssql
  - configuration
platforms:
  - Windows
verified: true
validated: true
---

# mssql-enable-xp_cmdshell

## Command

```sql
EXEC sp_configure 'show advanced options', 1;
GO
RECONFIGURE;
GO
EXEC sp_configure 'xp_cmdshell', 1;
GO
RECONFIGURE;
GO
```

## Description

This SQL command sequence enables the xp_cmdshell extended stored procedure on a Microsoft SQL Server instance by first activating advanced configuration options and then setting the xp_cmdshell option to 1, followed by reconfiguration to apply changes. It is used when authenticated with sysadmin privileges to allow subsequent OS command execution via SQL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a fixed configuration command with no user parameters. | N/A |

## Examples

### Basic Usage

```sql
EXEC sp_configure 'show advanced options', 1;
GO
RECONFIGURE;
GO
EXEC sp_configure 'xp_cmdshell', 1;
GO
RECONFIGURE;
GO
```

### Usage in Impacket mssqlclient.py

In tools like Impacket, 'GO' may be omitted:

```sql
sp_configure 'show advanced options', 1
RECONFIGURE
sp_configure 'xp_cmdshell', 1
RECONFIGURE
```

## Expected Output

```
1> EXEC sp_configure 'show advanced options', 1
2> GO
Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install.
(return status = 0)
1> RECONFIGURE
2> GO
DBCC execution completed. If DBCC printed error messages, contact your system administrator.
1> EXEC sp_configure 'xp_cmdshell', 1
2> GO
Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install.
(return status = 0)
1> RECONFIGURE
2> GO
DBCC execution completed. If DBCC printed error messages, contact your system administrator.
```

If already enabled, messages will indicate no change (e.g., 'changed from 1 to 1').

## Related

- [[procedures/Enable-and-Execute-xp_cmdshell-on-MSSQL-Server-Authenticated]]
