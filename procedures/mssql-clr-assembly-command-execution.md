---
id: 5b02de2e-482e-4d6c-85fe-10bade78a9b2
name: mssql-clr-assembly-command-execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.373807+00:00'
updated_at: '2023-04-10T20:36:39.590991+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - '[[tags/CLR Assemblies]]'
  - '[[tags/Execute commands using CLR assembly]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/create-clr-dll-and-sql-files]]'
  - '[[commands/invoke-clr-command-execution-whoami]]'
  - '[[commands/invoke-clr-command-execution-powershell]]'
  - '[[commands/list-clr-stored-procedures]]'
platforms:
  - Windows
tools: []
validated: true
---

# mssql-clr-assembly-command-execution

## Summary

This procedure enables execution of arbitrary commands on a Microsoft SQL Server (MSSQL) instance by creating and loading a custom Common Language Runtime (CLR) assembly. The assembly contains C# code that invokes system commands, allowing attackers with sufficient permissions to bypass restrictions and achieve remote code execution, such as spawning a reverse shell or running diagnostic commands like whoami.

## Description

MSSQL CLR Assembly Command Execution leverages the CLR integration feature in SQL Server to load unsafe assemblies that execute operating system commands. This technique is particularly effective in environments where direct command execution is restricted but CLR loading is permitted. An attacker first generates a C# DLL using a PowerShell helper script, converts it to a hexadecimal string for SQL injection or direct execution, and then loads it via SQL commands like CREATE ASSEMBLY. Once loaded, a stored procedure from the assembly can be invoked to run commands. This requires the 'sysadmin' role or equivalent permissions to enable CLR and load assemblies. It is commonly chained with SQL injection for initial access but can also be used post-compromise for persistence or escalation. The target environment is typically Windows servers running MSSQL 2005 or later with CLR enabled (sp_configure 'clr enabled', 1).

## Requirements

1. Valid credentials for an MSSQL account with sysadmin privileges or permissions to create assemblies (e.g., CREATE ASSEMBLY permission).
2. Network access to the MSSQL instance (default port 1433/TCP).
3. PowerShell execution environment on the attacker's machine to generate the CLR files.
4. CLR integration enabled on the target SQL Server (checked via sp_configure).

## Defense

- Disable CLR integration if not required: EXEC sp_configure 'clr enabled', 0; RECONFIGURE;
- Restrict CREATE ASSEMBLY permissions to trusted users only.
- Monitor SQL Server logs for assembly loading events (Event ID 33205 in SQL Audit) and unusual stored procedure creations.
- Implement database firewalls to block unauthorized SQL traffic and use parameterized queries to prevent injection-based delivery.

## Objectives

1. Load a custom CLR assembly into the MSSQL instance to enable command execution.
2. Execute arbitrary OS commands on the underlying Windows server hosting MSSQL.
3. Establish persistence or escalate privileges by running scripts like PowerShell payloads.

## Instructions

### Step 1: Generate CLR Assembly Files

**Context**: Create the C# source code for the CLR assembly, compile it into a DLL, and generate a SQL script with the DLL as a hexadecimal string for loading into MSSQL. This step prepares the payload for deployment and explains the purpose of each generated file: the .cs file defines the stored procedure, the .dll is the compiled assembly, and the .sql handles the CREATE ASSEMBLY and CREATE PROCEDURE statements.

**Command** ([[commands/create-clr-dll-and-sql-files]]):
```powershell
Create-SQLFileCLRDll -ProcedureName "runcmd" -OutFile runcmd -OutDir C:\Users\user\Desktop
```

> This PowerShell cmdlet from the SQLServer module or a custom script generates three files: runcmd.cs (C# code with a stored procedure that executes commands via System.Diagnostics.Process), runcmd.dll (compiled assembly), and runcmd.sql (SQL to load the assembly). Placeholders like procedure name allow customization. Success is verified by the presence of these files in the output directory.

### Step 2: Load the Assembly and Execute a Simple Command

**Context**: Connect to the MSSQL instance and use the generated SQL script to load the CLR assembly, create the stored procedure, and invoke it to run a basic command like whoami. This tests execution and confirms the assembly loads without errors, providing initial foothold verification.

**Command** ([[commands/invoke-clr-command-execution-whoami]]):
```powershell
Invoke-SQLOSCmdCLR -Username sa -Password <password> -Instance <instance> -Command "whoami" -Verbose
```

> The cmdlet automates the SQL execution: it runs the .sql file to CREATE ASSEMBLY from the hex DLL, CREATE PROCEDURE, and EXEC runcmd @cmd = 'whoami'. Replace <password> and <instance> with actual values. Verbose mode shows SQL queries and results. If successful, it returns the output of whoami (e.g., nt authority\system).

### Step 3: Execute Advanced Payloads

**Context**: Use the loaded CLR procedure to run more complex commands, such as a base64-encoded PowerShell payload for reverse shells or further exploitation. This step builds on the assembly for persistence or data exfiltration, with decision points: if basic execution works, proceed; otherwise, check SQL error logs for permission issues.

**Command** ([[commands/invoke-clr-command-execution-powershell]]):
```powershell
Invoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell -e <base64>" -Verbose
```

> Invoke the stored procedure with a PowerShell one-liner encoded in base64 (e.g., for a reverse shell). The cmdlet handles the EXEC call. If the instance is named, use the full format. Expected output includes the PowerShell execution result or connection confirmation. Clean up post-use with DROP PROCEDURE and DROP ASSEMBLY to avoid detection.

### Step 4: Verify and Clean Up CLR Procedures

**Context**: List all CLR-based stored procedures to confirm loading and identify any remnants from previous executions. This aids in operational security by ensuring no persistent artifacts remain, and if unauthorized procedures are found, it indicates potential compromise.

**Command** ([[commands/list-clr-stored-procedures]]):
```powershell
Get-SQLStoredProcedureCLR -Instance <instance> -Verbose
```

> This cmdlet queries the MSSQL system views (e.g., sys.assemblies, sys.procedures) to list CLR procedures. Replace <instance> accordingly. Success shows a table of procedure names, creation dates, and assemblies. Use this to target cleanup: DROP PROCEDURE [runcmd]; DROP ASSEMBLY [runcmd].
