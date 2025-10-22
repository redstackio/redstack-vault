---
id: a114bef7-dedd-4a6c-99e7-6bfac6f546e6
name: MYSQL Injection - Write Shell using Outfile Method
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.815745+00:00'
updated_at: '2023-04-10T20:22:49.769833+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Unix Shell|T1059.004 - Unix Shell]]'
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Into outfile method]]'
- '[[MYSQL Injection]]'
- '[[MYSQL Write a shell]]'
---

# MYSQL Injection - Write Shell using Outfile Method

## Summary

A MYSQL injection attack is a technique where an attacker inserts malicious SQL statements into a MYSQL database, thereby gaining access to sensitive information or executing unauthorized commands. In this specific procedure, the attacker will use the 'Into outfile' method to write a shell on the t

## Description

# Description

A MYSQL injection attack is a technique where an attacker inserts malicious SQL statements into a MYSQL database, thereby gaining access to sensitive information or executing unauthorized commands. In this specific procedure, the attacker will use the 'Into outfile' method to write a shell on the target system. 

The 'Into outfile' method is a MYSQL statement that allows the user to write the results of a query to a file on the server. This can be used to create a shell on the target system that the attacker can use to execute commands and gain further access. The attacker can then use this shell to escalate privileges, exfiltrate data or install additional malware. 

The business value of this attack is that it allows an attacker to gain unauthorized access to sensitive data and resources on the target system, which can result in financial loss, reputational damage, and legal consequences.

## Requirements

1. Access to a MYSQL database on the target system

1. Knowledge of MYSQL injection techniques

1. Ability to execute SQL statements on the target system

## Defense

1. Use parameterized queries to prevent SQL injection attacks

1. Limit the privileges of the MYSQL user to prevent unauthorized access

1. Monitor for suspicious activity, such as the creation of new files or unusual network traffic

## Objectives

1. Gain unauthorized access to the target system

1. Write a shell on the target system using the 'Into outfile' method

1. Execute commands on the target system using the shell

# Instructions

1. This command is used for SQL injection attacks. It is used to write files to the server by exploiting SQL injection vulnerabilities. The attacker can inject malicious code into the database, which can be executed on the server to create a backdoor or to execute arbitrary commands on the server.

**Code**: [[[...] UNION SELECT "<?php system($_GET['cmd']); ?>]]

> This command has multiple variations. The first variation uses the 'into outfile' clause to write a PHP script with a backdoor to the server. The second variation uses the 'into outfile' clause to write a PHP script that displays PHP configuration information. The third variation uses the 'into outfile' clause to write a PHP script with a backdoor to the server. The fourth variation uses the 'into outfile' clause to write a PHP script with a backdoor to the server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Unix Shell|T1059.004 - Unix Shell]]
- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Into outfile method]]
- [[MYSQL Injection]]
- [[MYSQL Write a shell]]
