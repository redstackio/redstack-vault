---
id: 414bab68-d171-4fe2-9a92-4d2cb08c2537
name: MSSQL Server R Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.630962+00:00'
updated_at: '2023-04-10T20:36:38.213689+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[MSSQL Server]]'
- '[[R]]'
---

# MSSQL Server R Command Execution

## Summary

MSSQL Server R Command Execution is a technique used by attackers to execute arbitrary code on a SQL Server using R scripts. This technique can be used to bypass security controls and gain access to sensitive data stored in the database. Attackers can use this technique to execute commands on the u

## Description

# Description

MSSQL Server R Command Execution is a technique used by attackers to execute arbitrary code on a SQL Server using R scripts. This technique can be used to bypass security controls and gain access to sensitive data stored in the database. Attackers can use this technique to execute commands on the underlying operating system and gain full control of the server. To execute R scripts, attackers can use the 'Execute SQL OS Command and External Script' command available in MSSQL Server.

Technical Explanation: The 'Execute SQL OS Command and External Script' command allows users to execute operating system commands and scripts on the server. Attackers can use this command to execute R scripts that can be used to execute arbitrary code on the server. By default, the MSSQL Server service account has permission to execute R scripts, making it an attractive target for attackers.

Business Value: Attackers can use this technique to gain access to sensitive data stored in the database, such as customer information, financial data, and intellectual property. This can result in reputational damage, financial loss, and legal liability for the affected organization.

 

## Requirements

1. Access to the MSSQL Server

1. Authenticated user account with permission to execute R scripts

1. Knowledge of R scripting language

 

## Defense

1. Restrict permissions for the MSSQL Server service account to prevent it from executing arbitrary R scripts

1. Monitor MSSQL Server logs for suspicious activity, such as the use of the 'Execute SQL OS Command and External Script' command

1. Implement network segmentation to limit the impact of a successful attack on the MSSQL Server

 

## Objectives

1. Execute arbitrary code on the MSSQL Server

1. Bypass security controls and gain access to sensitive data

1. Gain full control of the server

 

# Instructions

1. This command is used to execute an SQL OS command and an external script on a specified SQL Server instance. The command takes in parameters such as the username and password for the instance, the instance name, and the base64 encoded script for the SQL OS command. It also executes an external script in R language that returns data in the form of a data frame. The script can be modified to execute any desired command.

 



**Code**: [[Invoke-SQLOSCmdR -Username sa -Password Password12]]



> The 'Invoke-SQLOSCmdR' cmdlet is used to execute an SQL OS command on a specified SQL Server instance. The cmdlet takes in parameters such as the username and password for the instance, the instance name, and the base64 encoded script for the SQL OS command. The 'sp_execute_external_script' stored procedure is used to execute an external script in R language that returns data in the form of a data frame. The 'system' function is used to execute the 'cmd.exe /c dir' command and the 'shell' function is used to execute the 'dir' command. The returned data is in the form of a text file containing the output of the executed command.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]

## Tags

- [[MSSQL Server]]
- [[R]]


