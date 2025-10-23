---
id: 46226e4e-c5ae-4ddf-bd56-3da0d0e8759c
name: MSSQL User Information Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.522484+00:00'
updated_at: '2023-04-10T20:22:40.104494+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[MSSQL Injection]]'
- '[[MSSQL User]]'
commands:
- '[[Get Current User]]'
- '[[Get System User]]'
- '[[Get User]]'
- '[[Get User Name]]'
---

# MSSQL User Information Retrieval

## Summary

MSSQL User Information Retrieval is a technique used to extract user information from a MSSQL database using SQL injection. An attacker can use this technique to obtain usernames, passwords, and other sensitive information. This technique can be used to escalate privileges and gain access to additi

## Description

# Description

MSSQL User Information Retrieval is a technique used to extract user information from a MSSQL database using SQL injection. An attacker can use this technique to obtain usernames, passwords, and other sensitive information. This technique can be used to escalate privileges and gain access to additional systems.

To execute this technique, an attacker would need to identify a SQL injection vulnerability in the target system. Once identified, the attacker can use the 'User Information' command to retrieve user information from the database. This command executes a SQL query that retrieves user information from the 'sysusers' table.

The business value of this technique is that it allows an attacker to obtain sensitive information that can be used for further attacks, such as password spraying or phishing.

 

## Requirements

1. Access to the target system

1. Knowledge of SQL injection techniques

 

## Defense

1. Implement input validation to prevent SQL injection vulnerabilities

1. Use parameterized queries to prevent SQL injection attacks

1. Monitor for suspicious activity, such as unusual database queries

 

## Objectives

1. Retrieve user information from a MSSQL database

1. Escalate privileges and gain access to additional systems

 

# Instructions

1. This command will retrieve information about the current user, including their username and system user.

 



**Code**: [[SELECT CURRENT_USER
SELECT user_name();
SELECT sys]]



> The 'CURRENT_USER' command will return the name of the user who is currently logged in. 'user_name()' will return the current user's username. 'system_user' will return the name of the user who is executing the command. 'user' will return the current user's username as well.



**Command** ([[Get Current User]]):

```bash
SELECT CURRENT_USER
```





**Command** ([[Get User Name]]):

```bash
SELECT user_name()
```





**Command** ([[Get System User]]):

```bash
SELECT system_user
```





**Command** ([[Get User]]):

```bash
SELECT user
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Get Current User]]
- [[Get System User]]
- [[Get User]]
- [[Get User Name]]

## Tags

- [[MSSQL Injection]]
- [[MSSQL User]]


