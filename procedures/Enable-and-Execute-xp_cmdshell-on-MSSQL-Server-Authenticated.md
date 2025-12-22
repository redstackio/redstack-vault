---
type: procedure
description: >-
  Enables the xp_cmdshell extended stored procedure on a Microsoft SQL Server
  and uses it to execute operating system commands as the MSSQL service account.
tactics:
  - '[[Execution]]'
techniques:
  - '[[Windows Command Shell]]'
sub_techniques: []
tags:
  - mssql
  - xp_cmdshell
  - rce
  - execution
commands:
  - '[[commands/mssql-enable-xp_cmdshell]]'
  - '[[commands/xp_cmdshell-execute-shell-command]]'
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Enable-and-Execute-xp_cmdshell-on-MSSQL-Server-Authenticated

## Summary

This procedure enables the xp_cmdshell extended stored procedure on a Microsoft SQL Server instance, which allows execution of operating system commands via the SQL interface, and then demonstrates how to run shell commands as the MSSQL service account. It is useful for post-exploitation scenarios where authenticated access to the database is obtained, enabling lateral movement or command execution on the underlying Windows host.

## Description

xp_cmdshell is a built-in extended stored procedure in Microsoft SQL Server that executes a given command string using cmd.exe on the server. By default, it is disabled in modern SQL Server versions for security reasons, but it can be re-enabled using the sp_configure system procedure if the user has sysadmin privileges (e.g., the 'sa' account). Once enabled, attackers can leverage xp_cmdshell to run arbitrary OS commands, such as whoami, net user, or even download and execute payloads, running in the context of the MSSQL service account (often a low-privileged service account like NT SERVICE\MSSQLSERVER). This technique is commonly used in database compromise scenarios to achieve remote code execution (RCE) on the host. Prerequisites include valid credentials with sysadmin role and network access to the SQL Server port (default 1433). The procedure assumes use of a SQL client like sqlcmd, Impacket's mssqlclient.py, or Azure Data Studio.

## Requirements

1. Authenticated access to the MSSQL instance with sysadmin privileges (e.g., 'sa' account or equivalent).
2. Network connectivity to the SQL Server on TCP port 1433 (or custom port).
3. A SQL client tool such as sqlcmd (Windows), mssqlclient.py from Impacket (Python), or sqlplus.
4. The target must be running Microsoft SQL Server on Windows (xp_cmdshell is not available on Linux-hosted SQL Server).

## Defense

- Disable xp_cmdshell by default using sp_configure 'xp_cmdshell', 0; RECONFIGURE; and monitor for re-enablement attempts via SQL Server audit logs or Extended Events.
- Restrict sysadmin role to least-privilege principles; use Windows Authentication with domain accounts that have limited OS permissions.
- Enable SQL Server logging for stored procedure executions and failed logins; integrate with SIEM for alerts on sp_configure or xp_cmdshell usage.
- Run SQL Server under a non-privileged service account and apply AppLocker or WDAC to restrict cmd.exe execution from the SQL context.
- Regularly audit configuration changes with tools like SQL Server Configuration Manager or PowerShell scripts.

## Objectives

1. Enable the xp_cmdshell feature to allow OS command execution from SQL queries.
2. Execute arbitrary shell commands via xp_cmdshell to perform reconnaissance or post-exploitation actions on the host.
3. Verify successful command execution and gather output for further analysis or pivoting.

## Instructions

### Step 1: Enable xp_cmdshell

**Context**: xp_cmdshell must first be enabled if it is disabled (default state). This involves showing advanced configuration options, setting xp_cmdshell to 1, and reconfiguring the server. This step requires sysadmin privileges and will persist across restarts unless manually disabled.

**Command** ([[commands/mssql-enable-xp_cmdshell]]):
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

> This command sequence enables advanced options, then specifically activates xp_cmdshell. Note that some clients like Impacket's mssqlclient.py may not require 'GO' or 'EXEC'; adjust syntax per tool documentation. If already enabled, the configuration change messages will indicate no update was needed.

### Step 2: Execute a Shell Command via xp_cmdshell

**Context**: With xp_cmdshell enabled, use it to run OS commands in the context of the MSSQL service account. This allows reconnaissance (e.g., whoami) or more advanced actions like spawning a reverse shell. Output is returned as a result set; NULL rows may appear for empty lines.

**Command** ([[commands/xp_cmdshell-execute-shell-command]]):
```sql
EXEC xp_cmdshell '$_CMD';
GO
```

> Replace $_CMD with the desired command, e.g., 'whoami' for identity confirmation or 'dir C:\' for file listing. The command runs via cmd.exe, so complex commands may require escaping. Success is indicated by the command output in the result set; errors will show in SQL messages.
