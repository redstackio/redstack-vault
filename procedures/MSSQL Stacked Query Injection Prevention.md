---
id: e3067bfb-0c3d-4f09-8830-e4ec80133dfd
name: MSSQL Stacked Query Injection Prevention
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.895774+00:00'
updated_at: '2023-04-10T20:22:45.653938+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[MSSQL Injection]]'
- '[[MSSQL Stacked Query]]'
---

# MSSQL Stacked Query Injection Prevention

## Summary

MSSQL Stacked Query Injection is a technique used to execute multiple queries in a single SQL statement. This technique can be used by attackers to modify, delete or extract data from a database. In order to prevent MSSQL Stacked Query Injection, it is important to validate and sanitize all user in

## Description

# Description

MSSQL Stacked Query Injection is a technique used to execute multiple queries in a single SQL statement. This technique can be used by attackers to modify, delete or extract data from a database. In order to prevent MSSQL Stacked Query Injection, it is important to validate and sanitize all user input, especially those that are used in SQL statements. Additionally, using parameterized queries can help to prevent this type of attack. By implementing these measures, organizations can protect their databases from unauthorized access and modification, ensuring the confidentiality, integrity, and availability of their data.

## Requirements

1. Access to the database server

1. Ability to modify database configurations

1. Knowledge of SQL syntax and query construction

## Defense

1. Implement input validation and sanitization to prevent injection attacks

1. Use parameterized queries to prevent stacked query injection

1. Implement least privilege access control to limit the impact of a successful attack

## Objectives

1. Prevent unauthorized access to sensitive data

1. Ensure the integrity of the database

1. Maintain the availability of the database

# Instructions

1. When constructing SQL queries, always use parameterized statements and avoid concatenating user-supplied data into the query. This will prevent SQL injection attacks.

**Code**: [[ProductID=1; DROP members--]]

> SQL injection is a type of attack where an attacker can inject malicious SQL statements into an entry field for execution by the database. This can lead to unauthorized access to sensitive data, data corruption, or even complete system compromise. One way to prevent SQL injection is to use parameterized statements, which separate the SQL code from the user input. Another way is to sanitize the user input by removing any characters that could be interpreted as SQL code.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[MSSQL Injection]]
- [[MSSQL Stacked Query]]
