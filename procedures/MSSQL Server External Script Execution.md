---
id: 764f3a92-7435-4999-a9e3-4f4ee1e4471d
name: MSSQL Server External Script Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.584652+00:00'
updated_at: '2023-04-10T20:36:46.832400+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
tags:
- '[[External Scripts]]'
- '[[MSSQL Server]]'
commands:
- '[[Enable External Scripts]]'
---

# MSSQL Server External Script Execution

## Summary

MSSQL Server External Script Execution is a technique used to execute external scripts on a MSSQL Server. This can be used by an attacker to execute malicious code on the target system. To enable external scripts, the command 'Enable External Scripts' needs to be executed on the SQL Server. Once ex

## Description

# Description

MSSQL Server External Script Execution is a technique used to execute external scripts on a MSSQL Server. This can be used by an attacker to execute malicious code on the target system. To enable external scripts, the command 'Enable External Scripts' needs to be executed on the SQL Server. Once external scripts are enabled, the attacker can use various methods to execute their code, such as xp_cmdshell, PowerShell, or Python scripts. 

From a technical perspective, enabling external scripts allows the SQL Server to execute commands outside of the SQL Server process, which can be a security risk if not properly secured. However, enabling external scripts can also provide value to legitimate users who need to execute scripts for automation or other purposes.

The business value of this technique is that an attacker can use it to gain access to sensitive data or to execute commands on the target system.

 

## Requirements

1. Access to the MSSQL Server

1. Permission to execute external scripts

1. Ability to upload and execute external scripts

 

## Defense

1. Disable external scripts if not needed

1. Restrict access to the MSSQL Server and limit permissions for users

1. Monitor for any suspicious activity, such as the execution of unknown scripts

 

## Objectives

1. Execute external scripts on a MSSQL Server

1. Gain access to sensitive data

1. Execute commands on the target system

 

# Instructions

1. To enable external scripts in SQL Server, use the sp_configure system stored procedure with the 'external scripts enabled' option. Set the value to 1 and then run the RECONFIGURE statement to apply the changes.

 



**Code**: [[sp_configure 'external scripts enabled', 1;
RECONF]]



> This command enables the execution of external scripts in SQL Server. External scripts are scripts that are not written in T-SQL, such as R or Python scripts. Enabling external scripts allows you to run these scripts within SQL Server and integrate them with your T-SQL code. This can be useful for performing complex data analysis or machine learning tasks within SQL Server.



**Command** ([[Enable External Scripts]]):

```bash
sp_configure 'external scripts enabled', 1;
RECONFIGURE;
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]

## Commands Used

- [[Enable External Scripts]]

## Tags

- [[External Scripts]]
- [[MSSQL Server]]


