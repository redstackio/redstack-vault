---
id: ce1253ab-87b8-4ce3-8052-bc4f02ee17d7
name: SQLite Boolean-Based Order By Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.094838+00:00'
updated_at: '2023-04-10T20:24:28.458022+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[External Remote Services|T1133 - External Remote Services]]'
tags:
- '[[Boolean - Extract info (order by)]]'
- '[[SQLite Injection]]'
---

# SQLite Boolean-Based Order By Injection

## Summary

SQLite Boolean-Based Order By Injection is a technique used to extract sensitive information from a SQLite database. This technique takes advantage of the way SQLite handles the 'ORDER BY' clause. By injecting a boolean condition into the 'ORDER BY' clause, an attacker can extract information from 

## Description

# Description

SQLite Boolean-Based Order By Injection is a technique used to extract sensitive information from a SQLite database. This technique takes advantage of the way SQLite handles the 'ORDER BY' clause. By injecting a boolean condition into the 'ORDER BY' clause, an attacker can extract information from the database. This technique is commonly used to perform reconnaissance on a target system or to extract sensitive information such as usernames and passwords.

Technical Explanation: SQLite is a popular database engine used in many software applications. It is a lightweight, serverless database engine that stores data in a single file. SQLite injection is a technique used to exploit vulnerabilities in software applications that use SQLite as their database engine. The 'ORDER BY' clause is used to sort the results of a query. By injecting a boolean condition into the 'ORDER BY' clause, an attacker can extract information from the database.

Business Value: This technique can be used to extract sensitive information from a target system. This information can be used for further attacks or sold on the black market. By understanding how this technique works, organizations can take steps to secure their systems and prevent attackers from extracting sensitive information.

 

## Requirements

1. Access to a vulnerable application that uses SQLite as its database engine

 

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Regularly update and patch applications that use SQLite as their database engine

 

## Objectives

1. To extract sensitive information from a SQLite database

1. To perform reconnaissance on a target system

 

# Instructions

1. This command is used to determine which order element to use based on the table name. The command will check if the first character of the SQL statement for the table is equal to 'some_char'. If it is, <order_element_1> will be used as the order element, otherwise <order_element_2> will be used.

 



**Code**: [[CASE WHEN (SELECT hex(substr(sql,1,1)) FROM sqlite]]



> The 'CASE WHEN' statement is used to compare the first character of the SQL statement for the table with 'some_char'. If it is equal, <order_element_1> will be used. If not, <order_element_2> will be used. The 'SELECT hex(substr(sql,1,1))' statement is used to retrieve the first character of the SQL statement for the table in hexadecimal format. The 'FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0' statement is used to retrieve the SQL statement for the first table in the database that is not a system table. The 'hex' function is used to convert the first character of the SQL statement to hexadecimal format for comparison.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[External Remote Services|T1133 - External Remote Services]]

## Tags

- [[Boolean - Extract info (order by)]]
- [[SQLite Injection]]


