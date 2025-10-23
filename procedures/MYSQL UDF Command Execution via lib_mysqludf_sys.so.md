---
id: ab79a658-3f1b-4c9d-ac36-33a9fe4c5426
name: MYSQL UDF Command Execution via lib_mysqludf_sys.so
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.973249+00:00'
updated_at: '2023-04-10T20:22:59.128087+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Execution through API|T1106 - Execution through API]]'
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
- '[[User Execution|T1204 - User Execution]]'
tags:
- '[[MYSQL Injection]]'
- '[[MYSQL UDF command execution]]'
commands:
- '[[Console log Hello World!]]'
- '[[Find location of lib_mysqludf_sys.so]]'
- '[[List Files in Directory]]'
- '[[Retrieve MySQL User ID]]'
---

# MYSQL UDF Command Execution via lib_mysqludf_sys.so

## Summary

MYSQL UDF command execution via lib_mysqludf_sys.so is a technique used to execute arbitrary commands on a MYSQL database server. This technique involves exploiting MYSQL injection vulnerabilities to inject malicious code into the server. The attacker then loads the lib_mysqludf_sys.so library, whi

## Description

# Description

MYSQL UDF command execution via lib_mysqludf_sys.so is a technique used to execute arbitrary commands on a MYSQL database server. This technique involves exploiting MYSQL injection vulnerabilities to inject malicious code into the server. The attacker then loads the lib_mysqludf_sys.so library, which is a user-defined function (UDF) library that allows the execution of system commands. Once loaded, the attacker can execute any command they want on the server. This technique can be used to escalate privileges, exfiltrate data, or perform other malicious activities.

 

## Requirements

1. Access to a MYSQL database server

1. Knowledge of MYSQL injection vulnerabilities

1. Ability to load UDF libraries

 

## Defense

1. Ensure that the MYSQL server is patched and up-to-date

1. Implement input validation and sanitization to prevent MYSQL injection vulnerabilities

1. Restrict access to the MYSQL server to trusted users and networks

 

## Objectives

1. Execute arbitrary commands on a MYSQL database server

1. Escalate privileges on the server

1. Exfiltrate data from the server

 

# Instructions

1. To check if lib_mysqludf_sys.so is installed, run the following command:

whereis lib_mysqludf_sys.so

This will return the path to the library file if it is installed on the server.

 



**Code**: [[$ whereis lib_mysqludf_sys.so
/usr/lib/lib_mysqlud]]



> The 'whereis' command is used to locate the binary, source, and manual page files for a command. In this case, we are using it to locate the lib_mysqludf_sys.so library file. If the file is installed on the server, the command will return the path to the file. If the file is not installed, the command will return an empty response.



**Command** ([[Find location of lib_mysqludf_sys.so]]):

```bash
whereis lib_mysqludf_sys.so
```



2. sys_exec(command, args=None, shell=False)

 



**Code**: [[sys_exec]]



> This command allows you to execute a system command. The 'command' parameter is mandatory and should contain the command you want to execute. The 'args' parameter is optional and can be used to pass arguments to the command. The 'shell' parameter is also optional and can be set to True if you want to execute the command in a shell environment. Note that using shell=True can be a security risk if you're not careful with the input.



**Command** ([[List Files in Directory]]):

```bash
ls -l
```



3. The sys_eval command is used to evaluate the system performance and resource utilization.

 



**Code**: [[sys_eval]]



> This command takes no arguments and provides a detailed report on the current system performance, including CPU usage, memory usage, disk usage, and network usage. The report can be used to identify potential performance bottlenecks and optimize system performance.



**Command** ([[Console log Hello World!]]):

```bash
console.log('Hello World!');
```



4. To retrieve the user ID of the current MySQL user, run the following command:

mysql> SELECT sys_eval('id');

 



**Code**: [[$ mysql -u root -p mysql
Enter password: [...]
mys]]



> This command executes the 'id' command within the MySQL shell, which returns the user ID, group ID, and group memberships of the current user. The 'sys_eval' function is used to execute the command within the shell. The output of the command is displayed in a table format with the user ID, group ID, and group memberships separated by spaces.



**Command** ([[Retrieve MySQL User ID]]):

```bash
$ mysql -u root -p mysql
Enter password: [...]
mysql> SELECT sys_eval('id');
+--------------------------------------------------+
| sys_eval('id') |
+--------------------------------------------------+
| uid=118(mysql) gid=128(mysql) groups=128(mysql) |
+--------------------------------------------------+
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Execution through API|T1106 - Execution through API]]
- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]
- [[User Execution|T1204 - User Execution]]

## Commands Used

- [[Console log Hello World!]]
- [[Find location of lib_mysqludf_sys.so]]
- [[List Files in Directory]]
- [[Retrieve MySQL User ID]]

## Tags

- [[MYSQL Injection]]
- [[MYSQL UDF command execution]]


