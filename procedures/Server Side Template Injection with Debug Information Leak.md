---
id: e19bd1d0-54fa-4e8d-b656-5f4b099007c5
name: Server Side Template Injection with Debug Information Leak
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.470835+00:00'
updated_at: '2023-04-10T20:23:51.584252+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Debug information leak]]'
- '[[Django Templates]]'
- '[[Server Side Template Injection]]'
---

# Server Side Template Injection with Debug Information Leak

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server by injecting code into server-side templates. In the case of Django Templates, this vulnerability can be exploited through the use of debug information leak. When debug mode is e

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server by injecting code into server-side templates. In the case of Django Templates, this vulnerability can be exploited through the use of debug information leak. When debug mode is enabled, Django provides detailed error messages that can reveal sensitive information about the server configuration, including the file system structure and the names of installed packages. This information can be used by an attacker to craft a malicious payload that exploits the SSTI vulnerability and gains access to the server.

Technical Explanation:
Django Templates are a powerful tool for generating dynamic HTML pages on the server side. They allow developers to create reusable templates that can be populated with data from the server. However, if user-controlled data is used to populate the templates without proper sanitization, an attacker can inject code into the templates and execute it on the server. In the case of Django Templates, this vulnerability can be exploited through the use of debug information leak. When debug mode is enabled, Django provides detailed error messages that can reveal sensitive information about the server configuration, including the file system structure and the names of installed packages. This information can be used by an attacker to craft a malicious payload that exploits the SSTI vulnerability and gains access to the server.

Business Value:
A successful SSTI attack can result in a complete compromise of the server, allowing an attacker to steal sensitive data, modify or delete files, and use the server as a platform for further attacks. This can result in significant financial losses, damage to reputation, and legal liabilities for the affected organization.

## Requirements

1. Access to a vulnerable web application using Django Templates

1. Knowledge of the server-side template injection vulnerability

1. Access to debug mode on the server

## Defense

1. Disable debug mode on the server

1. Sanitize user input before using it to populate templates

1. Regularly update and patch the web application and server software

## Objectives

1. To gain access to the server using Server Side Template Injection

1. To obtain sensitive information about the server configuration

# Instructions

1. The debug command is used to display debugging information during the execution of a program.

**Code**: [[{% debug %}]]

> The debug command takes no arguments and is used to display information about the current state of a program. This can be useful for identifying errors or issues during the execution of the program. The output of the debug command will vary depending on the programming language being used, but it typically includes information about variables, function calls, and other relevant information. It is important to remove any debug statements from production code, as they can slow down the execution of the program and potentially expose sensitive information.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Debug information leak]]
- [[Django Templates]]
- [[Server Side Template Injection]]
