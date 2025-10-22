---
id: 92a19005-bc3b-4d05-b3f9-927f8ece7906
name: Polyglot Injection Sleep Command Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.609151+00:00'
updated_at: '2023-04-10T20:24:25.455342+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Polyglot injection (multicontext)]]'
- '[[SQL Injection]]'
---

# Polyglot Injection Sleep Command Procedure

## Summary

The Polyglot Injection Sleep Command Procedure is a method used to exploit SQL injection vulnerabilities in web applications. This technique involves injecting specially crafted code into input fields to manipulate the backend database. The code is designed to cause the database to pause for a set 

## Description

# Description

The Polyglot Injection Sleep Command Procedure is a method used to exploit SQL injection vulnerabilities in web applications. This technique involves injecting specially crafted code into input fields to manipulate the backend database. The code is designed to cause the database to pause for a set amount of time, which can be used to infer the success or failure of the injection. This procedure can be used to gain unauthorized access to sensitive data, modify or delete data, or execute arbitrary commands on the underlying system.

From a technical perspective, this procedure involves injecting a sleep command into the SQL query, which causes the database to pause for a set amount of time. The injection can be crafted to work across multiple database platforms, hence the term polyglot injection. The business value of this procedure is that it can be used to gain unauthorized access to sensitive data, which can be used for financial gain or to gain a competitive advantage.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of SQL injection techniques

1. Tools to craft and execute SQL injection payloads

## Defense

1. Implement input validation and sanitization techniques to prevent SQL injection vulnerabilities

1. Use parameterized queries to prevent SQL injection attacks

1. Monitor web application logs for suspicious activity

## Objectives

1. Exploit SQL injection vulnerabilities in web applications

1. Gain unauthorized access to sensitive data

1. Execute arbitrary commands on the underlying system

# Instructions

1. This command is used in SQL injection attacks to cause a delay in the response from the database server. The SLEEP function is used to pause the execution of the query for a specified amount of time. In this case, the value is set to 1 second. This can be used to detect vulnerabilities in the database and to gather information about the structure of the database. 

**Code**: [[SLEEP(1) /*' or SLEEP(1) or '" or SLEEP(1) or "*/
]]

> The SLEEP function is used to pause the execution of the query for a specified amount of time. In this case, the value is set to 1 second. The IF function is used to check the version of the database and execute a benchmark function if the version is less than 5. This can be used to detect vulnerabilities in the database and to gather information about the structure of the database. The XOR function is used to bypass certain security measures that may be in place.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[Polyglot injection (multicontext)]]
- [[SQL Injection]]
