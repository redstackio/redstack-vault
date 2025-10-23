---
id: 72004c31-779f-46e8-b727-a221d3587d4a
name: Identify Trustworthy Databases on MSSQL Server
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.690839+00:00'
updated_at: '2023-04-10T20:36:47.541305+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Find databases that have been configured as trustworthy]]'
- '[[MSSQL Server]]'
commands:
- '[[Invoke SQL Audit Privilege Escalation via Directory Traversal]]'
- '[[Invoke SQL Audit Privilege Escalation via File Existence]]'
- '[[Invoke SQL UNC Path Injection]]'
---

# Identify Trustworthy Databases on MSSQL Server

## Summary

This procedure is used to identify MSSQL databases that have been configured as trustworthy. A database marked as trustworthy allows code within that database to be executed with elevated privileges, which can be exploited by an attacker to gain further access to the system. The procedure involves 

## Description

# Description

This procedure is used to identify MSSQL databases that have been configured as trustworthy. A database marked as trustworthy allows code within that database to be executed with elevated privileges, which can be exploited by an attacker to gain further access to the system. The procedure involves using SQL Audit Privilege Trustworthy command and SQL Injection Commands to query the database for the trustworthy property. By identifying these databases, an attacker can determine which databases are vulnerable and can use this information to escalate privileges.

 

## Requirements

1. Authenticated access to the MSSQL Server

1. SQL Audit Privilege Trustworthy command

1. SQL Injection Commands

 

## Defense

1. Ensure that MSSQL databases are not configured as trustworthy unless absolutely necessary

1. Implement least privilege access controls to limit the impact of privilege escalation attacks

1. Regularly review MSSQL server logs for suspicious activity related to privilege escalation

 

## Objectives

1. Identify MSSQL databases that have been configured as trustworthy

1. Determine which databases are vulnerable to privilege escalation attacks

1. Escalate privileges within the MSSQL environment

 

# Instructions

1. Use the Invoke-SQLAuditPrivTrustworthy command to check if the SQL Server instance is vulnerable to a Trustworthy Database Privilege Escalation attack. This command will also generate a report of the databases that have the TRUSTWORTHY property set to ON.

 



**Code**: [[Invoke-SQLAuditPrivTrustworthy -Instance "<DBSERVE]]



> -Instance: Specifies the name of the SQL Server instance to connect to. 
-Exploit: Enables the exploit mode which will attempt to escalate the privilege. 
-Verbose: Displays detailed output about the command execution. 

The SELECT statement retrieves the name of each database, the name of the database owner, and the value of the TRUSTWORTHY property for each database from the sys.databases system catalog view.

2. These commands are used to test for SQL injection vulnerabilities in a system. 

1. Invoke-SQLAuditPrivXpDirtree: This command checks if the current user has audit privileges and can execute xp_dirtree. If successful, it will return a list of files and directories on the server.

2. Invoke-SQLUncPathInjection: This command tests for SQL injection vulnerabilities via UNC path injection. It does this by attempting to access a file on a remote server via a UNC path. If successful, it will return the contents of the file.

3. Invoke-SQLAuditPrivXpFileexist: This command checks if the current user has audit privileges and can execute xp_fileexist. If successful, it will return information about the existence of a file on the server.

 



**Code**: [[Invoke-SQLAuditPrivXpDirtree
Invoke-SQLUncPathInje]]



> The commands are useful for penetration testers and security researchers to identify SQL injection vulnerabilities in a system. These commands can be used to test for different types of vulnerabilities, such as audit privilege escalation and UNC path injection. The output of these commands can be used to further exploit the vulnerabilities and gain access to sensitive data or systems.



**Command** ([[Invoke SQL Audit Privilege Escalation via Directory Traversal]]):

```bash
Invoke-SQLAuditPrivXpDirtree
```





**Command** ([[Invoke SQL UNC Path Injection]]):

```bash
Invoke-SQLUncPathInjection
```





**Command** ([[Invoke SQL Audit Privilege Escalation via File Existence]]):

```bash
Invoke-SQLAuditPrivXpFileexist
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Invoke SQL Audit Privilege Escalation via Directory Traversal]]
- [[Invoke SQL Audit Privilege Escalation via File Existence]]
- [[Invoke SQL UNC Path Injection]]

## Tags

- [[Find databases that have been configured as trustworthy]]
- [[MSSQL Server]]


