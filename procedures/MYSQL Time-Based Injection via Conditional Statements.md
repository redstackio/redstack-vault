---
id: e0d271b6-8f59-4172-bac1-c66992976341
name: MYSQL Time-Based Injection via Conditional Statements
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.723433+00:00'
updated_at: '2023-04-10T20:22:49.424137+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[MYSQL Injection]]'
- '[[MYSQL Time Based]]'
- '[[Using conditional statements]]'
---

# MYSQL Time-Based Injection via Conditional Statements

## Summary

This procedure involves exploiting a MYSQL database by injecting malicious code into a SQL statement. By using time-based blind attacks, an attacker can infer the existence of data and extract sensitive information. This technique involves the use of conditional statements to delay the response of 

## Description

# Description

This procedure involves exploiting a MYSQL database by injecting malicious code into a SQL statement. By using time-based blind attacks, an attacker can infer the existence of data and extract sensitive information. This technique involves the use of conditional statements to delay the response of the database, allowing the attacker to obtain information about the data structure and the values stored within. This procedure can be used to gain access to sensitive information such as usernames, passwords, and other confidential data.

 

## Requirements

1. Access to the MYSQL database

1. Knowledge of SQL injection techniques

1. Tools such as SQLMap or similar SQL injection tools

 

## Defense

1. Implement input validation and sanitization techniques to prevent SQL injection attacks

1. Use parameterized queries to prevent the execution of malicious SQL statements

1. Regularly update the MYSQL database software to patch known vulnerabilities

 

## Objectives

1. Gain unauthorized access to sensitive information stored in the MYSQL database

1. Extract data from the database using time-based blind attacks

1. Identify vulnerabilities in the database and exploit them for malicious purposes

 

# Instructions

1. This command is used for SQL injection attacks via time-based blind attack. The attacker can use this command to perform a time-based attack to extract sensitive information from a database. The command uses a variety of techniques such as BENCHMARK and SLEEP to delay the response of the server and extract information based on the time delay. The attacker can modify the command to extract specific information from the database.

 



**Code**: [[?id=1 AND IF(ASCII(SUBSTRING((SELECT USER()),1,1))]]



> The 'data' field of the command contains the SQL injection payload. The 'id' parameter in the payload is vulnerable to SQL injection. The payload uses the 'IF' function to check if the ASCII value of the first character of the user is greater than or equal to 100. If the condition is true, the 'BENCHMARK' function is executed with a delay of 2 seconds. If the condition is false, the 'SLEEP' function is executed with a delay of 3 seconds. The attacker can modify the payload to extract specific information from the database.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Tags

- [[MYSQL Injection]]
- [[MYSQL Time Based]]
- [[Using conditional statements]]


