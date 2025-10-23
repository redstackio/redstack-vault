---
id: 2faa5e25-1d13-46bd-aa8a-097d9531239d
name: Java Velocity Server Side Template Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.381440+00:00'
updated_at: '2023-04-10T20:23:46.660743+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Java - Velocity]]'
- '[[Server Side Template Injection]]'
---

# Java Velocity Server Side Template Injection

## Summary

Java Velocity Server Side Template Injection is a technique used by attackers to inject malicious code into server-side templates in Java web applications that use the Velocity template engine. This technique can be used to execute arbitrary code on the server, gain access to sensitive data, and ta

## Description

# Description

Java Velocity Server Side Template Injection is a technique used by attackers to inject malicious code into server-side templates in Java web applications that use the Velocity template engine. This technique can be used to execute arbitrary code on the server, gain access to sensitive data, and take control of the web application. The attack is carried out by injecting malicious code into user input fields or URL parameters, which is then executed by the server-side template engine. The business value of this technique is that it can be used to gain unauthorized access to sensitive data or take control of a web application, which can result in financial loss or reputational damage.

 

## Requirements

1. Access to a Java web application that uses the Velocity template engine

1. Knowledge of the server-side template injection vulnerability

1. Ability to inject malicious code into user input fields or URL parameters

 

## Defense

1. Use input validation and sanitization to prevent injection attacks

1. Implement server-side security controls to prevent unauthorized access to sensitive data

1. Regularly update and patch the web application and its dependencies to address known vulnerabilities

 

## Objectives

1. Inject malicious code into server-side templates

1. Execute arbitrary code on the server

1. Gain access to sensitive data

1. Take control of the web application

 

# Instructions

1. This command executes the 'whoami' command and returns the username of the current user.

 



**Code**: [[#set($str=$class.inspect("java.lang.String").type)]]



> The 'whoami' command is used to fetch the username of the current user in the terminal. This command is executed using the Velocity Template Language (VTL) and the output is returned as a string. The output of this command can be used in various scenarios, such as in shell scripts or in other commands.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Java - Velocity]]
- [[Server Side Template Injection]]


