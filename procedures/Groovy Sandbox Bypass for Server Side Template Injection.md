---
id: 9c75b10f-f307-48e9-86ef-fb46c940664d
name: Groovy Sandbox Bypass for Server Side Template Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.230885+00:00'
updated_at: '2023-04-10T20:23:43.127826+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Groovy]]'
- '[[Groovy - Sandbox Bypass]]'
- '[[Server Side Template Injection]]'
---

# Groovy Sandbox Bypass for Server Side Template Injection

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a web application's template engine. Groovy is a popular scripting language that is often used in template engines. This procedure focuses on bypassing the Groovy sandbox to execute arbitr

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a web application's template engine. Groovy is a popular scripting language that is often used in template engines. This procedure focuses on bypassing the Groovy sandbox to execute arbitrary code. The Groovy sandbox is a security feature that restricts the execution of certain code, but it can be bypassed using certain techniques.

From an offensive perspective, this procedure can be used to gain remote code execution on a target system. By injecting malicious code into a web application's template engine, an attacker can execute arbitrary code on the server. This can lead to data exfiltration, privilege escalation, or complete compromise of the target system.

From a technical standpoint, this procedure involves identifying a vulnerable web application that uses Groovy as its template engine. The attacker then injects Groovy code that bypasses the sandbox and executes arbitrary code. This can be achieved using techniques such as disabling the sandbox or using reflective classes.

From a business perspective, this procedure highlights the importance of secure coding practices and regular vulnerability assessments. By identifying and patching vulnerabilities in web applications, organizations can prevent attackers from gaining access to sensitive data or compromising their systems.

## Requirements

1. Access to a vulnerable web application that uses Groovy as its template engine

1. Knowledge of Groovy syntax and the Groovy sandbox

## Defense

1. Regularly update and patch web applications to prevent vulnerabilities such as SSTI

1. Implement strict input validation to prevent malicious code injection

1. Use a web application firewall (WAF) to detect and block malicious requests

## Objectives

1. Bypass the Groovy sandbox to execute arbitrary code

1. Gain remote code execution on a target system

# Instructions

1. This command is used to get the name of the user who is currently logged in to the system.

**Code**: [[${ @ASTTest(value={assert java.lang.Runtime.getRun]]

> The 'whoami' command is a Unix command that is used to print the username of the current user. This command is useful in shell scripts and other automation tasks where the username of the current user is required. When this command is executed, it returns the name of the current user as a string. This command does not take any arguments.

2. Execute Calculator

**Code**: [[${ new groovy.lang.GroovyClassLoader().parseClass(]]

> This command will execute the calculator application on the system where the script is being run. It uses a GroovyClassLoader to parse and execute the specified command.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Groovy]]
- [[Groovy - Sandbox Bypass]]
- [[Server Side Template Injection]]
