---
id: 2f1d95af-c677-4d14-a4f6-0b4a1d6915af
name: Basic LFI with Null Byte Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.040475+00:00'
updated_at: '2023-04-10T20:22:13.110206+00:00'
tags:
- '[[Basic LFI]]'
- '[[File Inclusion]]'
- '[[Null byte]]'
---

# Basic LFI with Null Byte Injection

## Summary

Basic LFI with Null Byte Injection is a technique that allows an attacker to read sensitive files on a target system by exploiting a vulnerability in the target application. This technique involves injecting a null byte into the file path parameter of the targeted application. This can cause the ap

## Description

# Description

Basic LFI with Null Byte Injection is a technique that allows an attacker to read sensitive files on a target system by exploiting a vulnerability in the target application. This technique involves injecting a null byte into the file path parameter of the targeted application. This can cause the application to terminate the file path string at the null byte, allowing the attacker to read files outside the intended scope of the application.

From a technical perspective, this technique takes advantage of a vulnerability in PHP versions below 5.3.4 which allowed null bytes to be used as string terminators. By injecting a null byte into the file path parameter, an attacker can trick the application into reading files outside the intended scope of the application.

The business value of this technique is that it allows an attacker to access sensitive files on a target system, such as configuration files, user credentials, and other sensitive data. This can lead to further compromise of the target system and potentially other systems within the target organization.

 

## Requirements

1. Access to the target system

1. Knowledge of the file path parameter of the targeted application

1. A vulnerable version of PHP below 5.3.4

 

## Defense

1. Ensure that all software and applications are updated to the latest version to prevent vulnerabilities that can be exploited by attackers.

1. Implement input validation and sanitization to prevent attackers from injecting malicious input into the application.

1. Implement access controls to ensure that users are only able to access the files and resources that they are authorized to access.

 

## Objectives

1. To read sensitive files on a target system

1. To gain access to configuration files and user credentials

1. To compromise the target system and potentially other systems within the target organization

 

# Instructions

1. To perform a Basic LFI with Null Byte Injection attack, follow these steps:

1. Identify a vulnerable version of PHP below 5.3.4.
2. Identify a target application that is vulnerable to LFI attacks.
3. Inject a null byte into the file path parameter of the targeted application.
4. Read the sensitive files on the target system outside the intended scope of the application.

 



**Code**: [[http://example.com/index.php?page=../../../etc/pas]]



> The command injects a null byte into the file path parameter of the targeted application, causing the application to terminate the file path string at the null byte. This allows the attacker to read files outside the intended scope of the application.

## Tags

- [[Basic LFI]]
- [[File Inclusion]]
- [[Null byte]]


