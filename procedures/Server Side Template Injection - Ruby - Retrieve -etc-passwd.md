---
id: 7d93b700-b804-4b2c-9c55-f3e63242c2c5
name: Server Side Template Injection - Ruby - Retrieve /etc/passwd
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.182983+00:00'
updated_at: '2023-04-10T20:23:34.415425+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Ruby]]'
- '[[Ruby - Retrieve /etc/passwd]]'
- '[[Server Side Template Injection]]'
---

# Server Side Template Injection - Ruby - Retrieve /etc/passwd

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject code into a web application template that is then executed on the server. In this case, the attacker is using Ruby to retrieve the /etc/passwd file. This is achieved by injecting Ruby code into a template tha

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject code into a web application template that is then executed on the server. In this case, the attacker is using Ruby to retrieve the /etc/passwd file. This is achieved by injecting Ruby code into a template that will execute the 'File.read' command to retrieve the contents of the /etc/passwd file. The attacker can then use this information to further their attack.

From an offensive standpoint, an attacker could use this technique to gain access to sensitive information such as usernames and passwords. From a technical perspective, this technique takes advantage of the trust between the web application and the server, allowing the attacker to execute arbitrary code on the server. From a business perspective, this vulnerability could lead to a loss of sensitive data and damage to the company's reputation.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of Ruby and Server Side Template Injection

## Defense

1. Implement input validation and sanitization to prevent injection attacks

1. Disable unnecessary functionality and remove unnecessary dependencies

1. Implement strict file permissions to limit access to sensitive files

## Objectives

1. Retrieve sensitive information such as usernames and passwords

# Instructions

1. To read a file in Ruby, use the File.open method. The method takes one argument - the path to the file you want to read. The read method can then be called on the file object to retrieve its contents.

**Code**: [[<%= File.open('/etc/passwd').read %>]]

> This command reads the contents of the /etc/passwd file in the Linux operating system. This file contains information about the system's users and their login credentials. By reading this file, a user with sufficient privileges can gain access to sensitive information about the system's users.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Ruby]]
- [[Ruby - Retrieve /etc/passwd]]
- [[Server Side Template Injection]]
