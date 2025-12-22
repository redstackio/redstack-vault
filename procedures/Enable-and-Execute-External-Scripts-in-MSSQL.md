---
type: procedure
description: >-
  Enables external script execution in Microsoft SQL Server to run non-T-SQL
  scripts like Python or R, allowing potential command execution on the host
  system.
verified: true
submitted: false
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Python|T1059.006 - Python]]'
tags:
  - '[[tags/External Scripts]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/mssql-enable-external-scripts]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enable-and-Execute-External-Scripts-in-MSSQL

## Summary

This procedure enables the execution of external scripts (such as Python or R) within Microsoft SQL Server, allowing integration of advanced scripting capabilities directly from T-SQL queries. In an attack context, this can be abused to execute arbitrary code on the SQL Server host, potentially leading to system compromise if the attacker has sufficient privileges.

## Description

Microsoft SQL Server supports external script execution through the 'external scripts enabled' feature, introduced in SQL Server 2016 and later. When enabled, administrators or users with sysadmin privileges can run scripts in languages like Python or R using the sp_execute_external_script stored procedure. This feature spawns external processes (e.g., Python.exe) from the SQL Server service account context, which can execute operating system commands if the scripts are crafted maliciously. The target environment is a Windows-based SQL Server instance with Machine Learning Services installed. Prerequisites include authenticated access with sysadmin rights. Expected outcomes include successful enabling of the feature and execution of a sample script to verify functionality, demonstrating potential for code execution outside the SQL engine.

## Requirements

1. Authenticated access to the SQL Server instance with sysadmin privileges.
2. SQL Server 2016 or later with Machine Learning Services (R/Python) feature installed.
3. SQL Server Management Studio (SSMS) or a similar client like sqlcmd for executing T-SQL.
4. Network access to the SQL Server port (default 1433).

## Defense

- Disable external scripts using sp_configure 'external scripts enabled', 0; RECONFIGURE if not required for legitimate data analysis.
- Restrict sysadmin privileges to trusted users only and implement least privilege principles.
- Monitor SQL Server error logs and Windows Event Logs for external process spawns (e.g., Python.exe from sqlservr.exe parent).
- Enable SQL Server auditing for sp_configure and sp_execute_external_script usage.

## Objectives

1. Enable external script execution capability in SQL Server.
2. Verify the feature by executing a sample external script.
3. Demonstrate potential for host system command execution via scripted languages.

## Instructions

### Step 1: Connect to SQL Server Instance

**Context**: Establish a connection to the target SQL Server using a privileged account to prepare for configuration changes. This step ensures you have the necessary sysadmin role to modify server settings.

Use SSMS or sqlcmd to connect. Verify your privileges by running:

```sql
SELECT IS_SRVROLEMEMBER('sysadmin');
```

> If the result is 1, you have sysadmin rights. Expected output: A result set showing 1 for sysadmin membership.

### Step 2: Enable External Scripts

**Context**: Configure SQL Server to allow execution of external scripts. This modifies the advanced server option 'external scripts enabled' to 1, enabling the launch of external runtimes like Python from T-SQL.

**Command** ([[commands/mssql-enable-external-scripts]]):

```sql
sp_configure 'external scripts enabled', 1;
RECONFIGURE;
```

> This command updates the configuration and applies it immediately. Run it in a query window. Expected output: Messages indicating "Configuration option 'external scripts enabled' changed from 0 to 1. Run the RECONFIGURE statement to install." and "RECONFIGURE Statement: Configuration option 'external scripts enabled' has been changed. The new value will take effect after the RECONFIGURE statement completes."

### Step 3: Restart SQL Server Service (If Required)

**Context**: Some configurations require a service restart to fully apply changes, though RECONFIGURE often suffices. This ensures the external script runtime is active.

If the feature does not activate post-RECONFIGURE, restart the SQL Server service via SSMS (right-click instance > Restart) or Windows Services (services.msc, find "SQL Server (MSSQLSERVER)").

Expected output: Service restarts without errors, confirmed by checking server status in SSMS.

### Step 4: Execute a Sample External Script

**Context**: Test the enabled feature by running a simple Python script to confirm external execution works. This step verifies the ability to run code in an external language, which could be extended to malicious payloads like subprocess calls for OS commands.

Run the following T-SQL to execute a Python script that outputs the current date:

```sql
EXEC sp_execute_external_script
    @language = N'Python',
    @script = N'
    import datetime
    print(datetime.datetime.now())
    ';
```

> This invokes Python to print the current timestamp. Expected output: A result set with the Python print output, e.g., "2023-10-01 12:00:00.123456". If successful, the feature is enabled and external processes can be spawned.

**Success Indicators**:
- No errors on sp_configure execution.
- Sample Python script runs and returns output.
- SQL Server error log shows no failures in external runtime launch.
