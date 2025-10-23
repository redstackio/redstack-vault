---
id: dd16be03-466b-4167-a0f2-0c847fce7274
name: Server Side Template Injection with Java Spring
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.400237+00:00'
updated_at: '2023-04-10T20:23:33.340940+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Java - Spring]]'
- '[[Server Side Template Injection]]'
---

# Server Side Template Injection with Java Spring

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a server-side template, which is then executed by the server. In Java Spring, SSTI can be exploited through the use of Expression Language (EL) or Thymeleaf template engine. Attackers can 

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a server-side template, which is then executed by the server. In Java Spring, SSTI can be exploited through the use of Expression Language (EL) or Thymeleaf template engine. Attackers can use this technique to execute arbitrary code on the server, gain access to sensitive information, or perform other malicious activities. This procedure provides an overview of how to exploit SSTI in Java Spring and its potential impact on an organization.

 

## Requirements

1. Access to the target application

1. Knowledge of Java Spring and SSTI vulnerability

1. Access to a web browser and a command-line interface

 

## Defense

1. Implement input validation and sanitization to prevent injection attacks

1. Use a Content Security Policy (CSP) to restrict the sources of content that can be loaded by a web page

1. Regularly update and patch the software to fix known vulnerabilities

 

## Objectives

1. Exploit SSTI vulnerability in Java Spring

1. Execute arbitrary code on the server

1. Gain access to sensitive information

 

# Instructions

1. This command executes the 'id' command on the system and returns the output as a string. It also performs a simple arithmetic operation of 7 multiplied by 7 using the *{} syntax.

 



**Code**: [[*{7*7}
*{T(org.apache.commons.io.IOUtils).toString]]



> The *{} syntax is used to execute arbitrary code in the context of the current script. In this case, it is used to perform a simple arithmetic operation. The T() function is used to call static methods in Java classes, and in this case it is used to execute the 'id' command and return its output as a string.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Java - Spring]]
- [[Server Side Template Injection]]


