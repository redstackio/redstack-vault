---
id: 24e1b682-8eca-469a-95d7-2f944bed0686
name: Phar Deserialization Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.455024+00:00'
updated_at: '2023-04-06T03:55:59.469556+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Regsvr32|T1117 - Regsvr32]]'
tags:
- '[[Phar Deserialization]]'
- '[[PHP Deserialization]]'
commands:
- '[[Extract files from Phar archive]]'
- '[[Retrieve contents from phar archive]]'
---

# Phar Deserialization Attack

## Summary

A Phar Deserialization attack is a technique used by attackers to exploit vulnerabilities in PHP applications that can be triggered by unserializing user-controlled data. Attackers can use the phar:// wrapper to trigger a deserialization on a specified file, which can lead to remote code execution.

## Description

# Description

A Phar Deserialization attack is a technique used by attackers to exploit vulnerabilities in PHP applications that can be triggered by unserializing user-controlled data. Attackers can use the phar:// wrapper to trigger a deserialization on a specified file, which can lead to remote code execution. This technique is used to gain initial access to a system and execute arbitrary code on the target system. It is commonly used in web application attacks to compromise web servers and gain access to sensitive data.

## Requirements

1. Access to the target system.

1. Knowledge of the target system and its vulnerabilities.

1. Ability to craft malicious serialized data.

## Defense

1. Always validate user input and sanitize it before using it in code.

1. Use the latest version of PHP and keep it up to date with security patches.

1. Implement a web application firewall (WAF) to detect and block malicious requests.

## Objectives

1. Gain remote code execution on the target system.

1. Compromise web servers and gain access to sensitive data.

# Instructions

1. 

**Code**: [[phar://]]

> The phar:// wrapper is used to access files inside a phar archive. An attacker can use this wrapper to trigger a deserialization on a specified file.

**Command** ([[Extract files from Phar archive]]):

```bash
phar://path/to/archive.phar/file.txt
```

2. 

**Code**: [[file_get_contents("phar://./archives/app.phar")]]

> The file_get_contents() function is used to read the contents of a file. An attacker can use this function to trigger a deserialization on a specified file.

**Command** ([[Retrieve contents from phar archive]]):

```bash
file_get_contents("phar://./archives/app.phar")
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Regsvr32|T1117 - Regsvr32]]

## Commands Used

- [[Extract files from Phar archive]]
- [[Retrieve contents from phar archive]]

## Tags

- [[Phar Deserialization]]
- [[PHP Deserialization]]
