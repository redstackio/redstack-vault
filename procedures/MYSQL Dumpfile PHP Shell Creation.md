---
id: 8a718c91-9b49-4228-a4c8-56184fefa77b
name: MYSQL Dumpfile PHP Shell Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.851406+00:00'
updated_at: '2023-04-10T20:22:53.820243+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tags:
- '[[Into dumpfile method]]'
- '[[MYSQL Injection]]'
- '[[MYSQL Write a shell]]'
---

# MYSQL Dumpfile PHP Shell Creation

## Summary

This procedure involves exploiting a MYSQL injection vulnerability to create a PHP shell using the dumpfile method. An attacker can use this technique to gain remote access to a system and execute arbitrary commands. The attacker first identifies a MYSQL injection vulnerability and then crafts a SQ

## Description

# Description

This procedure involves exploiting a MYSQL injection vulnerability to create a PHP shell using the dumpfile method. An attacker can use this technique to gain remote access to a system and execute arbitrary commands. The attacker first identifies a MYSQL injection vulnerability and then crafts a SQL payload to create a PHP shell using the dumpfile method. Once the PHP shell is created, the attacker can use it to execute commands and gain full access to the system. This technique can be used to escalate privileges, exfiltrate data, or install persistent backdoors.

 

## Requirements

1. Access to a vulnerable MYSQL database

1. Knowledge of MYSQL injection techniques

1. Ability to craft SQL payloads

1. Ability to execute commands on the target system

 

## Defense

1. Implement input validation and sanitization to prevent MYSQL injection vulnerabilities

1. Use prepared statements or parameterized queries to prevent MYSQL injection vulnerabilities

1. Implement network segmentation and access controls to limit access to sensitive systems and data

 

## Objectives

1. Gain remote access to the target system

1. Execute arbitrary commands on the target system

1. Escalate privileges, exfiltrate data, or install persistent backdoors

 

# Instructions

1. This command allows an attacker to inject SQL code to create a PHP shell on the targeted system. The payload in hexadecimal format is injected into the SELECT statement, which is then executed to create a PHP shell file on the system.

 



**Code**: [[[...] UNION SELECT 0xPHP_PAYLOAD_IN_HEX, NULL, NUL]]



> The payload in this command is in hexadecimal format and is injected into the SELECT statement using the UNION operator. The payload is then written to a file using the INTO DUMPFILE command. The file is created in the specified directory, which in this case is C:/Program Files/EasyPHP-12.1/www/ or /var/www/html/images/ depending on the system. Once the file is created, the attacker can use it to execute arbitrary commands on the targeted system.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote File Copy|T1105 - Remote File Copy]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

## Tags

- [[Into dumpfile method]]
- [[MYSQL Injection]]
- [[MYSQL Write a shell]]


