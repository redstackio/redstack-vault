---
id: 2be02cf2-ff88-4fe8-a5f8-fb77ec8b5bb4
name: Basic Directory Traversal using UTF-8 Unicode encoding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.837492+00:00'
updated_at: '2023-04-10T20:22:07.225560+00:00'
tags:
- '[[Basic exploitation]]'
- '[[Directory Traversal]]'
- '[[UTF-8 Unicode encoding]]'
commands:
- '[[Character Encoding]]'
---

# Basic Directory Traversal using UTF-8 Unicode encoding

## Summary

A directory traversal attack is a technique used by attackers to gain unauthorized access to restricted directories and files. This attack is possible when a web application does not properly sanitize user input, allowing attackers to inject malicious input that can manipulate the application's fil

## Description

# Description

A directory traversal attack is a technique used by attackers to gain unauthorized access to restricted directories and files. This attack is possible when a web application does not properly sanitize user input, allowing attackers to inject malicious input that can manipulate the application's file path. By using UTF-8 Unicode encoding, attackers can bypass certain security measures that are designed to detect and block directory traversal attacks.

This procedure allows an attacker to perform a basic directory traversal attack using UTF-8 Unicode encoding. By manipulating the file path, attackers can access files that are outside of the intended directory, potentially gaining access to sensitive data or system files. This attack can be used to gather information about the target system or to execute arbitrary code.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the file system structure of the target system

1. Ability to manipulate file paths using UTF-8 Unicode encoding

 

## Defense

1. Ensure that all user input is properly sanitized to prevent directory traversal attacks

1. Implement access controls to restrict access to sensitive files and directories

1. Use file system permissions to restrict access to system files and directories

 

## Objectives

1. To gain unauthorized access to restricted directories and files

1. To gather information about the target system

1. To execute arbitrary code

 

# Instructions

1. Inject the encoded input into the file path of the vulnerable web application to bypass security measures and access restricted files and directories.

 



**Code**: [[. = %c0%2e, %e0%40%ae, %c0ae
/ = %c0%af, %e0%80%af]]



> The encoding used in this procedure allows an attacker to bypass certain security measures that are designed to detect and block directory traversal attacks. The encoding replaces certain characters in the file path with their encoded equivalents, allowing the attacker to manipulate the path and access files that are outside of the intended directory.



**Command** ([[Character Encoding]]):

```bash
. = %c0%2e, %e0%40%ae, %c0ae
/ = %c0%af, %e0%80%af, %c0%2f
\ = %c0%5c, %c0%80%5c
```



## Commands Used

- [[Character Encoding]]

## Tags

- [[Basic exploitation]]
- [[Directory Traversal]]
- [[UTF-8 Unicode encoding]]


