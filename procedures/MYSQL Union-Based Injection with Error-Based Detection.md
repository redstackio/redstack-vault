---
id: 437e271e-ff91-4a92-b04e-99510349976d
name: MYSQL Union-Based Injection with Error-Based Detection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.307813+00:00'
updated_at: '2023-04-10T20:22:52.735582+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
tags:
- '[[Detect columns number]]'
- '[[MYSQL Injection]]'
- '[[MYSQL Union Based]]'
- '[[Using `order by` or `group by`]]'
- '[[Using `UNION SELECT` Error Based]]'
---

# MYSQL Union-Based Injection with Error-Based Detection

## Summary

MYSQL Union-Based Injection with Error-Based Detection is a technique used by attackers to gain unauthorized access to a MySQL database. This technique involves injecting malicious SQL code into a vulnerable web application to manipulate the database into returning data that the attacker is not aut

## Description

# Description

MYSQL Union-Based Injection with Error-Based Detection is a technique used by attackers to gain unauthorized access to a MySQL database. This technique involves injecting malicious SQL code into a vulnerable web application to manipulate the database into returning data that the attacker is not authorized to access. The attacker can use this technique to extract sensitive information such as usernames, passwords, and other confidential data.

Technical Explanation: This technique involves using a UNION SELECT statement to combine the results of two or more SELECT statements into a single result set. The attacker can use this technique to extract data from tables that they are not authorized to access. Error-based detection is used to identify the number of columns in the table and the type of data in each column.

Business Value: This technique can be used to compromise sensitive data such as customer information, financial data, and intellectual property. A successful MYSQL Union-Based Injection with Error-Based Detection attack can result in financial losses, reputational damage, and legal liabilities for the targeted organization.

## Requirements

1. Vulnerable web application with a MYSQL database

1. Knowledge of SQL injection techniques

1. Access to a tool for exploiting SQL injection vulnerabilities

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Monitor database logs for suspicious activity

## Objectives

1. Gain unauthorized access to a MySQL database

1. Extract sensitive information such as usernames, passwords, and other confidential data

# Instructions

1. To perform SQL Union-based Injection with Error-based Detection, follow these steps:
1. Identify a vulnerable parameter that is susceptible to SQL injection.
2. Use the 'UNION SELECT' statement to inject SQL code into the vulnerable parameter.
3. Use the '@' symbol to specify the number of columns in the original query.
4. Add additional '@' symbols to the 'UNION SELECT' statement until an error is generated.
5. Count the number of '@' symbols required to generate an error.
6. Use the correct number of '@' symbols in the 'UNION SELECT' statement to successfully inject SQL code without generating an error.
7. Verify the injection by checking for the expected output or by using additional SQL statements to extract data from the database.

**Code**: [[1' UNION SELECT @--+        #The used SELECT state]]

> The 'UNION SELECT' statement is used to combine the results of two or more SELECT statements into a single result set. In SQL injection attacks, this statement can be used to inject additional SQL code into a vulnerable parameter. By using the '@' symbol, the attacker can specify the number of columns in the original query. The attacker can then add additional '@' symbols to the 'UNION SELECT' statement until an error is generated. The number of '@' symbols required to generate an error indicates the number of columns in the original query. The attacker can then use the correct number of '@' symbols in the 'UNION SELECT' statement to successfully inject SQL code without generating an error. This method can be used to extract sensitive information from the database or to modify the contents of the database.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]

## Tags

- [[Detect columns number]]
- [[MYSQL Injection]]
- [[MYSQL Union Based]]
- [[Using `order by` or `group by`]]
- [[Using `UNION SELECT` Error Based]]
