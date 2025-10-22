---
id: 9e0b3793-7090-4f56-acc2-1a06e4606044
name: SQL Injection using SQLmap with Proxy
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.429601+00:00'
updated_at: '2023-04-10T20:24:18.028839+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[SQL Injection]]'
- '[[SQL injection using SQLmap]]'
- '[[Using a proxy with SQLmap]]'
commands:
- '[[SQL Injection scan using sqlmap]]'
---

# SQL Injection using SQLmap with Proxy

## Summary

SQL injection is a technique used to exploit security vulnerabilities in web applications that use SQL databases. Attackers use SQL injection to attack data-driven applications, steal sensitive information, and execute unauthorized commands. SQLmap is a popular open-source tool used for automated S

## Description

# Description

SQL injection is a technique used to exploit security vulnerabilities in web applications that use SQL databases. Attackers use SQL injection to attack data-driven applications, steal sensitive information, and execute unauthorized commands. SQLmap is a popular open-source tool used for automated SQL injection attacks. By using a proxy with SQLmap, attackers can hide their IP address and evade detection. Using a proxy can also help attackers bypass network security measures such as firewalls and intrusion detection systems. 

From a technical perspective, SQL injection attacks work by injecting malicious SQL code into input fields on a web application. This code is then executed by the application's backend database, giving the attacker access to sensitive data or allowing them to execute unauthorized commands. SQLmap automates this process by identifying vulnerable input fields and automatically injecting malicious SQL code. By using a proxy, attackers can hide their IP address and evade detection.

From a business perspective, SQL injection attacks can be devastating. They can result in the theft of sensitive information such as customer data, financial information, and intellectual property. They can also lead to unauthorized access to critical systems and the execution of unauthorized commands.

## Requirements

1. Access to a vulnerable web application

1. SQLmap installed on the attacker's system

1. A proxy server to hide the attacker's IP address

## Defense

1. Implement input validation and parameterized queries to prevent SQL injection attacks

1. Use a web application firewall to detect and block SQL injection attacks

1. Monitor network traffic for suspicious activity and investigate any anomalies

## Objectives

1. Identify SQL injection vulnerabilities in web applications

1. Exploit SQL injection vulnerabilities to gain unauthorized access to sensitive data or execute unauthorized commands

1. Evade detection by using a proxy to hide the attacker's IP address

# Instructions

1. Use this command to scan a target website for SQL injection vulnerabilities. This command uses sqlmap which is a popular open-source tool for detecting and exploiting SQL injection flaws. The -u flag is used to specify the target URL and the --proxy flag is used to specify the proxy server to be used for the scan.

**Code**: [[sqlmap -u "http://www.target.com" --proxy="http://]]

> SQL injection is a type of web application security vulnerability that allows attackers to inject malicious SQL statements into web application inputs in order to access sensitive data or perform unauthorized actions. Sqlmap automates the process of detecting and exploiting SQL injection flaws and is a powerful tool for penetration testers and security researchers.

**Command** ([[SQL Injection scan using sqlmap]]):

```bash
sqlmap -u "http://www.target.com" --proxy="http://127.0.0.1:8080"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[SQL Injection scan using sqlmap]]

## Tags

- [[SQL Injection]]
- [[SQL injection using SQLmap]]
- [[Using a proxy with SQLmap]]
