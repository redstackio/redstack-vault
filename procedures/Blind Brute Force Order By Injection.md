---
id: f6face3a-f8e9-4629-86b4-a2ca17ae0213
name: Blind Brute Force Order By Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.575120+00:00'
updated_at: '2023-04-10T20:22:58.344088+00:00'
tags:
- '[[MYSQL Blind]]'
- '[[MySQL Blind SQL Injection in ORDER BY clause using a binary query and REGEXP]]'
- '[[MYSQL Injection]]'
---

# Blind Brute Force Order By Injection

## Summary

Blind Brute Force Order By Injection is a technique used to exploit MySQL Blind SQL Injection vulnerabilities in the ORDER BY clause of a SQL query. This technique involves using a binary query and REGEXP to brute force the values in the ORDER BY clause. The attacker can then use this technique to 

## Description

# Description

Blind Brute Force Order By Injection is a technique used to exploit MySQL Blind SQL Injection vulnerabilities in the ORDER BY clause of a SQL query. This technique involves using a binary query and REGEXP to brute force the values in the ORDER BY clause. The attacker can then use this technique to extract sensitive information from the database without being detected.

 

## Requirements

1. Access to a vulnerable application with a MySQL database

1. Knowledge of SQL syntax

1. Tools like SQLMap or manual exploitation

 

## Defense

1. Use prepared statements to prevent SQL injection attacks

1. Limit database user permissions to only necessary actions

1. Regularly update and patch the application and database software to prevent known vulnerabilities

 

## Objectives

1. To extract sensitive information from the database

 

# Instructions

1. To use this command, replace [COLUMN] with the column you want to bruteforce, [TABLE] with the table name, [BRUTEFORCE CHAR BY CHAR] with the characters you want to bruteforce, [FURTHER OPTIONS / CONDITIONS] with any additional conditions, [ONE COLUMN TO ORDER BY] with the column to order by if the REGEXP query matches, and [ANOTHER COLUMN TO ORDER BY] with the column to order by if the REGEXP query does not match.

 

This command can be used to extract data from a database by bruteforcing values character by character. By using the REGEXP query, you can check if a certain character is present in the value of the specified column. If the character is present, the EXISTS() function will return a 1 and the query will order by the first specified column. If the character is not present, the EXISTS() function will return a 0 and the query will order by the second specified column. This allows you to extract data from the database without direct output, making it a useful tool for SQL injection attacks.

## Tags

- [[MYSQL Blind]]
- [[MySQL Blind SQL Injection in ORDER BY clause using a binary query and REGEXP]]
- [[MYSQL Injection]]


