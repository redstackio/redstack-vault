---
id: 7b9e1adf-57f4-40e3-9bc2-dbd1d45f5c0c
name: PostgreSQL Version Retrieval via Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.424813+00:00'
updated_at: '2023-04-10T20:23:21.047050+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[PostgreSQL injection]]'
- '[[PostgreSQL Version]]'
commands:
- '[[MySQL Version]]'
---

# PostgreSQL Version Retrieval via Injection

## Summary

PostgreSQL is a popular open-source relational database management system. Attackers can leverage SQL injection vulnerabilities to retrieve sensitive information from a PostgreSQL database, including the version number. By exploiting a vulnerability in a public-facing application, an attacker can e

## Description

# Description

PostgreSQL is a popular open-source relational database management system. Attackers can leverage SQL injection vulnerabilities to retrieve sensitive information from a PostgreSQL database, including the version number. By exploiting a vulnerability in a public-facing application, an attacker can execute arbitrary SQL queries and extract the version number of the database. This information can be used to identify vulnerabilities in the database and plan further attacks to gain access to sensitive data. 

To retrieve the PostgreSQL version, the attacker can use the 'SELECT version()' command in the SQL injection payload. This command returns the version number of the database. 

Business Value: By identifying vulnerabilities in the database, organizations can take steps to secure their systems and prevent data breaches. This procedure can be used to test the security of PostgreSQL databases and ensure that they are properly secured against SQL injection attacks.

## Requirements

1. Access to a vulnerable public-facing application with a SQL injection vulnerability

## Defense

1. Ensure that all public-facing applications are properly secured and tested for vulnerabilities

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Monitor database activity for suspicious behavior and unauthorized access

## Objectives

1. Retrieve the version number of the PostgreSQL database

# Instructions

1. This command retrieves the version of the MySQL database currently in use.

**Code**: [[SELECT version()]]

> The SELECT statement is used to retrieve the version of the MySQL database currently in use. The version() function is a built-in function in MySQL that returns the version of the MySQL database currently in use. No arguments are required for this function.

**Command** ([[MySQL Version]]):

```bash
SELECT version()
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[MySQL Version]]

## Tags

- [[PostgreSQL injection]]
- [[PostgreSQL Version]]
