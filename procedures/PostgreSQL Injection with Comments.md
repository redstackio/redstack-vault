---
id: 2f9fe46e-f4a7-44ef-a007-724c45a6a530
name: PostgreSQL Injection with Comments
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.373645+00:00'
updated_at: '2023-04-10T20:23:19.149902+00:00'
tags:
- '[[PostgreSQL Comments]]'
- '[[PostgreSQL injection]]'
---

# PostgreSQL Injection with Comments

## Summary

PostgreSQL is an open-source relational database management system that is widely used in web applications. One of the most common vulnerabilities in web applications is SQL injection. An attacker can exploit SQL injection vulnerabilities to execute arbitrary SQL commands, which can lead to data th

## Description

# Description

PostgreSQL is an open-source relational database management system that is widely used in web applications. One of the most common vulnerabilities in web applications is SQL injection. An attacker can exploit SQL injection vulnerabilities to execute arbitrary SQL commands, which can lead to data theft, data corruption, and even complete compromise of the system.

In this procedure, we will focus on injecting comments into a SQL query to bypass security measures and execute malicious code. By using comments, we can hide the injected SQL commands and make them harder to detect.

This technique can be used by attackers to gain unauthorized access to sensitive data, escalate privileges, and execute arbitrary code on the target system. It can also be used to perform reconnaissance and gather information about the target system.

## Requirements

1. Access to the target system

1. Knowledge of SQL injection techniques

1. A tool to send SQL queries to the target system (e.g. SQLMap)

## Defense

1. Use parameterized queries to prevent SQL injection attacks

1. Implement input validation and sanitization to prevent malicious input

1. Limit the privileges of database users to prevent privilege escalation

## Objectives

1. Inject malicious SQL commands into the target system

1. Bypass security measures and gain unauthorized access to sensitive data

1. Escalate privileges and execute arbitrary code on the target system

1. Perform reconnaissance and gather information about the target system

# Instructions

1. To execute a SQL query, replace the comment '--/**/  ' with your SQL code.

**Code**: [[--
/**/  ]]

> This JSON object represents an empty SQL query. To use this command, replace the comment '--/**/  ' with your SQL code and execute the query. The 'lang' field specifies that the code is written in SQL. The 'text' field is null, indicating that there is no text associated with the query. The 'instruction' field provides guidance on how to use this command, and the 'name' field gives a descriptive name to the command.

## Tags

- [[PostgreSQL Comments]]
- [[PostgreSQL injection]]
