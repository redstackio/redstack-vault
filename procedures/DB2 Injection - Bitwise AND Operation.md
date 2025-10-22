---
id: d8123a56-610a-4f56-99c0-89b26f7dcff8
name: DB2 Injection - Bitwise AND Operation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.916510+00:00'
updated_at: '2023-04-10T20:21:59.413410+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Bitwise AND/OR/NOT/XOR]]'
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
commands:
- '[[Perform bit operation]]'
---

# DB2 Injection - Bitwise AND Operation

## Summary

DB2 Injection is a type of SQL injection that targets IBM DB2 databases. By leveraging Bitwise AND Operation, an attacker can manipulate the SQL query to return data that they should not have access to. This technique allows the attacker to bypass authentication and authorization checks, and gain a

## Description

# Description

DB2 Injection is a type of SQL injection that targets IBM DB2 databases. By leveraging Bitwise AND Operation, an attacker can manipulate the SQL query to return data that they should not have access to. This technique allows the attacker to bypass authentication and authorization checks, and gain access to sensitive data. 

Bitwise AND Operation is a binary operation that takes two equal-length binary representations and performs the logical AND operation on each pair of corresponding bits. This operation returns a binary value where each bit is 1 only if both bits in the corresponding positions of the binary inputs are 1. 

This technique can be used by attackers to extract sensitive information from databases, such as usernames, passwords, and other confidential data.

## Requirements

1. Access to a vulnerable DB2 database

1. Knowledge of SQL Injection techniques

1. Tools such as SQLmap or manually crafted SQL queries

## Defense

1. Input validation and sanitization of user-supplied data can help prevent SQL injection attacks

1. Using parameterized queries can help prevent SQL injection attacks

1. Implementing proper authentication and authorization checks can limit the impact of successful SQL injection attacks

## Objectives

1. Extract sensitive information from DB2 databases

1. Bypass authentication and authorization checks

# Instructions

1. The Bitwise AND operation is used to compare two binary numbers bit by bit. It returns a value where each bit is set to 1 only if both corresponding bits in the input numbers are 1, otherwise the bit is set to 0. The bitand function in SQL is used to perform the Bitwise AND operation. The syntax for the function is: bitand(num1, num2), where num1 and num2 are the two binary numbers to be compared.

**Code**: [[select bitand(1,0) from sysibm.sysdummy1 -- return]]

> In the given example, the bitand function is used to compare the binary numbers 1 and 0. Since the corresponding bits in the two numbers are not both 1, the function returns 0. The same function can also be used with other operators like bitandnot, bitor, bitxor and bitnot to perform other Bitwise operations.

**Command** ([[Perform bit operation]]):

```bash
select bitand(1,0) from sysibm.sysdummy1
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Perform bit operation]]

## Tags

- [[Bitwise AND/OR/NOT/XOR]]
- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
