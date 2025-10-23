---
id: 5454177f-57f4-4f6e-a0c8-cedbeb32572a
name: MSSQL Server Role Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.744692+00:00'
updated_at: '2023-04-10T20:36:37.791496+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
tags:
- '[[Current Role]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
commands:
- '[[List all users]]'
- '[[Select John]]'
---

# MSSQL Server Role Enumeration

## Summary

MSSQL Server Role Enumeration is a technique used by attackers to identify the current role of a user in the MSSQL Server. An attacker can use this information to identify the privileges of the user and plan their next move. To perform this technique, the attacker can use manual SQL Server queries 

## Description

# Description

MSSQL Server Role Enumeration is a technique used by attackers to identify the current role of a user in the MSSQL Server. An attacker can use this information to identify the privileges of the user and plan their next move. To perform this technique, the attacker can use manual SQL Server queries to identify the current role of the user. This technique can be used in various stages of an attack, such as initial access, privilege escalation, and lateral movement.

From a technical perspective, this technique involves querying the MSSQL Server system tables to identify the current role of the user. The attacker can use various SQL queries to extract this information. The attacker can use the 'User Selection' command to identify the current role of the user.

From a business value perspective, this technique can help attackers gain access to sensitive data and systems. By identifying the current role of the user, the attacker can plan their next move and perform various malicious activities.


 

## Requirements

1. Access to the MSSQL Server

1. Authentication credentials with appropriate privileges

1. Knowledge of manual SQL Server queries

 

## Defense

1. Implement the principle of least privilege to restrict the privileges of the users

1. Monitor and analyze MSSQL Server logs for any suspicious activities

1. Regularly update and patch the MSSQL Server to prevent known vulnerabilities

 

## Objectives

1. Identify the current role of the user in the MSSQL Server

1. Plan the next move based on the user's privileges

1. Perform malicious activities such as data exfiltration or privilege escalation

 

# Instructions

1. To select a user from a database table, use the SELECT statement followed by the name of the table and the column(s) you want to retrieve. For example: SELECT * FROM users;

 



**Code**: [[Select user]]



> The SELECT statement is used to retrieve data from one or more tables in a database. In this case, we are retrieving data from the 'users' table. The '*' symbol means to retrieve all columns from the table. You can also specify specific columns by listing them after the SELECT statement, separated by commas. For example: SELECT name, email, phone FROM users; This will retrieve only the 'name', 'email', and 'phone' columns from the 'users' table.



**Command** ([[List all users]]):

```bash
db.users.find()
```





**Command** ([[Select John]]):

```bash
db.users.find({'name': 'John'})
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]
- [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]

## Commands Used

- [[List all users]]
- [[Select John]]

## Tags

- [[Current Role]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]


