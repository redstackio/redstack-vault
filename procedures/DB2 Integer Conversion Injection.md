---
id: a05a105b-1fb6-4de4-a86e-f1af0cf9c9fa
name: DB2 Integer Conversion Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.996648+00:00'
updated_at: '2023-04-10T20:22:03.010238+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Casting]]'
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
commands:
- '[[Convert integer to string]]'
- '[[Convert string to integer]]'
---

# DB2 Integer Conversion Injection

## Summary

DB2 Integer Conversion Injection is a type of SQL injection attack that exploits vulnerabilities in the way DB2 handles integer conversion. By injecting specially crafted input, an attacker can manipulate the database to execute arbitrary SQL commands, potentially gaining access to sensitive data o

## Description

# Description

DB2 Integer Conversion Injection is a type of SQL injection attack that exploits vulnerabilities in the way DB2 handles integer conversion. By injecting specially crafted input, an attacker can manipulate the database to execute arbitrary SQL commands, potentially gaining access to sensitive data or taking control of the system. This technique involves casting input to an integer data type, allowing the attacker to bypass input validation and execute malicious code.

## Requirements

1. Access to the DB2 database

1. Knowledge of the database schema and structure

1. A tool capable of performing SQL injection attacks

## Defense

1. Implement input validation and sanitization techniques to prevent injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Regularly update and patch the DB2 system to address known vulnerabilities

## Objectives

1. Gain unauthorized access to sensitive data stored in the DB2 database

1. Execute arbitrary SQL commands on the DB2 database

1. Take control of the DB2 system

# Instructions

1. The 'cast' function is used to convert the data type of a column or an expression to a specified data type. In this case, the first 'select' statement is converting the string '123' to an integer data type. The second 'select' statement is converting the integer value 1 to a character data type.

**Code**: [[select cast('123' as integer) from sysibm.sysdummy]]

> The 'cast' function takes two arguments: the column or expression to be converted and the target data type. In this example, the first argument is the string '123' and the target data type is 'integer'. The second argument is the integer value 1 and the target data type is 'char'.

**Command** ([[Convert string to integer]]):

```bash
select cast('123' as integer) from sysibm.sysdummy1
```

**Command** ([[Convert integer to string]]):

```bash
select cast(1 as char) from sysibm.sysdummy1
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Convert integer to string]]
- [[Convert string to integer]]

## Tags

- [[Casting]]
- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
