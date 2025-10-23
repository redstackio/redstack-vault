---
id: 5ec4f784-5fa2-47a6-80ee-9fd1adde0191
name: Oracle SQL and Java Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.312142+00:00'
updated_at: '2023-04-10T20:23:12.112891+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Execution through API|T1106 - Execution through API]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
tags:
- '[[Oracle Java Execution]]'
- '[[Oracle SQL Command Execution]]'
- '[[Oracle SQL Injection]]'
commands:
- '[[Grant Java Permissions]]'
- '[[Select all from dba_java_policy]]'
- '[[Select all from user_java_policy]]'
---

# Oracle SQL and Java Command Execution

## Summary

Oracle SQL and Java Command Execution is a technique used by attackers to execute arbitrary SQL commands and Java code on an Oracle database. This technique can be used to gain unauthorized access to sensitive data, escalate privileges, and execute malicious code on the target system. Attackers can

## Description

# Description

Oracle SQL and Java Command Execution is a technique used by attackers to execute arbitrary SQL commands and Java code on an Oracle database. This technique can be used to gain unauthorized access to sensitive data, escalate privileges, and execute malicious code on the target system. Attackers can use various methods such as SQL injection and Java deserialization to exploit vulnerabilities in the Oracle database and achieve their objectives. This technique is a serious threat to organizations that use Oracle databases as it can lead to data theft, system compromise, and financial loss.

 

## Requirements

1. Access to an Oracle database

1. Knowledge of SQL injection and Java deserialization vulnerabilities

1. Access to a tool that can execute SQL and Java commands on the target system

 

## Defense

1. Implement input validation and parameterized queries to prevent SQL injection attacks

1. Disable Java deserialization in the Oracle database

1. Use database firewalls and intrusion detection systems to monitor and block suspicious activity

 

## Objectives

1. Execute arbitrary SQL commands on the target Oracle database

1. Execute arbitrary Java code on the target system

1. Gain unauthorized access to sensitive data

1. Escalate privileges

 

# Instructions

1. This command will list the Java policies for the current user and the entire database. The output will show the details of the Java privileges granted to the user and the database.

 



**Code**: [[select * from dba_java_policy
select * from user_j]]



> The 'select * from dba_java_policy' command lists the Java policies for the entire database. The 'select * from user_java_policy' command lists the Java policies for the current user. The output will show the details of the Java privileges granted to the user and the database. This command is useful for checking the Java privileges of the current user or the entire database.



**Command** ([[Select all from dba_java_policy]]):

```bash
select * from dba_java_policy
```





**Command** ([[Select all from user_java_policy]]):

```bash
select * from user_java_policy
```



2. This command grants Java permissions to the SCOTT user. The permissions granted include the ability to execute all files, write to a file descriptor, and read from a file descriptor.

 



**Code**: [[exec dbms_java.grant_permission('SCOTT', 'SYS:java]]



> The first command grants the permission to execute all files. The second command grants permission to write to a file descriptor, which is necessary for certain Java programs to function properly. The third command grants permission to read from a file descriptor, which is also necessary for certain Java programs. These permissions are granted to the SCOTT user in the database.



**Command** ([[Grant Java Permissions]]):

```bash
exec dbms_java.grant_permission('SCOTT', 'SYS:java.io.FilePermission','<<ALL FILES>>','execute');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'writeFileDescriptor', '');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'readFileDescriptor', '');
```



3. This command allows the user to execute operating system commands from the database. The command takes in arguments such as the path to the command and the arguments to be passed to the command.

 



**Code**: [[SELECT DBMS_JAVA_TEST.FUNCALL('oracle/aurora/util/]]



> It is important to note that this command should be used with caution as it can potentially execute malicious commands on the operating system. The user should ensure that the command being executed is safe and does not cause harm to the system. In addition, the user should also ensure that they have the necessary permissions to execute the command.

4. This command will list all the files in the directory specified in the command. The output will be stored in the file /tmp/OUT.LST.

 



**Code**: [[SELECT DBMS_JAVA.RUNJAVA('oracle/aurora/util/Wrapp]]



> The command uses the DBMS_JAVA.RUNJAVA function to execute a shell command. In this case, the command is '/bin/ls' which lists all the files in the current directory. The output of this command is redirected to the file '/tmp/OUT.LST'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Execution through API|T1106 - Execution through API]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

## Commands Used

- [[Grant Java Permissions]]
- [[Select all from dba_java_policy]]
- [[Select all from user_java_policy]]

## Tags

- [[Oracle Java Execution]]
- [[Oracle SQL Command Execution]]
- [[Oracle SQL Injection]]


