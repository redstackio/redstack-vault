---
id: 38eb7b06-44f0-4190-bf3f-0f9726747d79
name: Server Side Template Injection - Expression Language EL - Code Execution with
  Java RCE Payloads
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.012144+00:00'
updated_at: '2023-04-10T20:23:35.992508+00:00'
tags:
- '[[Expression Language EL]]'
- '[[Expression Language EL - Code Execution]]'
- '[[Server Side Template Injection]]'
---

# Server Side Template Injection - Expression Language EL - Code Execution with Java RCE Payloads

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a web application's templates. Expression Language (EL) is a scripting language used in web applications to dynamically generate content. By injecting malicious code into an EL expression,

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a web application's templates. Expression Language (EL) is a scripting language used in web applications to dynamically generate content. By injecting malicious code into an EL expression, an attacker can execute arbitrary code on the server. This can lead to complete compromise of the web application and the underlying server. In this procedure, we use Java RCE Payloads to demonstrate how SSTI with EL can be exploited to achieve code execution.

Technical Explanation: The attacker identifies a web application that is vulnerable to SSTI. The attacker then crafts an EL expression that includes a Java RCE Payload. When the web application evaluates the EL expression, the payload is executed on the server. This allows the attacker to execute arbitrary code on the server.

Business Value: SSTI with EL can be used to compromise web applications and underlying servers. This can lead to unauthorized access to sensitive data, theft of intellectual property, and disruption of business operations.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of SSTI and EL

1. Java RCE Payloads

 

## Defense

1. Ensure that web applications are not vulnerable to SSTI by following secure coding practices

1. Implement input validation and output encoding to prevent injection attacks

1. Monitor web application logs for suspicious activity

 

## Objectives

1. Execute arbitrary code on the server

1. Compromise the web application and underlying server

 

# Instructions

1. This JSON object contains a list of Java RCE payloads that can be used for executing arbitrary commands on a target system. The payloads use different methods such as Runtime, ProcessBuilder, Reflection & Invoke, ScriptEngineManager, and JavaClass to execute the commands. The user needs to replace the <COMMAND STRING/ARRAY> and <COMMAND ARRAY/LIST> placeholders with the actual command string or array/list to be executed. The user should also replace the x.x.x.x placeholders with the actual IP address or hostname of the target system.

 



**Code**: [[// Common RCE payloads
''.class.forName('java.lang]]



> The Java RCE payloads use various methods to execute arbitrary commands on a target system. These methods include Runtime, ProcessBuilder, Reflection & Invoke, ScriptEngineManager, and JavaClass. The user needs to replace the <COMMAND STRING/ARRAY> and <COMMAND ARRAY/LIST> placeholders with the actual command string or array/list to be executed. The user should also replace the x.x.x.x placeholders with the actual IP address or hostname of the target system. The payloads can be used for various purposes such as remote code execution, privilege escalation, and lateral movement.

## Tags

- [[Expression Language EL]]
- [[Expression Language EL - Code Execution]]
- [[Server Side Template Injection]]


