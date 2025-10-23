---
id: df4609d5-ab2d-44e3-bbc5-c878a5691f09
name: Oracle SQL Database Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.176138+00:00'
updated_at: '2023-04-10T20:23:09.519577+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Query Registry|T1012 - Query Registry]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Oracle SQL Injection]]'
- '[[Oracle SQL List Databases]]'
commands:
- '[[Retrieve distinct owners from all tables]]'
---

# Oracle SQL Database Enumeration

## Summary

Oracle SQL Database Enumeration is a technique used to discover all databases within an Oracle database server. This technique is achieved through SQL injection vulnerabilities within the Oracle database server. Once a SQL injection vulnerability is found, an attacker can use this technique to list

## Description

# Description

Oracle SQL Database Enumeration is a technique used to discover all databases within an Oracle database server. This technique is achieved through SQL injection vulnerabilities within the Oracle database server. Once a SQL injection vulnerability is found, an attacker can use this technique to list all databases within the server.

From a technical standpoint, this technique is achieved by using the 'UNION' operator in SQL injection payloads. The 'UNION' operator is used to combine the results of two or more SELECT statements into a single result set. By using the 'UNION' operator, an attacker can combine the results of a SELECT statement that lists all known databases with the original SQL injection payload.

The business value of this technique is that it allows an attacker to gain a better understanding of the target environment. This information can be used to identify sensitive data within the databases and to plan further attacks against the target.

 

## Requirements

1. Access to an Oracle database server with a SQL injection vulnerability

 

## Defense

1. Ensure that all input is properly sanitized before being sent to the database server

1. Implement a web application firewall to detect and block SQL injection attempts

1. Use least privilege access controls to limit the potential impact of a successful SQL injection attack

 

## Objectives

1. Identify all databases within the Oracle database server

1. Gain a better understanding of the target environment

 

# Instructions

1. This command lists all the owners of the tables in the database.

 



**Code**: [[SELECT DISTINCT owner FROM all_tables;]]



> The 'SELECT DISTINCT' statement is used to return only distinct (different) values. In this case, it retrieves only the distinct owners from the 'all_tables' view. The 'owner' column in this view contains the name of the user who owns the table. This command is useful when you need to know who owns the tables in the database, for example, to grant or revoke privileges.



**Command** ([[Retrieve distinct owners from all tables]]):

```bash
SELECT DISTINCT owner FROM all_tables;
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Query Registry|T1012 - Query Registry]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Retrieve distinct owners from all tables]]

## Tags

- [[Oracle SQL Injection]]
- [[Oracle SQL List Databases]]


