---
id: 695b4ec8-aafa-42ce-b078-aa5df6f8bc27
name: SQL Injection using SQLmap with Suffix Tampering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.480484+00:00'
updated_at: '2023-04-10T20:24:19.527264+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[SQL Injection]]'
- '[[SQL injection using SQLmap]]'
- '[[Using suffix to tamper the injection]]'
commands:
- '[[Test SQL Injection on http://example.com]]'
---

# SQL Injection using SQLmap with Suffix Tampering

## Summary

SQL Injection is a type of attack that targets the database layer of a web application. SQLmap is an open-source tool used to automate the process of detecting and exploiting SQL injection vulnerabilities. By using suffix tampering, an attacker can modify the SQL injection payload to bypass securit

## Description

# Description

SQL Injection is a type of attack that targets the database layer of a web application. SQLmap is an open-source tool used to automate the process of detecting and exploiting SQL injection vulnerabilities. By using suffix tampering, an attacker can modify the SQL injection payload to bypass security measures and gain access to sensitive data. This attack can lead to data theft, account takeover, and other serious consequences. From a technical perspective, SQLmap is a powerful tool that automates the process of exploiting SQL injection vulnerabilities. It uses a variety of techniques to detect and exploit vulnerabilities, including error-based, time-based, and boolean-based techniques. By using suffix tampering, an attacker can modify the SQL injection payload to bypass security measures and gain access to sensitive data. From a business perspective, SQL injection attacks can lead to data theft, account takeover, and other serious consequences. It is important for organizations to take steps to protect against SQL injection attacks.

 

## Requirements

1. Access to a vulnerable web application

1. SQLmap tool installed on the attacker's system

 

## Defense

1. Use parameterized queries to prevent SQL injection vulnerabilities

1. Implement input validation to prevent malicious input from being processed

1. Regularly scan web applications for vulnerabilities using tools like SQLmap

 

## Objectives

1. Gain unauthorized access to sensitive data

1. Execute arbitrary SQL commands on the database

1. Steal data or credentials

 

# Instructions

1. Use this command to detect SQL injection vulnerabilities in a web application.

 



**Code**: [[python sqlmap.py -u "http://example.com/?id=1"  -p]]



> This command uses the SQLMap tool to scan a website's URL parameter for SQL injection vulnerabilities. The -u flag specifies the URL to scan, and the -p flag specifies the parameter to test. The --suffix flag adds a suffix to the payload sent to the server, which can help bypass certain security measures. Running this command can reveal potential SQL injection vulnerabilities, which can then be further investigated and patched.



**Command** ([[Test SQL Injection on http://example.com]]):

```bash
python sqlmap.py -u "http://example.com/?id=1"  -p id --suffix="-- "
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Test SQL Injection on http://example.com]]

## Tags

- [[SQL Injection]]
- [[SQL injection using SQLmap]]
- [[Using suffix to tamper the injection]]


