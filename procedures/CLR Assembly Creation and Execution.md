---
id: 610ee597-10b0-4b3f-9371-bacb03cc4eca
name: CLR Assembly Creation and Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.411015+00:00'
updated_at: '2023-04-10T20:36:40.652382+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Process Injection|T1055 - Process Injection]]'
tags:
- '[[CLR Assemblies]]'
- '[[Manually creating a CLR DLL and importing it]]'
- '[[MSSQL Server]]'
---

# CLR Assembly Creation and Execution

## Summary

CLR Assemblies are used to execute managed code within SQL Server. This technique can be used to evade detection and gain access to sensitive data. The creation and execution of a CLR Assembly involves manually creating a DLL and importing it into SQL Server. This can be done using C# code and the 

## Description

# Description

CLR Assemblies are used to execute managed code within SQL Server. This technique can be used to evade detection and gain access to sensitive data. The creation and execution of a CLR Assembly involves manually creating a DLL and importing it into SQL Server. This can be done using C# code and the Execute Command function.

From an offensive standpoint, this technique can be used to bypass security measures and gain access to sensitive data stored within the MSSQL Server. From a technical perspective, this technique involves creating a DLL using C# code and then importing it into SQL Server using the Execute Command function. From a business standpoint, this technique can be used to gain access to sensitive data, resulting in financial loss and reputational damage.

## Requirements

1. Access to SQL Server

1. C# compiler

## Defense

1. Implement strict access controls and limit user privileges to prevent unauthorized access to SQL Server

1. Regularly monitor and analyze SQL Server logs for any suspicious activity or unauthorized access attempts

1. Disable CLR integration if it is not required for the functioning of the SQL Server

## Objectives

1. Gain access to sensitive data stored within MSSQL Server

1. Bypass security measures

# Instructions

1. To create a C# DLL file using the above command, you need to have the .NET framework installed on your system. You also need to have a C# code file named cmd_exec.cs saved in the C:\temp directory.

**Code**: [[C:\Windows\Microsoft.NET\Framework64\v4.0.30319\cs]]

> The above command uses the C# compiler (csc.exe) to create a DLL file with a target of 'library'. The path of the csc.exe file is specified as C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe. The path of the cmd_exec.cs file is specified as c:\temp\cmd_exec.cs. The resulting DLL file will be created in the same directory as the cmd_exec.cs file.

2. Execute a command on the command prompt and return the output

**Code**: [[using System;
using System.Data;
using System.Data]]

> This command executes a command on the command prompt and returns the output. The command to be executed should be passed as an argument to the stored procedure. The output of the command is returned as a result set with a single column named 'output'.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Process Injection|T1055 - Process Injection]]

## Tags

- [[CLR Assemblies]]
- [[Manually creating a CLR DLL and importing it]]
- [[MSSQL Server]]
