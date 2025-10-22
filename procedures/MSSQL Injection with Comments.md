---
id: 041b0839-cd3d-4b52-962e-44de4fc64206
name: MSSQL Injection with Comments
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.499757+00:00'
updated_at: '2023-04-10T20:22:43.012674+00:00'
tags:
- '[[MSSQL Comments]]'
- '[[MSSQL Injection]]'
---

# MSSQL Injection with Comments

## Summary

MSSQL Injection with Comments is a technique used by attackers to inject malicious SQL code into a MSSQL database. By adding comments to the injected SQL code, the attacker can evade detection by security tools and bypass authentication mechanisms. This technique allows the attacker to execute arbi

## Description

# Description

MSSQL Injection with Comments is a technique used by attackers to inject malicious SQL code into a MSSQL database. By adding comments to the injected SQL code, the attacker can evade detection by security tools and bypass authentication mechanisms. This technique allows the attacker to execute arbitrary SQL commands and potentially gain unauthorized access to sensitive data.

Technical Explanation: MSSQL Injection with Comments is achieved by adding comments to the SQL code injected into a MSSQL database. The comments help to obscure the malicious code and evade detection by security tools. The attacker can use this technique to execute arbitrary SQL commands and potentially gain unauthorized access to sensitive data.

Business Value: MSSQL Injection with Comments can be used by attackers to gain unauthorized access to sensitive data stored in MSSQL databases. This can result in financial loss, reputational damage, and legal liabilities for the affected organization.

## Requirements

1. Access to the target network

1. Access to a MSSQL database

1. Knowledge of SQL injection techniques

## Defense

1. Implement input validation and sanitization techniques to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Monitor MSSQL database logs for suspicious activity

## Objectives

1. Gain unauthorized access to a MSSQL database

1. Execute arbitrary SQL commands

# Instructions

1. Use this command to add comments to your SQL code.

**Code**: [[-- comment goes here
/* comment goes here */]]

> The 'data' field should contain the comment that you want to add to your SQL code. You can add single-line comments using '--' and multi-line comments using '/* */'. Comments are useful for explaining what your code does or for leaving notes for other developers who may be working on the same project.

## Tags

- [[MSSQL Comments]]
- [[MSSQL Injection]]
