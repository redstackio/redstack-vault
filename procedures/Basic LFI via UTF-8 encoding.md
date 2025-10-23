---
id: 1d49fedb-cf7a-4c44-bb11-ff7d1bd1f57d
name: Basic LFI via UTF-8 encoding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.088492+00:00'
updated_at: '2023-04-10T20:22:13.465525+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Basic LFI]]'
- '[[File Inclusion]]'
- '[[UTF-8 encoding]]'
---

# Basic LFI via UTF-8 encoding

## Summary

A Local File Inclusion (LFI) vulnerability allows an attacker to include files on a server through the web browser. When the application does not properly sanitize user input, an attacker can include files on the server that are not intended to be viewed by the user. In this case, the attacker can 

## Description

# Description

A Local File Inclusion (LFI) vulnerability allows an attacker to include files on a server through the web browser. When the application does not properly sanitize user input, an attacker can include files on the server that are not intended to be viewed by the user. In this case, the attacker can use UTF-8 encoding to bypass filters and include files that are outside the web root directory.

Technical Explanation: This technique takes advantage of the vulnerability in the application that does not properly validate user input. With the use of UTF-8 encoding, an attacker can bypass filters and include files that are outside the web root directory. The attacker can then view the contents of these files, which may contain sensitive information such as passwords, configuration files, and other critical data.

Business Value: This technique can be used by attackers to gain access to sensitive information stored on the server. By exploiting LFI vulnerabilities, attackers can bypass authentication and authorization controls and gain access to data that they are not authorized to view.

 

## Requirements

1. Access to a vulnerable web application.

 

## Defense

1. Ensure that user input is properly validated and sanitized to prevent LFI vulnerabilities.

1. Use web application firewalls to detect and block LFI attacks.

1. Restrict access to sensitive files and directories to prevent unauthorized access.

 

## Objectives

1. To include files on the server that are not intended to be viewed by the user.

1. To view the contents of files that are outside the web root directory.

 

# Instructions

1. 1. Replace the URL with the vulnerable web application URL.
2. Replace the file name with the name of the file that you want to include.
3. Use the UTF-8 encoding to bypass filters and include files that are outside the web root directory.

 



**Code**: [[http://example.com/index.php?page=%c0%ae%c0%ae/%c0]]



> The attacker can use the above command to exploit the LFI vulnerability using UTF-8 encoding. The attacker can replace the URL with the URL of the vulnerable web application and the file name with the name of the file that they want to include. The attacker can use the UTF-8 encoding to bypass filters and include files that are outside the web root directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Basic LFI]]
- [[File Inclusion]]
- [[UTF-8 encoding]]


