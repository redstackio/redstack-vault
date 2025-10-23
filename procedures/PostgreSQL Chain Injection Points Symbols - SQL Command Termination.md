---
id: dde206a9-8a68-43a2-896c-3712bc7dc688
name: PostgreSQL Chain Injection Points Symbols - SQL Command Termination
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.396571+00:00'
updated_at: '2023-04-10T20:23:21.755395+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[PostgreSQL chain injection points symbols]]'
- '[[PostgreSQL injection]]'
---

# PostgreSQL Chain Injection Points Symbols - SQL Command Termination

## Summary

PostgreSQL injection is a type of SQL injection attack that targets PostgreSQL databases. This attack occurs when an attacker is able to inject malicious SQL code into a PostgreSQL query. This can be done through various chain injection points symbols, one of which is the SQL command termination. B

## Description

# Description

PostgreSQL injection is a type of SQL injection attack that targets PostgreSQL databases. This attack occurs when an attacker is able to inject malicious SQL code into a PostgreSQL query. This can be done through various chain injection points symbols, one of which is the SQL command termination. By terminating a SQL command prematurely, an attacker can inject their own malicious code into the query. This can lead to unauthorized access to sensitive information or the ability to modify or delete data.

 

## Requirements

1. Access to the target network

1. Knowledge of PostgreSQL database structure

1. Tools for SQL injection attacks

 

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Use parameterized queries to prevent chain injection points symbols

1. Limit user privileges to only necessary database functions

 

## Objectives

1. Gain unauthorized access to sensitive information

1. Modify or delete data within the database

 

# Instructions

1. To terminate a SQL command, use the semicolon (;) character within a string constant or quoted identifier. Additionally, the double pipe symbol (||) can be used as an OR statement within a SQL statement.

 



**Code**: [[; #Used to terminate a SQL command. The only place]]



> When writing SQL statements, it is important to properly terminate each command to ensure the statement is executed correctly. The semicolon character is used to signify the end of a command within a statement. It can only be used within a string constant or quoted identifier. Additionally, the double pipe symbol can be used as an OR statement within a SQL statement. For example, when using a SQL injection attack, the double pipe symbol can be used to concatenate a valid query with a malicious query, allowing an attacker to execute arbitrary code on the database.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[PostgreSQL chain injection points symbols]]
- [[PostgreSQL injection]]


