---
id: dbc80215-82db-430b-88fb-f8ada0167794
name: Google BigQuery Error-Based SQL Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.399964+00:00'
updated_at: '2023-04-10T20:21:06.079085+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[BigQuery Error Based]]'
- '[[Google BigQuery SQL Injection]]'
---

# Google BigQuery Error-Based SQL Injection

## Summary

Google BigQuery is a cloud-based data warehouse that allows users to analyze large amounts of data using SQL queries. However, if not properly secured, it can be vulnerable to SQL injection attacks. Error-based SQL injection is a technique where an attacker injects SQL code into a query to cause th

## Description

# Description

Google BigQuery is a cloud-based data warehouse that allows users to analyze large amounts of data using SQL queries. However, if not properly secured, it can be vulnerable to SQL injection attacks. Error-based SQL injection is a technique where an attacker injects SQL code into a query to cause the database to generate an error message that reveals information about the database schema or data. This can be used to extract sensitive information or even gain remote code execution.

From an offensive perspective, an attacker can use error-based SQL injection to extract sensitive information from a BigQuery database, such as usernames, passwords, and other credentials. This can then be used to gain access to other systems or escalate privileges. From a defensive perspective, it is important to properly secure BigQuery instances to prevent SQL injection attacks.

Business value: By securing BigQuery instances, organizations can prevent data breaches and protect sensitive information from being stolen or leaked.

 

## Requirements

1. Access to a vulnerable BigQuery instance

1. Knowledge of SQL injection techniques

 

## Defense

1. Properly secure BigQuery instances to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection

1. Monitor BigQuery logs for suspicious activity

 

## Objectives

1. Extract sensitive information from a BigQuery database

1. Gain access to other systems or escalate privileges

 

# Instructions

1. To perform an error-based SQL injection, the attacker injects code that will cause an error in the SQL statement, revealing information about the database. In this example, the attacker is trying to find the length of a string by dividing by zero. If the division by zero causes an error message to be displayed, the attacker knows that the string length is 1. The attacker can also use casting to reveal information about the database, as shown in the second example.

 



**Code**: [[# Error based - division by zero
' OR if(1/(length]]



> The attacker can use this technique to extract sensitive information from the database, such as usernames and passwords. It is important to sanitize user input to prevent SQL injection attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[BigQuery Error Based]]
- [[Google BigQuery SQL Injection]]


