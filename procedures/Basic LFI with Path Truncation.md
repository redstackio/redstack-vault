---
id: 885cc58c-1673-43fc-86e5-736bf9909478
name: Basic LFI with Path Truncation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.117950+00:00'
updated_at: '2023-04-10T20:22:17.348416+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[AppleScript|T1059.002 - AppleScript]]'
tags:
- '[[Basic LFI]]'
- '[[File Inclusion]]'
- '[[Path and dot truncation]]'
---

# Basic LFI with Path Truncation

## Summary

Basic LFI with Path Truncation is a technique that allows an attacker to read files on a web server by exploiting a vulnerability in a web application. This technique is used to bypass input validation and access files that are not intended to be accessed by the attacker. By truncating the path and

## Description

# Description

Basic LFI with Path Truncation is a technique that allows an attacker to read files on a web server by exploiting a vulnerability in a web application. This technique is used to bypass input validation and access files that are not intended to be accessed by the attacker. By truncating the path and using dot and slash characters, the attacker can bypass certain security checks and access sensitive files. The technical explanation of this technique involves manipulating the file inclusion parameter to point to a file outside of the intended directory. The business value of this technique is that an attacker can access sensitive information such as passwords, configuration files, and other sensitive data.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the file inclusion parameter

 

## Defense

1. Implement input validation to prevent malicious input

1. Use a web application firewall to detect and block LFI attacks

1. Restrict access to sensitive files and directories

 

## Objectives

1. To read files on a web server that are not intended to be accessed by the attacker

1. To bypass input validation and security checks

 

# Instructions

1. To perform Basic LFI with Path Truncation, the attacker needs to manipulate the file inclusion parameter to point to a file outside of the intended directory. The attacker can use dot and slash characters to bypass certain security checks and access sensitive files.

 



**Code**: [[http://example.com/index.php?page=../../../etc/pas]]



> The attacker can use the following commands:
- http://example.com/index.php?page=../../../etc/passwd
- http://example.com/index.php?page=../../../etc/passwd/./././././.
- http://example.com/index.php?page=../../../[ADD MORE]../../../../etc/passwd

The attacker can use dot and slash characters to bypass certain security checks and access sensitive files. On most PHP installations a filename longer than 4096 bytes will be cut off so any excess chars will be thrown away.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[AppleScript|T1059.002 - AppleScript]]

## Tags

- [[Basic LFI]]
- [[File Inclusion]]
- [[Path and dot truncation]]


