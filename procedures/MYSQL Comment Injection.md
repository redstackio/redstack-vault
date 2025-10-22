---
id: b6660d4b-7797-4421-be96-ac0392f7bbc4
name: MYSQL Comment Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.209682+00:00'
updated_at: '2023-04-10T20:22:48.643424+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[MYSQL comment]]'
- '[[MYSQL Injection]]'
---

# MYSQL Comment Injection

## Summary

MYSQL Comment Injection is a technique used by attackers to inject malicious code into a MYSQL database through comments. This technique can be used to bypass input validation checks and execute unauthorized commands against the database. By injecting comments into MYSQL queries, attackers can mani

## Description

# Description

MYSQL Comment Injection is a technique used by attackers to inject malicious code into a MYSQL database through comments. This technique can be used to bypass input validation checks and execute unauthorized commands against the database. By injecting comments into MYSQL queries, attackers can manipulate the database and potentially gain access to sensitive data. This technique can be used in combination with other attack methods to achieve a more comprehensive attack.

## Requirements

1. Access to a vulnerable MYSQL database

1. Knowledge of MYSQL Comment Injection technique

## Defense

1. Implement input validation checks to prevent MYSQL Comment Injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Regularly update and patch MYSQL databases to address known vulnerabilities

## Objectives

1. Inject malicious code into a MYSQL database

1. Bypass input validation checks

1. Execute unauthorized commands against the database

# Instructions

1. To add comments in MYSQL, there are three ways: 
1. Single-line comments: To add a single-line comment in MYSQL, use ‘--’ followed by the comment text. 
2. Multi-line comments: To add a multi-line comment in MYSQL, use ‘/*’ followed by the comment text and end the comment with ‘*/’. 
3. Special comments: Special comments in MYSQL are used to provide instructions to the MYSQL server. Special comments are written using the syntax ‘/*! comment */’. 

**Code**: [[# MYSQL Comment
-- comment [Note the space after t]]

> The ‘data’ field in the JSON object demonstrates the usage of all three types of comments in MYSQL. The ‘/*!32302 10*/’ in the data is an example of a special comment. The number ‘32302’ represents the version of MYSQL and the number ‘10’ represents the number of seconds the MYSQL server should wait before timing out. Special comments are useful when you want to provide specific instructions to the MYSQL server. 

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[MYSQL comment]]
- [[MYSQL Injection]]
