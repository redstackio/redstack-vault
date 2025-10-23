---
id: 43785ef8-bc27-4b76-b849-48d762da6353
name: Double URL encoded Directory Traversal
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.896763+00:00'
updated_at: '2023-04-10T20:22:09.320278+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[Basic exploitation]]'
- '[[Directory Traversal]]'
- '[[Double URL encoding]]'
commands:
- '[[Convert special characters to URL encoded format]]'
- '[[View Windows ini file]]'
---

# Double URL encoded Directory Traversal

## Summary

Double URL encoded Directory Traversal is a technique used by attackers to access files and directories that are outside of the web server's root directory. The attacker sends a specially crafted HTTP request containing double URL encoded characters to the web server. If the server is vulnerable to

## Description

# Description

Double URL encoded Directory Traversal is a technique used by attackers to access files and directories that are outside of the web server's root directory. The attacker sends a specially crafted HTTP request containing double URL encoded characters to the web server. If the server is vulnerable to this attack, it will process the request and return the requested file or directory. This technique can be used to steal sensitive information or to execute arbitrary code on the target system.

From a technical perspective, this attack takes advantage of the fact that web servers may not properly handle double URL encoded characters. Double URL encoding is a technique used to bypass input validation filters that are designed to detect and block certain characters. By encoding the characters twice, the filters may not recognize them and allow them to pass through.

From a business perspective, this attack can have serious consequences. An attacker who successfully exploits this vulnerability can gain access to sensitive information, such as user credentials, financial data, or intellectual property. This can result in reputational damage, financial losses, and legal liabilities.

 

## Requirements

1. Access to a vulnerable web server

1. Knowledge of the target system's file structure

1. Ability to craft HTTP requests with double URL encoded characters

 

## Defense

1. Implement input validation filters that can detect and block double URL encoded characters

1. Use a web application firewall (WAF) that can detect and block directory traversal attacks

1. Keep software and web applications up to date with the latest security patches and updates

 

## Objectives

1. To gain unauthorized access to files and directories on the target system

1. To steal sensitive information from the target system

1. To execute arbitrary code on the target system

 

# Instructions

1. Use this cheat sheet to encode special characters with double URL encoding.

 



**Code**: [[. = %252e
/ = %252f
\ = %255c]]



> This command provides a cheat sheet that can be used to encode special characters with double URL encoding. The cheat sheet includes the most commonly used characters, such as the dot, forward slash, and backslash. By using this cheat sheet, the attacker can encode the characters twice and bypass input validation filters that are designed to block certain characters.



**Command** ([[Convert special characters to URL encoded format]]):

```bash
. = %252e
/ = %252f
\ = %255c
```



2. Use this command to exploit the Spring MVC Directory Traversal Vulnerability (CVE-2018-1271) with double URL encoding.

 

This command sends a specially crafted HTTP request to the Spring MVC web server that contains double URL encoded characters. If the server is vulnerable to this attack, it will process the request and return the requested file or directory. In this case, the attacker is requesting the win.ini file from the Windows directory. By exploiting this vulnerability, the attacker can gain access to sensitive information and potentially execute arbitrary code on the target system.



**Command** ([[View Windows ini file]]):

```bash
type win.ini
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[Convert special characters to URL encoded format]]
- [[View Windows ini file]]

## Tags

- [[Basic exploitation]]
- [[Directory Traversal]]
- [[Double URL encoding]]


