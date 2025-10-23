---
id: d4b62d1b-9413-4876-ab3b-ead19477e9c6
name: MYSQL Injection with Blind MAKE_SET
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.630027+00:00'
updated_at: '2023-04-10T20:22:58.710835+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[MYSQL Blind]]'
- '[[MYSQL Blind with MAKE_SET]]'
- '[[MYSQL Injection]]'
---

# MYSQL Injection with Blind MAKE_SET

## Summary

MYSQL Injection with Blind MAKE_SET is a technique used by attackers to bypass user authentication in MYSQL databases. This technique involves injecting malicious SQL code into a vulnerable application to gain unauthorized access to sensitive data. The MAKE_SET function is used to perform a blind S

## Description

# Description

MYSQL Injection with Blind MAKE_SET is a technique used by attackers to bypass user authentication in MYSQL databases. This technique involves injecting malicious SQL code into a vulnerable application to gain unauthorized access to sensitive data. The MAKE_SET function is used to perform a blind SQL injection attack, where the attacker can infer the results of their queries based on the application's response.

From a technical standpoint, the attacker uses the SQL Injection Command for User Authentication Bypass to inject malicious code into the application's login form. The MAKE_SET function is used to create a bit field with one or more bits set, which is then used to infer the results of the attacker's queries based on the application's response. This technique can be used to bypass user authentication and gain access to sensitive data stored in the database.

From a business perspective, MYSQL Injection with Blind MAKE_SET can result in unauthorized access to sensitive data, which can lead to data theft, financial loss, and reputational damage.

 

## Requirements

1. Access to a vulnerable application

1. Knowledge of SQL Injection techniques

1. Knowledge of the MAKE_SET function

 

## Defense

1. Ensure that all user input is properly sanitized and validated to prevent SQL Injection attacks

1. Implement strict access controls to limit access to sensitive data

1. Regularly monitor database logs for suspicious activity

 

## Objectives

1. Bypass user authentication in MYSQL databases

1. Gain unauthorized access to sensitive data

 

# Instructions

1. This command is used for bypassing user authentication in SQL injection attacks. It takes advantage of the fact that an SQL query can be manipulated to execute arbitrary commands. The command uses the MAKE_SET() function to compare the result of a subquery with a hardcoded value of 1. If the result of the subquery is less than 1, the comparison returns true and the injected code is executed. The injected code consists of two subqueries, one to determine the length of the version string and another to determine the length of the concatenated login and password strings. The code then uses the ASCII() function to extract individual characters from the version and login/password strings, one at a time, until it has extracted all of the characters.

 



**Code**: [[AND MAKE_SET(YOLO<(SELECT(length(version()))),1)
A]]



> This command is used to bypass user authentication in SQL injection attacks. It works by injecting code into an SQL query that executes arbitrary commands. The injected code uses the MAKE_SET() function to compare the result of a subquery with a hardcoded value of 1. If the result of the subquery is less than 1, the comparison returns true and the injected code is executed. The injected code consists of two subqueries, one to determine the length of the version string and another to determine the length of the concatenated login and password strings. The code then uses the ASCII() function to extract individual characters from the version and login/password strings, one at a time, until it has extracted all of the characters.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[MYSQL Blind]]
- [[MYSQL Blind with MAKE_SET]]
- [[MYSQL Injection]]


