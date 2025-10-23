---
id: d7c187c3-76dc-419c-8470-bc5d6d9d4df2
name: MYSQL Union Based Injection to Extract Data from Users Table
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.330887+00:00'
updated_at: '2023-04-10T20:22:56.608758+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
tags:
- '[[Detect columns number]]'
- '[[MYSQL Injection]]'
- '[[MYSQL Union Based]]'
- '[[Using `order by` or `group by`]]'
- '[[Using `SELECT * FROM SOME_EXISTING_TABLE` Error Based]]'
---

# MYSQL Union Based Injection to Extract Data from Users Table

## Summary

MYSQL Union Based Injection is a technique used to extract data from a database by injecting malicious SQL code into an input field. This specific procedure focuses on extracting data from the Users table using the `UNION` operator. By detecting the number of columns in the table, the attacker can 

## Description

# Description

MYSQL Union Based Injection is a technique used to extract data from a database by injecting malicious SQL code into an input field. This specific procedure focuses on extracting data from the Users table using the `UNION` operator. By detecting the number of columns in the table, the attacker can craft a SQL statement to extract data from the Users table. The attacker can then use the `ORDER BY` or `GROUP BY` clauses to sort the data and extract specific information. This technique can be used to extract sensitive information such as usernames, passwords, and email addresses.

This procedure can be used by an attacker to gain unauthorized access to a system and steal sensitive information. The technical explanation involves injecting malicious SQL code into an input field to extract data from a database. The business value of this procedure is to highlight the importance of securing input fields and databases to prevent unauthorized access and data theft.

 

## Requirements

1. Access to an input field vulnerable to SQL Injection

1. Knowledge of MYSQL Union Based Injection

1. Knowledge of the database schema

 

## Defense

1. Implement input validation to prevent SQL Injection attacks

1. Use parameterized queries to prevent SQL Injection attacks

1. Monitor database logs for suspicious activity

 

## Objectives

1. Extract data from the Users table using MYSQL Union Based Injection

1. Sort the extracted data using `ORDER BY` or `GROUP BY` clauses

 

# Instructions

1. To extract data from the users table, an attacker can use SQL injection by injecting a query that selects all columns from the users table. This can be done by appending the payload 'AND (SELECT * FROM Users) = 1' to the original query. If the application is vulnerable to SQL injection, the server will respond with an error message that includes the data from the users table. The attacker can then parse the error message to extract the data.
Alternatively, the attacker can use the payload '-1' UNION SELECT 1,2,3--+' to retrieve data from the users table. This payload will return a result set with three columns, which can be used to extract data from the users table.

 



**Code**: [[1' AND (SELECT * FROM Users) = 1--+ 	#Operand shou]]



> The payload 'AND (SELECT * FROM Users) = 1' injects a query that selects all columns from the users table. The payload '-1' UNION SELECT 1,2,3--+' injects a query that returns a result set with three columns. The first column will contain the results from the original query, and the second and third columns will contain data from the users table. The double hyphen (--) at the end of the payload is used to comment out the rest of the original query and prevent any syntax errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Data Obfuscation|T1001 - Data Obfuscation]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

## Tags

- [[Detect columns number]]
- [[MYSQL Injection]]
- [[MYSQL Union Based]]
- [[Using `order by` or `group by`]]
- [[Using `SELECT * FROM SOME_EXISTING_TABLE` Error Based]]


