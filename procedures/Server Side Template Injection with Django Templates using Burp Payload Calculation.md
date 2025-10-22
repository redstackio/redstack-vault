---
id: c8aaf04b-bcbd-4cb5-8828-92ddc0f7a577
name: Server Side Template Injection with Django Templates using Burp Payload Calculation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.385153+00:00'
updated_at: '2023-04-10T20:23:45.020473+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Template Injection|T1221 - Template Injection]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
tags:
- '[[Detection]]'
- '[[Django Templates]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Burp Payload]]'
- '[[Calculate]]'
- '[[Caution]]'
- '[[Caution]]'
---

# Server Side Template Injection with Django Templates using Burp Payload Calculation

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server-side. In the context of Django Templates, it occurs when user-controlled data is used to render templates without proper input validation. This can lead to remote code execution 

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server-side. In the context of Django Templates, it occurs when user-controlled data is used to render templates without proper input validation. This can lead to remote code execution (RCE) and other serious consequences. 

To exploit this vulnerability, an attacker can use Burp Payload Calculation to generate payloads that can be injected into the vulnerable templates. Once the payload is injected and executed, the attacker can gain control over the server and perform various malicious activities.

This procedure can be used by red teamers to test the security of web applications and by attackers to compromise vulnerable systems.

## Requirements

1. Access to a vulnerable web application

1. Burp Suite Professional

## Defense

1. Implement proper input validation and sanitization techniques to prevent SSTI vulnerabilities

1. Use a Content Security Policy (CSP) to limit the types of scripts that can be executed on the page

1. Regularly update and patch the web application and its dependencies to prevent known vulnerabilities

## Objectives

1. To exploit the SSTI vulnerability in Django Templates

1. To achieve remote code execution on the server

1. To gain control over the server and perform malicious activities

# Instructions

1. Use the Burp Payload Calculation command to calculate the value of a payload using the specified formula.

**Code**: [[{% csrf_token %} # Causes error with Jinja2
{{ 7*7]]

> The 'data' field contains a formula that is used to calculate the final payload value. The formula is made up of different components, including the Burp Payload, which is represented by 'ih0vr{{364|add:733}}d121r'. The formula can be modified to suit your specific needs. The 'lang' field specifies the programming language used in the formula. The 'text' field provides additional information about the Django Templates rendering engine and how it works. Use the 'instruction' field to provide specific instructions on how to use this command.

**Command** ([[Calculate]]):

```bash
{{ 7*7 }}
```

**Command** ([[Burp Payload]]):

```bash
ih0vr{{364|add:733}}d121r
```

**Command** ([[Caution]]):

```bash
{% csrf_token %}
```

**Command** ([[Caution]]):

```bash
{{ 7*7 }}
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Template Injection|T1221 - Template Injection]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]

## Commands Used

- [[Burp Payload]]
- [[Calculate]]
- [[Caution]]
- [[Caution]]

## Tags

- [[Detection]]
- [[Django Templates]]
- [[Server Side Template Injection]]
