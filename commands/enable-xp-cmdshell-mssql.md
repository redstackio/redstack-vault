---
id: 96c9aff1-5760-47bb-adf6-0814ae1aa7e7
name: enable-xp-cmdshell-mssql
type: command
executor: sql
data: >-
  EXEC sp_configure 'show advanced options',1; RECONFIGURE; EXEC sp_configure
  'xp_cmdshell',1; RECONFIGURE;
output: null
created_at: '2023-04-06T03:56:33.953275+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - SQL Server
tags:
  - mssql
  - enable-procedure
verified: true
validated: true
---

# enable-xp-cmdshell-mssql

## Command

```sql
EXEC sp_configure 'show advanced options',1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell',1;
RECONFIGURE;
```

## Description

This SQL command sequence enables the xp_cmdshell extended stored procedure in Microsoft SQL Server, which is disabled by default for security. It first exposes advanced options, then activates xp_cmdshell, applying changes immediately. Use this in scenarios requiring OS command execution from SQL, such as post-exploitation on a compromised database server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a fixed configuration command with no user parameters. | N/A |

## Examples

### Basic Usage

```sql
EXEC sp_configure 'show advanced options',1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell',1; RECONFIGURE;
```

Run in SSMS or sqlcmd connected to the target instance with sysadmin privileges.

### Verification

After execution, verify with:
```sql
SELECT name, value FROM sys.configurations WHERE name = 'xp_cmdshell';
```
Expected: value = 1.

## Expected Output

Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install.
RECONFIGURE
Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install.
RECONFIGURE

No errors if successful; otherwise, indicates insufficient privileges.

## Related

- [[procedures/Command-Execution-via-xp-cmdshell-MSSQL-Server]]
- [[commands/execute-command-via-xp-cmdshell-mssql]]
