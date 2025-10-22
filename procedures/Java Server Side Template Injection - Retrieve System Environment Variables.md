---
id: 922a582b-eb7d-4490-ac05-4254c249af35
name: Java Server Side Template Injection - Retrieve System Environment Variables
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.334386+00:00'
updated_at: '2023-04-10T20:23:37.066452+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Java]]'
- '[[Java - Retrieve the system’s environment variables]]'
- '[[Server Side Template Injection]]'
---

# Java Server Side Template Injection - Retrieve System Environment Variables

## Summary

Java Server Side Template Injection is a technique that allows an attacker to execute arbitrary code on the server by injecting malicious code into a server-side template. In this specific procedure, the attacker aims to retrieve the system's environment variables. This technique can be used to gat

## Description

# Description

Java Server Side Template Injection is a technique that allows an attacker to execute arbitrary code on the server by injecting malicious code into a server-side template. In this specific procedure, the attacker aims to retrieve the system's environment variables. This technique can be used to gather sensitive information such as passwords, API keys, and other credentials. 

The attacker can use the 'System Environment Variables' command to execute the payload and retrieve the environment variables. This technique can be used to escalate privileges and gain access to sensitive data.

Business Value: This technique can be used to gather sensitive information about the target system, which can be used for further attacks. It is important to secure against this attack to prevent unauthorized access and data breach.

## Requirements

1. Access to the server-side template

1. Java environment installed on the attacker's system

1. Knowledge of Java programming language and server-side template syntax

## Defense

1. Sanitize user input to prevent injection attacks

1. Implement access control and least privilege principles to prevent unauthorized access

1. Monitor server logs for suspicious activity

## Objectives

1. Retrieve the system's environment variables

1. Escalate privileges and gain access to sensitive data

# Instructions

1. To retrieve the system environment variables in Java, you can use the `getenv()` method of the `System` class.

**Code**: [[${T(java.lang.System).getenv()}]]

> This method returns a `java.util.Map` object that contains the environment variables as key-value pairs. The keys are the names of the environment variables, and the values are their values. You can use this method to retrieve any environment variable that is set on the system where your Java program is running.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Java]]
- [[Java - Retrieve the system’s environment variables]]
- [[Server Side Template Injection]]
