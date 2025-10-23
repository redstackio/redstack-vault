---
id: bd1ac113-8a6f-4128-b20e-b2a930964303
name: Creating and Importing a CLR Assembly for MSSQL Server
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.439838+00:00'
updated_at: '2023-04-10T20:36:42.117302+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Email Collection|T1114 - Email Collection]]'
- '[[Process Injection|T1055 - Process Injection]]'
tags:
- '[[CLR Assemblies]]'
- '[[Manually creating a CLR DLL and importing it]]'
- '[[MSSQL Server]]'
commands:
- '[[Create Assembly]]'
- '[[Enable advanced options]]'
- '[[Enable CLR]]'
- '[[Execute whoami command]]'
---

# Creating and Importing a CLR Assembly for MSSQL Server

## Summary

This procedure involves manually creating a CLR DLL and importing it into MSSQL Server. This technique can be used by an attacker to bypass security controls and execute malicious code on the server. The attacker can use this technique to gain access to sensitive data, escalate privileges, and main

## Description

# Description

This procedure involves manually creating a CLR DLL and importing it into MSSQL Server. This technique can be used by an attacker to bypass security controls and execute malicious code on the server. The attacker can use this technique to gain access to sensitive data, escalate privileges, and maintain persistence on the system.

To create the CLR DLL, the attacker must first enable the 'Show Advanced Options' and 'CLR' options on the server. The attacker can then create the DLL using Visual Studio or another development tool. Once the DLL is created, the attacker can import it into MSSQL Server and link it to a stored procedure. The attacker can then execute the stored procedure to retrieve user information and clean up after themselves.

From a business perspective, this technique can be used to steal sensitive data, compromise user credentials, and disrupt business operations.

 

## Requirements

1. Access to MSSQL Server

1. Enable 'Show Advanced Options' and 'CLR' options on the server

1. Development tool such as Visual Studio

 

## Defense

1. Disable the 'CLR' option on the server if it is not required for business operations

1. Monitor for any unusual activity or processes running on the server

1. Implement network segmentation and access controls to limit access to the MSSQL Server

 

## Objectives

1. Create a CLR DLL

1. Import the DLL into MSSQL Server

1. Link the DLL to a stored procedure

1. Retrieve user information

1. Cover tracks and clean up after the attack

 

# Instructions

1. To enable the `show advanced options` setting on the server, run the following SQL command:

 



**Code**: [[sp_configure 'show advanced options',1; 
RECONFIGU]]



> This command enables the display of advanced configuration options in SQL Server Configuration Manager. The `sp_configure` system stored procedure is used to change server-level configuration options, and the `RECONFIGURE` statement is used to apply the changes to the server. This setting can be useful for troubleshooting and advanced configuration scenarios.



**Command** ([[Enable advanced options]]):

```bash
sp_configure 'show advanced options',1; 
RECONFIGURE
GO
```



2. To enable CLR on the server, run the following commands:
1. sp_configure 'clr enabled', 1
2. RECONFIGURE
3. GO

 



**Code**: [[sp_configure 'clr enabled',1
RECONFIGURE
GO]]



> This command enables the Common Language Runtime (CLR) integration feature on the SQL Server. CLR allows developers to write stored procedures, triggers, user-defined functions, user-defined types, and aggregates using any .NET Framework language, such as C# or Visual Basic. The sp_configure system stored procedure is used to configure various server-level settings, including CLR integration. The RECONFIGURE statement is used to apply the configuration changes. The GO statement is used to execute the previous batch of statements. Note that enabling CLR may have security implications and should be done with caution.



**Command** ([[Enable CLR]]):

```bash
sp_configure 'clr enabled',1
RECONFIGURE
GO
```



3. Use this command to import an assembly into SQL Server. Specify the path of the assembly file in the FROM clause and provide a name for the assembly in the CREATE ASSEMBLY statement. You can also specify the permission set for the assembly using the WITH PERMISSION_SET clause.

 



**Code**: [[CREATE ASSEMBLY my_assembly
FROM 'c:\temp\cmd_exec]]



> The CREATE ASSEMBLY statement is used to import an assembly into SQL Server. An assembly is a collection of one or more files that contain code that can be executed by the .NET runtime. Once an assembly is imported into SQL Server, you can use it to create SQL Server objects such as stored procedures, functions, and triggers. The FROM clause specifies the path of the assembly file on the file system. The WITH PERMISSION_SET clause specifies the security level at which the assembly will run. UNSAFE allows the assembly to access external resources and execute unmanaged code.



**Command** ([[Create Assembly]]):

```bash
CREATE ASSEMBLY my_assembly
FROM 'c:\temp\cmd_exec.dll'
WITH PERMISSION_SET = UNSAFE;
```



4. To link the assembly to a stored procedure, use the CREATE PROCEDURE statement followed by the name of the stored procedure and the parameters. In the AS clause, specify the name of the assembly, the namespace, and the class that contains the stored procedure. Finally, use the EXTERNAL NAME clause to specify the name of the method that implements the stored procedure.

 



**Code**: [[CREATE PROCEDURE [dbo].[cmd_exec] @execCommand NVA]]



> The @execCommand parameter is a string that contains the command to be executed. This command can be any valid SQL statement or batch. The maximum length of the command is 4000 characters. The stored procedure executes the command and returns the result set, if any. This command is useful when you need to execute dynamic SQL statements, or when you want to execute a command that is not supported by the T-SQL language.

5. This command retrieves the current user information by executing the 'whoami' command. After retrieving the information, it cleans up by dropping the 'cmd_exec' procedure and 'my_assembly' assembly.

 



**Code**: [[cmd_exec "whoami"
DROP PROCEDURE cmd_exec
DROP ASS]]



> The 'cmd_exec' procedure is used to execute external commands from within SQL Server. In this case, it is used to execute the 'whoami' command which retrieves the current user information. The 'DROP PROCEDURE' and 'DROP ASSEMBLY' commands are used to clean up after executing the 'whoami' command by removing any unnecessary objects from the database.



**Command** ([[Execute whoami command]]):

```bash
cmd_exec "whoami"
```



6. To create an assembly in SQL Server, use the CREATE ASSEMBLY statement. The CREATE ASSEMBLY statement requires the assembly name, authorization, and binary representation of the assembly. The WITH PERMISSION_SET option specifies the permission set that the assembly will be loaded with.

 



**Code**: [[CREATE ASSEMBLY [my_assembly] AUTHORIZATION [dbo] ]]



> The CREATE ASSEMBLY statement is used to create a .NET Framework assembly in SQL Server. The assembly can be used to extend the functionality of SQL Server by adding user-defined functions, stored procedures, triggers, or user-defined types. In this specific case, the hexadecimal string representation of a CLR DLL is used to create the assembly. The AUTHORIZATION clause specifies the owner of the assembly. The WITH PERMISSION_SET option specifies the permission set that the assembly will be loaded with, which can be either SAFE, EXTERNAL_ACCESS, or UNSAFE. The permission set determines the level of access the assembly has to system resources outside of the database.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Email Collection|T1114 - Email Collection]]
- [[Process Injection|T1055 - Process Injection]]

## Commands Used

- [[Create Assembly]]
- [[Enable advanced options]]
- [[Enable CLR]]
- [[Execute whoami command]]

## Tags

- [[CLR Assemblies]]
- [[Manually creating a CLR DLL and importing it]]
- [[MSSQL Server]]


