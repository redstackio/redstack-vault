---
id: 8b39a576-7639-4754-8aa6-5ca26229041b
name: BigQuery SQL Injection Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.424053+00:00'
updated_at: '2023-04-10T20:21:05.151809+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Application Window Discovery|T1010 - Application Window Discovery]]'
- '[[Data Staged|T1074 - Data Staged]]'
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
tags:
- '[[BigQuery Boolean Based]]'
- '[[Google BigQuery SQL Injection]]'
---

# BigQuery SQL Injection Attack

## Summary

A SQL injection attack on Google BigQuery can allow an attacker to access sensitive data, escalate privileges, and gain unauthorized access to the system. The attack can be performed through a Boolean-based injection technique, which involves modifying the SQL query to return a true or false value.

## Description

# Description

A SQL injection attack on Google BigQuery can allow an attacker to access sensitive data, escalate privileges, and gain unauthorized access to the system. The attack can be performed through a Boolean-based injection technique, which involves modifying the SQL query to return a true or false value. This technique is commonly used when the attacker has limited knowledge of the database structure and is unable to perform a more complex attack. The business value of this attack is that it can compromise the confidentiality, integrity, and availability of the data stored in the BigQuery system.

 

## Requirements

1. Access to the BigQuery system

1. Knowledge of SQL injection techniques

1. Ability to modify SQL queries

 

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Limit access to the BigQuery system to authorized personnel only

 

## Objectives

1. Gain unauthorized access to sensitive data stored in the BigQuery system

1. Escalate privileges to gain more control over the system

1. Compromise the confidentiality, integrity, and availability of the data

 

# Instructions

1. This command is used to perform a SQL injection attack. The injected code is designed to extract the first letter of the first column name from the specified table. The '#' symbol is used to comment out the rest of the injected code. The command can be modified to extract different information from the database.

 



**Code**: [[' WHERE SUBSTRING((select column_name from `projec]]



> The 'WHERE' clause in SQL is used to filter data based on a specified condition. In this command, the condition is designed to always be true by injecting a code that extracts a specific piece of information. The 'SUBSTRING' function is used to extract a substring from a specified string. In this case, it extracts the first letter of the column name. The 'LIMIT' clause is used to limit the number of rows returned by the query. The injected code is enclosed in single quotes to indicate that it is a string. The '#' symbol is used to comment out the rest of the injected code.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Application Window Discovery|T1010 - Application Window Discovery]]
- [[Data Staged|T1074 - Data Staged]]
- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]

## Tags

- [[BigQuery Boolean Based]]
- [[Google BigQuery SQL Injection]]


