---
id: b0bf3c7b-c5f1-430e-9b35-8d7ab5ddcba5
name: SQLite Injection via Remote Command Execution using Attach Database Command
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.151960+00:00'
updated_at: '2023-04-10T20:24:29.615227+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Remote Command Execution using SQLite command - Attach Database]]'
- '[[SQLite Injection]]'
---

# SQLite Injection via Remote Command Execution using Attach Database Command

## Summary

SQLite injection is a type of injection attack that targets SQLite databases. In this procedure, we will be focusing on Remote Command Execution using SQLite command - Attach Database. This command can be used to execute arbitrary commands on the operating system. This technique can be used by an a

## Description

# Description

SQLite injection is a type of injection attack that targets SQLite databases. In this procedure, we will be focusing on Remote Command Execution using SQLite command - Attach Database. This command can be used to execute arbitrary commands on the operating system. This technique can be used by an attacker to gain remote access to the system and execute malicious commands. By injecting a specially crafted SQL query, an attacker can execute arbitrary commands on the target system. The attacker can then use these commands to steal sensitive information or cause damage to the system.

From a technical perspective, this technique works by injecting a specially crafted SQL query into an application that uses SQLite as its backend database. The query is designed to execute arbitrary commands on the operating system. This technique is particularly dangerous because it allows an attacker to bypass application-level security controls and execute commands directly on the underlying operating system.

The business value of this procedure is that it allows an attacker to gain remote access to a system and execute arbitrary commands. This can be used to steal sensitive information or cause damage to the system. It is important for organizations to be aware of this technique and take steps to protect their systems from this type of attack.

## Requirements

1. Access to a vulnerable application that uses SQLite as its backend database

1. Knowledge of SQL injection techniques

## Defense

1. Ensure that all applications that use SQLite as their backend database are properly configured and secured

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

## Objectives

1. Gain remote access to the target system

1. Execute arbitrary commands on the target system

# Instructions

1. This command is used to inject PHP code into the SQLite database by attaching a new database file and creating a table within it. The code that is injected allows for command execution via the 'cmd' parameter passed in the GET request. 

**Code**: [[ATTACH DATABASE '/var/www/lol.php' AS lol;
CREATE ]]

> The 'ATTACH DATABASE' command is used to attach a new SQLite database file to the current database connection. In this case, the file '/var/www/lol.php' is attached and given the alias 'lol'. The 'CREATE TABLE' command is then used to create a new table named 'pwn' within the 'lol' database. The 'INSERT INTO' command is used to insert PHP code into the 'dataz' column of the 'pwn' table. This PHP code allows for command execution via the 'cmd' parameter passed in the GET request. The double hyphen '--' at the end of the SQL query is used to comment out any remaining SQL code that may follow.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Tags

- [[Remote Command Execution using SQLite command - Attach Database]]
- [[SQLite Injection]]
