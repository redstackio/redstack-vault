---
id: 3a64b1c3-2d9f-4463-be91-208d41e0cd56
name: MySQL Blind SQL Injection using REGEXP
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.590604+00:00'
updated_at: '2023-04-10T20:22:55.212108+00:00'
tags:
- '[[MYSQL Blind]]'
- '[[MySQL Blind SQL Injection binary query using REGEXP.]]'
- '[[MYSQL Injection]]'
---

# MySQL Blind SQL Injection using REGEXP

## Summary

MySQL Blind SQL Injection binary query using REGEXP is a technique used by attackers to bypass security measures put in place to prevent SQL injection attacks. This technique is used to extract sensitive data from a database by injecting malicious SQL queries into a vulnerable application. The atta

## Description

# Description

MySQL Blind SQL Injection binary query using REGEXP is a technique used by attackers to bypass security measures put in place to prevent SQL injection attacks. This technique is used to extract sensitive data from a database by injecting malicious SQL queries into a vulnerable application. The attacker can use this technique to extract data from the database without knowing the exact structure of the database. This technique is particularly useful when the attacker has limited access to the database and cannot execute arbitrary commands.

Technical Explanation: The attacker uses the 'REGEXP' function in MySQL to extract data from the database. This function is used to search for a pattern in a string. The attacker injects a 'REGEXP' function into a vulnerable application to extract data from the database. The attacker can use this technique to extract data from the database without knowing the exact structure of the database.

Business Value: This technique is used by attackers to extract sensitive data from a database. The stolen data can be used for various purposes, such as identity theft, financial fraud, and corporate espionage.

 

## Requirements

1. Access to a vulnerable application

1. Knowledge of SQL injection techniques

 

## Defense

1. Input validation and sanitization should be performed on all user input to prevent SQL injection attacks

1. Database access should be restricted to only authorized users

1. Regular security audits should be conducted to identify and fix vulnerabilities in the system

 

## Objectives

1. Extract sensitive data from a database

1. Bypass security measures put in place to prevent SQL injection attacks

 

# Instructions

1. This payload can be used to test SQL injection vulnerabilities in web applications. The payload uses a SQL injection technique called 'time-based blind SQL injection'. This technique relies on the database server taking a longer time to respond to certain queries, allowing an attacker to infer information about the database.

 

In this specific payload, the attacker is trying to determine if there is a record in the 'items' table whose name starts with the letter 'a'. The 'REGEXP "^a.*"' part of the query checks if the name starts with 'a', and the 'EXISTS' function returns true if there is at least one record that matches the condition. If the condition is true, the 'SLEEP(3)' function causes the database server to delay the response by 3 seconds. Otherwise, the query executes normally and the response is returned immediately. The final part of the payload is a comment that comments out the rest of the original query, preventing any errors caused by the injected code.

2. This command is used to exploit a SQL injection vulnerability by causing a delay in the response of the database. The injection point is in the "where" clause of the query. The injection point can be used to execute arbitrary SQL commands.

 

The command works by injecting SQL code into the query, causing the database to execute the injected code. The injected code checks if there is a name in the items table that starts with the letter "a". If there is, the command causes the database to sleep for 3 seconds before returning a response. This delay can be used to determine if the injection was successful and to gather information about the database. The injection point can be used to execute arbitrary SQL commands, such as reading or modifying data in the database.

## Tags

- [[MYSQL Blind]]
- [[MySQL Blind SQL Injection binary query using REGEXP.]]
- [[MYSQL Injection]]


