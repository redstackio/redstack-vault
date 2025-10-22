---
id: 6ab3fc32-12c4-4a1c-8e16-58c32248d66c
name: Freemarker Sandbox Bypass Remote Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.075018+00:00'
updated_at: '2023-04-10T20:23:38.534109+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
- '[[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox Evasion]]'
tags:
- '[[Freemarker]]'
- '[[Freemarker - Sandbox bypass]]'
- '[[Server Side Template Injection]]'
---

# Freemarker Sandbox Bypass Remote Code Execution

## Summary

Freemarker is a Java-based template engine that is widely used in web applications. It allows developers to generate dynamic content by merging templates with data. However, if the application is vulnerable to Server Side Template Injection (SSTI), an attacker can inject malicious code into the tem

## Description

# Description

Freemarker is a Java-based template engine that is widely used in web applications. It allows developers to generate dynamic content by merging templates with data. However, if the application is vulnerable to Server Side Template Injection (SSTI), an attacker can inject malicious code into the template, which will be executed on the server. This can lead to Remote Code Execution (RCE) and potentially compromise the entire system. Freemarker has a built-in sandbox mechanism to prevent malicious code execution. However, this can be bypassed by chaining multiple vulnerabilities. This procedure explains how to bypass the sandbox and achieve RCE on a target system.

By exploiting this vulnerability, an attacker can execute arbitrary code on the target system. This can lead to data theft, system compromise, and other malicious activities. The technical explanation involves injecting malicious code into the Freemarker template, which will be executed on the server. The business value of this attack is that it allows attackers to gain unauthorized access to sensitive information and systems, which can lead to financial losses, reputational damage, and legal consequences.

## Requirements

1. Access to the target application

1. Knowledge of Freemarker syntax

1. Ability to inject code into the target application

## Defense

1. Implement input validation and output encoding to prevent SSTI attacks

1. Disable the Freemarker sandbox if not needed

1. Regularly update the application and its dependencies to patch known vulnerabilities

## Objectives

1. Bypass the Freemarker sandbox mechanism

1. Inject and execute malicious code on the target system

# Instructions

1. This command allows remote code execution on a target system running an outdated version of Freemarker. The command uses the ObjectWrapper and Execute classes to execute arbitrary code on the target system. In order to use this command, the attacker must have access to a vulnerable version of Freemarker and be able to inject the payload into the target system.

**Code**: [[<#assign classloader=article.class.protectionDomai]]

> The payload for this command is a Freemarker template that executes the 'id' command on the target system. The command works by loading the ObjectWrapper and Execute classes through the classloader, and then using them to execute arbitrary code. The payload can be modified to execute any desired command on the target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]
- [[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox Evasion]]

## Tags

- [[Freemarker]]
- [[Freemarker - Sandbox bypass]]
- [[Server Side Template Injection]]
