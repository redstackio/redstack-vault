---
id: 248b8059-759e-4266-8538-0c445d24e838
name: MSSQL Time Based SQL Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.874406+00:00'
updated_at: '2023-04-10T20:22:45.303894+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Non-Standard Port|T1571 - Non-Standard Port]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
tags:
- '[[MSSQL Injection]]'
- '[[MSSQL Time based]]'
---

# MSSQL Time Based SQL Injection

## Summary

MSSQL Time Based SQL Injection is a technique used to exploit web applications that use MSSQL as their database backend. It is a type of SQL injection that allows an attacker to execute arbitrary SQL commands on the target database. This technique is called 'time based' because it relies on the tim

## Description

# Description

MSSQL Time Based SQL Injection is a technique used to exploit web applications that use MSSQL as their database backend. It is a type of SQL injection that allows an attacker to execute arbitrary SQL commands on the target database. This technique is called 'time based' because it relies on the time it takes for the database to respond to a query. The attacker can use this time delay to infer information about the database schema and extract sensitive data. A successful MSSQL Time Based SQL Injection attack can result in the compromise of sensitive data such as usernames, passwords, and credit card information. 

From a technical perspective, the attacker sends specially crafted SQL queries to the web application that cause the database to delay its response. The attacker can then infer information about the database schema based on the time it takes for the database to respond. The attacker can use this information to extract sensitive data from the database. 

From a business perspective, a successful MSSQL Time Based SQL Injection attack can result in the compromise of sensitive data which can lead to financial loss, reputational damage, and legal liability.

## Requirements

1. Access to the target web application

1. Knowledge of MSSQL Time Based SQL Injection techniques

1. Access to a tool that can automate the injection process

## Defense

1. Use parameterized queries to prevent SQL injection attacks

1. Implement proper input validation to prevent malicious input from being processed

1. Regularly update the web application and database software to patch known vulnerabilities

## Objectives

1. To extract sensitive data from the target database

1. To compromise the target web application

1. To gain unauthorized access to the target network

# Instructions

1. This command is used to perform an SQL injection delay attack. It allows the attacker to delay the execution of a query by injecting a 'waitfor delay' statement into the SQL query. The attacker can use this technique to slow down the response time of the application and cause it to crash or become unresponsive.

**Code**: [[ProductID=1;waitfor delay '0:0:10'--
ProductID=1);]]

> The 'waitfor delay' statement is used to delay the execution of a query for a specified amount of time. The attacker can use this statement to cause the application to wait for an extended period of time, which can cause it to become unresponsive. The attacker can inject this statement into the SQL query by appending it to the end of the query. The attacker can also use this technique to test for SQL injection vulnerabilities in the application by modifying the 'SLEEPTIME' parameter to see how long the application takes to respond.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Non-Standard Port|T1571 - Non-Standard Port]]
- [[Scheduled Task|T1053 - Scheduled Task]]

## Tags

- [[MSSQL Injection]]
- [[MSSQL Time based]]
