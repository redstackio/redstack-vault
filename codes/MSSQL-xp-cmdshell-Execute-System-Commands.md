---
id: c23e24c7-e7ae-4cd5-9c3d-f97250afd5b4
type: code
name: MSSQL-xp-cmdshell-Execute-System-Commands
language: sql
verified: true
created_at: '2023-04-06T03:56:33.953119+00:00'
updated_at: '2023-04-10T20:22:46.088423+00:00'
platforms:
  - Windows
tags:
  - mssql
  - xp-cmdshell
  - execution
validated: true
---

# MSSQL-xp-cmdshell-Execute-System-Commands

## Code

```sql
EXEC xp_cmdshell "net user";
EXEC master.dbo.xp_cmdshell 'cmd.exe dir c:';
EXEC master.dbo.xp_cmdshell 'ping 127.0.0.1';
```

## Description

SQL code snippets demonstrating execution of basic Windows system commands via the xp_cmdshell stored procedure. These can be used for reconnaissance, such as listing users, directories, or testing connectivity, after enabling xp_cmdshell.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Command string | OS command to execute (e.g., "net user") | 'whoami' |

## Usage

Execute each statement in an MSSQL shell after connecting and enabling xp_cmdshell. Useful in SQL injection payloads or direct admin access for initial foothold establishment.

## Detection

- SQL audit logs showing xp_cmdshell invocations.
- Windows process creation events (4688) for spawned commands like net.exe, cmd.exe.
- Network logs for ping traffic from SQL Server host.

## Related

- [[procedures/MSSQL-Command-Execution-via-xp-cmdshell]]
