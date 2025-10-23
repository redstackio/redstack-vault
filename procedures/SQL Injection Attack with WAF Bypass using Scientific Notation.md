---
id: 9c89eb6b-f888-48b5-b626-0ce9e2e826cd
name: SQL Injection Attack with WAF Bypass using Scientific Notation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.885217+00:00'
updated_at: '2023-04-10T20:24:23.204243+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[More MySQL specific]]'
- '[[SQL Injection]]'
- '[[WAF Bypass]]'
- '[[WAF bypass for MySQL using scientific notation]]'
---

# SQL Injection Attack with WAF Bypass using Scientific Notation

## Summary

SQL Injection is a common technique used by attackers to exploit vulnerabilities in web applications. By injecting malicious SQL code into a vulnerable application, attackers can bypass authentication mechanisms and gain access to sensitive data. In this specific attack, the attacker uses a techniq

## Description

# Description

SQL Injection is a common technique used by attackers to exploit vulnerabilities in web applications. By injecting malicious SQL code into a vulnerable application, attackers can bypass authentication mechanisms and gain access to sensitive data. In this specific attack, the attacker uses a technique called scientific notation to bypass a Web Application Firewall (WAF) and extract password data from a MySQL database. Scientific notation is a technique that converts numbers into a shorter format using exponent notation. By using scientific notation in the SQL injection attack, the attacker can bypass the WAF and extract password data from the database.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of SQL Injection techniques

1. Knowledge of scientific notation

 

## Defense

1. Ensure that all web applications are properly patched and up to date to prevent SQL Injection attacks

1. Implement a WAF that can detect and prevent SQL Injection attacks

1. Regularly monitor and analyze web traffic to detect any suspicious activity

 

## Objectives

1. Bypass the WAF to gain access to the MySQL database

1. Extract password data from the MySQL database

 

# Instructions

1. SQL Injection Attack

 



**Code**: [[' or ''=']]



> SQL Injection is a type of attack where an attacker tries to insert malicious SQL code into a database, which can then be used to steal data, modify data, or even delete data. The attacker typically tries to exploit vulnerabilities in the application's input validation, such as using single quotes or other special characters to break out of a query and execute their own code. To prevent SQL Injection attacks, it is important to use prepared statements, input validation, and other security best practices.

2. To perform a SQL injection attack, an attacker attempts to inject malicious SQL code into a vulnerable web application's database. This can be done by inserting SQL code into input fields that are not properly validated or sanitized. The injected SQL code can then be used to manipulate the database or extract sensitive information.

 



**Code**: [[' or 1.e('')=']]



> The 'data' field contains the malicious SQL code that is being injected into the vulnerable web application. The 'lang' field specifies that the code is written in SQL. The 'text' field indicates that the attack was successful. The 'instruction' field provides a brief overview of how the attack is performed. The 'explain' field provides more detail about what a SQL injection attack is and how it works.

3. This command is used to extract the password from the 'users' table in a SQL database. The 'select' command is used to retrieve the password field from the 'users' table. The 'limit' command is used to limit the result set to one row. The 'substring' command is used to extract a single character from the password. The 'ascii' command is used to obtain the ASCII value of the character. The 'or' condition is used to bypass any authentication checks.

 



**Code**: [[1.e(ascii 1.e(substring(1.e(select password from u]]



> The '1.e' string is used to obfuscate the query and bypass any input validation checks. The 'substring' command is used to extract a single character from the password field. The 'ascii' command is used to obtain the ASCII value of the character. The obtained value is compared to 70 which is the ASCII value of 'F'. If the comparison is true, the password extraction is successful. The 'or' condition is used to bypass any authentication checks and return the password regardless of the input provided.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[More MySQL specific]]
- [[SQL Injection]]
- [[WAF Bypass]]
- [[WAF bypass for MySQL using scientific notation]]


