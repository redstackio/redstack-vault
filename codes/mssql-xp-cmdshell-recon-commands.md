---
id: d0cc6887-ec49-449e-af9e-6ffd5e9a0906
name: mssql-xp-cmdshell-recon-commands
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:20.266570+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - SQL Server
tags:
  - recon
  - mssql
  - xp-cmdshell
validated: true
---

# mssql-xp-cmdshell-recon-commands

## Code

```sql
EXEC xp_cmdshell "net user";
EXEC master..xp_cmdshell 'whoami'
EXEC master.dbo.xp_cmdshell 'cmd.exe dir c:';
EXEC master.dbo.xp_cmdshell 'ping 127.0.0.1';
```

## Description

This SQL code snippet executes a series of reconnaissance commands via xp_cmdshell to gather initial system information on a Windows host running SQL Server. It enumerates local users, identifies the current execution context, lists the C: drive contents, and tests local network connectivity. Use this after enabling xp_cmdshell to quickly assess the environment and confirm shell access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This code uses fixed, hardcoded commands with no substitutable variables. | N/A |

## Usage

Execute the entire batch in SSMS or sqlcmd against a compromised SQL instance with xp_cmdshell enabled. It provides a quick recon payload without needing custom scripting. Integrate into procedures for post-exploitation enumeration, such as identifying users for lateral movement or directories for persistence.

## Detection

- SQL audit logs showing xp_cmdshell executions with suspicious commands like 'net user' or 'whoami'.
- Windows Security event logs (ID 4688) for cmd.exe processes spawned by sqlservr.exe.
- Network monitoring for anomalous pings or connections from the SQL host.
- SIEM rules for configuration changes enabling xp_cmdshell followed by command executions.

## Related

- [[procedures/Command-Execution-via-xp-cmdshell-MSSQL-Server]]
- [[execute-command-via-xp-cmdshell-mssql]]
