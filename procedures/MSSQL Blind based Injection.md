---
id: 51e72513-e6d3-4dbf-8650-a06645f0a4b2
name: MSSQL Blind based Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.855781+00:00'
updated_at: '2023-04-10T20:22:41.647842+00:00'
tags:
- '[[MSSQL Blind based]]'
- '[[MSSQL Injection]]'
---

# MSSQL Blind based Injection

## Summary

MSSQL Blind based Injection is a technique used by attackers to exploit vulnerabilities in MSSQL databases. This type of injection is called 'blind' because the attacker does not receive any direct feedback from the database. Instead, they must infer the results of their queries based on the behavi

## Description

# Description

MSSQL Blind based Injection is a technique used by attackers to exploit vulnerabilities in MSSQL databases. This type of injection is called 'blind' because the attacker does not receive any direct feedback from the database. Instead, they must infer the results of their queries based on the behavior of the application. Attackers can use this technique to extract sensitive information such as passwords, credit card numbers, and other confidential data.

To exploit this vulnerability, attackers use SQL Injection Commands to inject malicious SQL statements into the application. These statements manipulate the behavior of the application and allow attackers to extract data from the database.

MSSQL Blind based Injection can be used to bypass authentication, escalate privileges, and execute arbitrary code on the database server. This technique can have serious consequences for businesses, as it can lead to data breaches and compromise sensitive information.

 

## Requirements

1. Access to the target application

1. Knowledge of SQL Injection Commands

1. Access to a tool for SQL Injection, such as SQLMap

 

## Defense

1. Use parameterized queries to prevent SQL Injection attacks

1. Implement least privilege access controls to limit the impact of successful attacks

1. Regularly update and patch MSSQL databases to reduce the risk of exploitation

 

## Objectives

1. Extract sensitive information from MSSQL databases

1. Bypass authentication and escalate privileges

1. Execute arbitrary code on the database server

 

# Instructions

1. These commands are used for SQL injection attacks. The commands are designed to extract sensitive information from a database by exploiting vulnerabilities in the SQL code.

 



**Code**: [[AND LEN(SELECT TOP 1 username FROM tblusers)=5 ; -]]



> The first command checks if the length of the username field in the tblusers table is 5. The second command checks if the first character of the username is 'a'. The third command checks if the ASCII value of the first character of the string 'A' is greater than 64. The fourth command checks if the ASCII value of the first character of the lowercase version of the current database name is greater than 90. The fifth command selects the version of the database if the version is '12.0.2000.8'. The sixth command selects the first message from the log_table where the message starts with the letter 't'.

## Tags

- [[MSSQL Blind based]]
- [[MSSQL Injection]]


