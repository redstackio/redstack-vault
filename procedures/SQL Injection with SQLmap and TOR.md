---
id: 60900bce-21b5-4d53-9ccb-0c8e8b5cfc7c
name: SQL Injection with SQLmap and TOR
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.403383+00:00'
updated_at: '2023-04-10T20:24:27.792017+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[SQL Injection]]'
- '[[SQL injection using SQLmap]]'
- '[[Using TOR with SQLmap]]'
commands:
- '[[SQL Injection Vulnerability Scan]]'
---

# SQL Injection with SQLmap and TOR

## Summary

SQL injection is a type of attack that allows an attacker to execute malicious SQL statements that control a web application's database server. SQLmap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws. By using TOR with SQLmap, an 

## Description

# Description

SQL injection is a type of attack that allows an attacker to execute malicious SQL statements that control a web application's database server. SQLmap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws. By using TOR with SQLmap, an attacker can anonymize their traffic and make it more difficult to trace the source of the attack. 

From an offensive standpoint, SQL injection can be used to steal sensitive data, modify database contents, and even take over the entire web application. In technical terms, SQL injection occurs when an attacker is able to inject malicious SQL code into an application's input fields. This code is then executed by the database server, giving the attacker control over the database. From a business perspective, SQL injection can lead to data breaches, financial losses, and damage to a company's reputation.


 

## Requirements

1. Access to a vulnerable web application

1. SQLmap installed on the attacker's machine

1. TOR installed on the attacker's machine

 

## Defense

1. Ensure that all input fields are properly sanitized and validated to prevent SQL injection attacks

1. Implement a web application firewall (WAF) to detect and block SQL injection attacks

1. Regularly scan web applications for vulnerabilities and apply security patches as needed

 

## Objectives

1. Identify SQL injection vulnerabilities in a web application

1. Exploit SQL injection vulnerabilities to gain access to a database

1. Anonymize traffic to make it more difficult to trace the source of the attack

 

# Instructions

1. This command is used to scan a target website for SQL injection vulnerabilities. The command uses the sqlmap tool and the Tor network to anonymize the scan. The `--tor` flag enables the use of Tor, while `--tor-type=SOCKS5` specifies the type of Tor connection. The `--time-sec` flag sets the maximum time in seconds for each request, while `--check-tor` verifies that the Tor connection is working. The `--level` flag sets the level of tests to perform, with 5 being the highest level. The `--risk` flag sets the risk level for the tests, with 3 being the highest risk level. The `--threads` flag sets the number of threads to use for the scan.

 



**Code**: [[sqlmap -u "http://www.target.com" --tor --tor-type]]



> The `-u` flag specifies the target URL to scan for SQL injection vulnerabilities. The `sqlmap` tool is a popular open-source tool used by security professionals to automate the process of detecting and exploiting SQL injection vulnerabilities. The tool is highly configurable and can be used to perform a variety of tests against a target website. The use of Tor helps to anonymize the scan and prevent the target website from detecting the source of the scan.



**Command** ([[SQL Injection Vulnerability Scan]]):

```bash
sqlmap -u "http://www.target.com" --tor --tor-type=SOCKS5 --time-sec 11 --check-tor --level=5 --risk=3 --threads=5
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[SQL Injection Vulnerability Scan]]

## Tags

- [[SQL Injection]]
- [[SQL injection using SQLmap]]
- [[Using TOR with SQLmap]]


