---
id: 9ff78cbd-a43d-4088-b585-6139d1bf8eaf
name: DB2 Injection - Char to ASCII Conversion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.969921+00:00'
updated_at: '2023-04-10T20:22:04.455338+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Char -> ASCII Value]]'
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
commands:
- '[[ASCII value of character ''A'']]'
---

# DB2 Injection - Char to ASCII Conversion

## Summary

DB2 Injection is a technique used by attackers to exploit vulnerabilities in DB2 databases. One common method is through SQL Injection, where an attacker can inject malicious SQL code into a database query. In this particular scenario, the attacker is using the 'Char -> ASCII Value' method to conve

## Description

# Description

DB2 Injection is a technique used by attackers to exploit vulnerabilities in DB2 databases. One common method is through SQL Injection, where an attacker can inject malicious SQL code into a database query. In this particular scenario, the attacker is using the 'Char -> ASCII Value' method to convert characters to their corresponding ASCII values. This can be used to bypass input validation checks and execute unauthorized SQL queries. The business value of this attack is that an attacker can gain access to sensitive information stored in the database, such as customer data or financial records.

## Requirements

1. Access to the target database

1. Knowledge of SQL Injection techniques

1. Tools to perform SQL Injection attacks

## Defense

1. Implement input validation checks to prevent SQL Injection attacks

1. Use parameterized queries to avoid SQL Injection vulnerabilities

1. Monitor database activity for suspicious behavior

## Objectives

1. Execute unauthorized SQL queries

1. Gain access to sensitive information stored in the database

# Instructions

1. The ASCII function in SQL returns the ASCII code value of the leftmost character of a character expression. In this case, the character expression is 'A'. The function returns the integer value 65, which represents the ASCII code for the uppercase letter 'A'.

**Code**: [[select ascii('A') from sysibm.sysdummy1 -- returns]]

> The ASCII function is useful for converting character data into its corresponding ASCII code value. This can be particularly helpful when working with legacy systems that require ASCII data input. The function takes a single argument, which can be a character expression or a column name containing character data.

**Command** ([[ASCII value of character 'A']]):

```bash
select ascii('A') from sysibm.sysdummy1 -- returns 65
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[ASCII value of character 'A']]

## Tags

- [[Char -> ASCII Value]]
- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
