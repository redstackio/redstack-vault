---
id: 51507ce7-41e2-4b97-b824-dbf382204d9d
name: MYSQL Blind Injection using a Conditional Statement
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.608505+00:00'
updated_at: '2023-04-10T20:22:57.635352+00:00'
tags:
- '[[MYSQL Blind]]'
- '[[MYSQL Blind using a conditional statement]]'
- '[[MYSQL Injection]]'
---

# MYSQL Blind Injection using a Conditional Statement

## Summary

MYSQL Blind Injection using a Conditional Statement is a technique used to exploit MYSQL databases that are vulnerable to SQL Injection attacks. This technique is used when the attacker does not have direct access to the database and cannot see the results of their queries. Instead, the attacker us

## Description

# Description

MYSQL Blind Injection using a Conditional Statement is a technique used to exploit MYSQL databases that are vulnerable to SQL Injection attacks. This technique is used when the attacker does not have direct access to the database and cannot see the results of their queries. Instead, the attacker uses a series of conditional statements to infer information about the database. The attacker can use this technique to extract sensitive information such as usernames, passwords, and other confidential data. 

To execute this attack, the attacker sends specially crafted SQL queries to the database. The queries are designed to exploit vulnerabilities in the database that allow the attacker to execute arbitrary code. The attacker can then use the conditional statements to infer information about the database. 

The business value of this attack lies in the fact that MYSQL is one of the most widely used databases in the world. By exploiting vulnerabilities in MYSQL databases, attackers can gain access to sensitive data, compromise systems, and cause significant damage to organizations.

## Requirements

1. Access to a vulnerable MYSQL database

1. Knowledge of MYSQL Blind Injection using a Conditional Statement

1. SQL Injection Attack tools

## Defense

1. Implement input validation and sanitization techniques to prevent SQL Injection attacks

1. Use parameterized queries to mitigate the risk of SQL Injection attacks

1. Implement least privilege access controls to limit the damage that can be caused by attackers

## Objectives

1. Extract sensitive information such as usernames, passwords, and other confidential data

1. Gain access to the database

1. Compromise systems

# Instructions

1. This command checks the version number of the SQL Server instance and returns TRUE if the version number starts with a 5.

**Code**: [[if @@version starts with a 5]]

> The @@version variable returns a string that contains the version number of the SQL Server instance. This command checks if the version number starts with a 5, which is a common identifier for SQL Server 2005 and later versions. If the version number does start with a 5, the command returns TRUE. Otherwise, it returns FALSE.

2. The SQL injection attack is a technique used to exploit vulnerabilities in web applications that use SQL databases. The attack involves inserting malicious SQL code into a web form input field, which is then executed by the database server. This can allow the attacker to bypass authentication, steal data, or even take control of the server.

**Code**: [[2100935' OR IF(MID(@@version,1,1)='5',sleep(1),1)=]]

> In this particular example, the attacker is attempting to determine if the database server is running MySQL version 5 by using the MID() function to extract the first character of the @@version variable. If the first character is '5', the attacker uses the SLEEP() function to pause the execution of the query for 1 second, which can indicate to them that the server is vulnerable to a time-based attack. The '2' at the end of the query is just used to close the existing SQL statement and cause a syntax error, which can help to prevent the server from returning an error message that could reveal information about the database schema.

3. This command checks the version of SQL Server and returns a boolean value indicating whether the version starts with a 4 or not.

**Code**: [[if @@version starts with a 4]]

> The @@version variable returns the version information of the SQL Server instance. This command checks if the version starts with a 4 and returns a boolean value indicating whether it does or not. If the version does start with a 4, the command returns True, otherwise it returns False.

4. This command is used to perform SQL injection attacks on vulnerable web applications. The injected code is used to manipulate the SQL query and retrieve sensitive information from the database.

**Code**: [[2100935' OR IF(MID(@@version,1,1)='4',sleep(1),1)=]]

> The 'data' field contains the payload used to exploit the SQL injection vulnerability. The payload is designed to retrieve information from the database or to perform other malicious activities. The 'lang' field specifies the programming language used in the payload. The 'instruction' field provides details on how to use the payload to exploit the vulnerability. The 'explain' field describes the purpose and functionality of the payload.

## Tags

- [[MYSQL Blind]]
- [[MYSQL Blind using a conditional statement]]
- [[MYSQL Injection]]
