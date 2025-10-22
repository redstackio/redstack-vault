---
id: 59fdffc4-8dad-4e13-9cc6-94f11fd4fe80
name: Command Execution via xp_cmdshell - MSSQL Server
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.271553+00:00'
updated_at: '2023-04-10T20:36:43.564109+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[DLL Side-Loading|T1073 - DLL Side-Loading]]'
tags:
- '[[Command Execution via xp_cmdshell]]'
- '[[MSSQL Server]]'
commands:
- '[[Enable xp_cmdshell]]'
---

# Command Execution via xp_cmdshell - MSSQL Server

## Summary

Command Execution via xp_cmdshell is a technique used to execute arbitrary commands on a Microsoft SQL Server by leveraging the xp_cmdshell stored procedure. This procedure allows users to execute shell commands on the underlying operating system where the SQL Server is installed. Attackers can use

## Description

# Description

Command Execution via xp_cmdshell is a technique used to execute arbitrary commands on a Microsoft SQL Server by leveraging the xp_cmdshell stored procedure. This procedure allows users to execute shell commands on the underlying operating system where the SQL Server is installed. Attackers can use this technique to gain access to sensitive data or to perform other malicious activities. By executing commands with the privileges of the SQL Server service account, attackers can escalate their privileges and move laterally within the network.

To execute commands via xp_cmdshell, the user must have the required permissions to execute the xp_cmdshell stored procedure. Once permissions are granted, the user can execute any command that the SQL Server service account is authorized to execute. This can include commands to download and execute malware, dump password hashes, or create new user accounts on the system.

The business value of this technique is that it allows attackers to gain access to sensitive data stored on the SQL Server, such as customer data or financial records. It also allows attackers to move laterally within the network and gain access to other systems that are connected to the SQL Server.

## Requirements

1. Authenticated access to the Microsoft SQL Server

1. Permissions to execute the xp_cmdshell stored procedure

## Defense

1. Disable or remove the xp_cmdshell stored procedure if it is not required for business operations

1. Restrict permissions to the xp_cmdshell stored procedure to only authorized users

1. Monitor for suspicious activity, such as unusual command execution or changes to the xp_cmdshell stored procedure

## Objectives

1. Execute arbitrary commands on a Microsoft SQL Server

1. Gain access to sensitive data stored on the SQL Server

1. Escalate privileges and move laterally within the network

# Instructions

1. To retrieve information about the Windows user, execute the SQL query provided. The query will retrieve information such as user accounts, current user's name, directory listing of the C drive, and ping the local IP address.

**Code**: [[EXEC xp_cmdshell "net user";
EXEC master..xp_cmdsh]]

> The SQL query provided executes several xp_cmdshell commands to retrieve information about the Windows user. The 'net user' command retrieves information about user accounts on the system. The 'whoami' command retrieves the name of the current user. The 'cmd.exe dir c:' command lists the contents of the C drive. The 'ping 127.0.0.1' command pings the local IP address to test network connectivity. Note that the use of xp_cmdshell should be limited and only used when necessary, as it can pose a security risk if not used properly.

2. To reactivate xp_cmdshell, run the following commands in SQL Server Management Studio:

**Code**: [[EXEC sp_configure 'show advanced options',1;
RECON]]

> The xp_cmdshell command in SQL Server allows users to execute command shell commands from within T-SQL. It is disabled by default in SQL Server 2005 for security reasons. To reactivate it, you need to execute these three commands:

1. EXEC sp_configure 'show advanced options',1;
2. RECONFIGURE;
3. EXEC sp_configure 'xp_cmdshell',1;
4. RECONFIGURE;

The first command enables the 'show advanced options' configuration option, which allows you to modify advanced settings in SQL Server. The second command applies the configuration change. The third command enables xp_cmdshell. The fourth command applies the configuration change.

**Command** ([[Enable xp_cmdshell]]):

```bash
EXEC sp_configure 'show advanced options',1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell',1;
RECONFIGURE;
```

3. Use this command to add an extended stored procedure named xp_cmdshell to SQL Server. This procedure allows you to execute command-line commands on the server. The xplog70.dll file is required for this procedure to function properly.

**Code**: [[sp_addextendedproc 'xp_cmdshell','xplog70.dll']]

> The first argument of the sp_addextendedproc command is the name of the extended procedure you want to add. The second argument is the DLL file that contains the code for the procedure. This command should only be used by experienced database administrators and developers, as it can pose a security risk if not used properly.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[DLL Side-Loading|T1073 - DLL Side-Loading]]

## Commands Used

- [[Enable xp_cmdshell]]

## Tags

- [[Command Execution via xp_cmdshell]]
- [[MSSQL Server]]
