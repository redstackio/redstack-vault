---
id: f963d9e5-2f5b-4f2b-982c-87a6524f06d5
name: MYSQL Blind with Substring Equivalent Version and Schema Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.557722+00:00'
updated_at: '2023-04-10T20:22:56.965049+00:00'
tags:
- '[[MYSQL Blind]]'
- '[[MYSQL Blind with substring equivalent]]'
- '[[MYSQL Injection]]'
---

# MYSQL Blind with Substring Equivalent Version and Schema Extraction

## Summary

MYSQL Blind with Substring Equivalent Version and Schema Extraction is a technique used by attackers to extract information from a MYSQL database without being detected. This technique involves injecting malicious code into a MYSQL query that allows the attacker to extract the version and schema of

## Description

# Description

MYSQL Blind with Substring Equivalent Version and Schema Extraction is a technique used by attackers to extract information from a MYSQL database without being detected. This technique involves injecting malicious code into a MYSQL query that allows the attacker to extract the version and schema of the database. This technique is often used to gain access to sensitive information such as usernames and passwords.

Technical Explanation: MYSQL Blind with Substring Equivalent is a technique that allows attackers to infer information about the database by sending specially crafted requests to the server. By analyzing the server's response, the attacker can deduce the contents of the database. This technique is often used when the attacker does not have direct access to the database but can still send requests to the server.

Business Value: This technique can be used to gain access to sensitive information such as usernames and passwords. Attackers can use this information to gain access to other systems and networks that use the same credentials. This technique can also be used to gather information about the target's infrastructure, which can be used for future attacks.

## Requirements

1. Access to the target's MYSQL database

1. Knowledge of MYSQL Blind with Substring Equivalent technique

1. Ability to inject malicious code into a MYSQL query

## Defense

1. Implement input validation techniques to prevent MYSQL injection attacks

1. Use parameterized queries to prevent MYSQL injection attacks

1. Monitor MYSQL logs for suspicious activity

## Objectives

1. Extract the version and schema of the MYSQL database

1. Gain access to sensitive information such as usernames and passwords

1. Gather information about the target's infrastructure

# Instructions

1. This command is used to extract the version and schema of a MySQL database. It uses various SQL injection techniques to extract the information.

**Code**: [[?id=1 and substring(version(),1,1)=5
?id=1 and rig]]

> The 'version()' function returns the version of the MySQL database. The 'substring()' function is used to extract the first character of the version number. The 'right()' and 'left()' functions are used to extract the first and second characters of the version number respectively. The 'ascii()' function is used to convert the first character of the version number to its ASCII value. The 'mid()' function is used to extract the first character of the version number. The 'SELECT' statement is used to retrieve information from the 'information_schema' database. The 'SUBSTR()' function is used to extract the first character of the table and column names. The '>' operator is used to compare the ASCII value of the first character of the table and column names with the ASCII value of 'A'.

## Tags

- [[MYSQL Blind]]
- [[MYSQL Blind with substring equivalent]]
- [[MYSQL Injection]]
