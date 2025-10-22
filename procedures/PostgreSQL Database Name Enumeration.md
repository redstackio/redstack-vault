---
id: abca4031-77b4-4a2a-9b89-e89c2cee1b61
name: PostgreSQL Database Name Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.636435+00:00'
updated_at: '2023-04-10T20:23:13.611193+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[PostgreSQL Database Name]]'
- '[[PostgreSQL injection]]'
commands:
- '[[Get current database name]]'
---

# PostgreSQL Database Name Enumeration

## Summary

PostgreSQL Database Name Enumeration is an attack technique that allows an attacker to extract the name of the current database from a PostgreSQL database server. This technique is achieved through injecting SQL queries into the database server, which can lead to unauthorized access to sensitive da

## Description

# Description

PostgreSQL Database Name Enumeration is an attack technique that allows an attacker to extract the name of the current database from a PostgreSQL database server. This technique is achieved through injecting SQL queries into the database server, which can lead to unauthorized access to sensitive data stored within the database. In order to execute this attack, the attacker must have prior knowledge of the database structure and the SQL syntax used by the database server.

Technical Explanation: An attacker can exploit a vulnerability in the database server to inject SQL queries that extract the name of the current database. This can be achieved through a variety of methods, including input validation errors or unsanitized user inputs. Once the attacker has extracted the name of the current database, they can use this information to launch further attacks against the database server.

Business Value: This technique can be used by attackers to gain access to sensitive data stored within a PostgreSQL database. This can lead to data theft, data manipulation, and other malicious activities that can harm a business's reputation and financial stability.

## Requirements

1. Access to the target network

1. Knowledge of PostgreSQL database structure and SQL syntax

## Defense

1. Ensure that all user inputs are properly validated and sanitized to prevent SQL injection attacks

1. Implement strong authentication mechanisms to prevent unauthorized access to the database server

1. Regularly monitor and audit database activity to detect and respond to any suspicious activity

## Objectives

1. Extract the name of the current database from a PostgreSQL database server

1. Gain unauthorized access to sensitive data stored within the database

# Instructions

1. This command retrieves the name of the current database being used.

**Code**: [[SELECT current_database()]]

> There are no arguments for this command. It simply executes the SQL function 'current_database()' which returns the name of the current database.

**Command** ([[Get current database name]]):

```bash
SELECT current_database()
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Get current database name]]

## Tags

- [[PostgreSQL Database Name]]
- [[PostgreSQL injection]]
