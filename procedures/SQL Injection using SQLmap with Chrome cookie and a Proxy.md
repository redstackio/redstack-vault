---
id: 0bce25df-ef38-4835-b63a-f786f1d300de
name: SQL Injection using SQLmap with Chrome cookie and a Proxy
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.455001+00:00'
updated_at: '2023-04-10T20:24:26.216359+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[SQL Injection]]'
- '[[SQL injection using SQLmap]]'
- '[[Using Chrome cookie and a Proxy]]'
---

# SQL Injection using SQLmap with Chrome cookie and a Proxy

## Summary

SQL injection attacks are one of the most common and dangerous web application vulnerabilities. Attackers can use SQL injection attacks to gain unauthorized access to sensitive data, bypass authentication mechanisms, and execute arbitrary SQL commands on the underlying database. SQLmap is a popular

## Description

# Description

SQL injection attacks are one of the most common and dangerous web application vulnerabilities. Attackers can use SQL injection attacks to gain unauthorized access to sensitive data, bypass authentication mechanisms, and execute arbitrary SQL commands on the underlying database. SQLmap is a popular open-source tool that automates the process of detecting and exploiting SQL injection vulnerabilities. By using Chrome cookies and a proxy, attackers can increase their chances of successfully exploiting SQL injection vulnerabilities. Technical details on how to use SQLmap with Chrome cookies and a proxy can be found in the documentation.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the web application's technology stack

1. SQLmap tool installed

1. Chrome browser installed

1. A proxy tool installed, such as Burp Suite

 

## Defense

1. Implement input validation and parameterized queries to prevent SQL injection attacks

1. Regularly scan web applications for vulnerabilities, including SQL injection

1. Use a web application firewall (WAF) to help detect and block SQL injection attacks

 

## Objectives

1. Exploit SQL injection vulnerabilities

1. Gain unauthorized access to sensitive data

1. Bypass authentication mechanisms

 

# Instructions

1. To scan for SQL injection vulnerabilities, run the following command:

 



**Code**: [[sqlmap -u "https://test.com/index.php?id=99" --loa]]



> This command uses sqlmap, a popular tool for detecting and exploiting SQL injection vulnerabilities. The -u flag specifies the target URL, while the --load-cookie flag loads a cookie file for authentication. The --proxy flag specifies the address of a proxy server to use during the scan. The -f flag tells sqlmap to fingerprint the database management system, and the --time-sec flag sets the maximum amount of time to wait for each request. The --level flag sets the level of tests to perform, with higher levels performing more tests at the cost of increased time and traffic.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[SQL Injection]]
- [[SQL injection using SQLmap]]
- [[Using Chrome cookie and a Proxy]]


