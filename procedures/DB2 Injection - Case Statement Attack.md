---
id: b8dfa4c0-a458-4372-908e-92edbdf32be8
name: DB2 Injection - Case Statement Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.051189+00:00'
updated_at: '2023-04-10T20:22:00.470585+00:00'
tags:
- '[[Case Statement]]'
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
---

# DB2 Injection - Case Statement Attack

## Summary

DB2 injection is a type of attack that targets IBM's relational database management system. The case statement attack is a technique that can be used to extract sensitive information from a database. Attackers can use the case statement to test multiple conditions and return specific results based 

## Description

# Description

DB2 injection is a type of attack that targets IBM's relational database management system. The case statement attack is a technique that can be used to extract sensitive information from a database. Attackers can use the case statement to test multiple conditions and return specific results based on the outcome. This technique can be used to bypass authentication mechanisms or extract data that is not normally accessible. 

Technical Explanation: The case statement is a conditional statement that evaluates a set of conditions and returns a specific result based on the outcome. In a DB2 database, the case statement can be used to test for specific values in a table and return the associated data. Attackers can use this technique to extract sensitive information from the database by crafting input that will cause the case statement to return the desired data. 

Business Value: DB2 injection attacks can result in the theft of sensitive information, such as customer data, financial information, and intellectual property. This can lead to reputational damage, financial losses, and legal liabilities for affected organizations.

## Requirements

1. Access to the DB2 database

1. Knowledge of SQL injection techniques

## Defense

1. Implement input validation and parameterization to prevent SQL injection attacks

1. Use prepared statements to prevent SQL injection attacks

1. Regularly monitor the database for unusual activity and suspicious queries

## Objectives

1. Extract sensitive information from a DB2 database

1. Bypass authentication mechanisms

# Instructions

1. This command is used to perform a conditional selection based on a specified condition. The SELECT statement is used to retrieve data from one or more tables. The CASE statement is used to evaluate multiple conditions and return a value based on the first condition that is true. The WHEN keyword is used to specify the condition to be evaluated, and the THEN keyword is used to specify the value to be returned if the condition is true. The ELSE keyword is used to specify the value to be returned if none of the conditions are true.

**Code**: [[select CASE WHEN (1=1) THEN 'AAAAAAAAAA' ELSE 'BBB]]

> The data field in this command contains an example SQL statement that demonstrates the usage of the CASE statement. In this example, the CASE statement is used to check if the condition (1=1) is true. If it is true, the value 'AAAAAAAAAA' is returned. If it is false, the value 'BBBBBBBBBB' is returned. The lang field specifies the language used in this command, which is SQL. The text field provides additional information about the usage of this command. The instruction field provides step-by-step instructions on how to use this command. The explain field provides a brief explanation of the purpose and functionality of this command.

## Tags

- [[Case Statement]]
- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
